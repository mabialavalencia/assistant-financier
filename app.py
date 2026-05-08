import streamlit as st
from extracteur_documents import ExtracteurDocuments
from classifieur import ClassifieurDocuments
from ner_financier import NERFinancier
from indexeur import IndexeurRAG
from chatbot import ChatbotFinancier
import os
import tempfile

st.set_page_config(page_title="Assistant Financier", layout="wide")
st.title("📄 Assistant financier")

@st.cache_resource
def init_modules():
    return {
        "classifieur": ClassifieurDocuments(),
        "ner": NERFinancier(),
        "indexeur": IndexeurRAG(),
        "chatbot": ChatbotFinancier()
    }

modules = init_modules()

with st.sidebar:
    st.header("1. Importer un document")
    uploaded_file = st.file_uploader("Choisir un fichier (PDF, DOCX, image)",
                                     type=["pdf", "docx", "png", "jpg", "jpeg"])
    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=f"_{uploaded_file.name}") as tmp:
            tmp.write(uploaded_file.getbuffer())
            temp_path = tmp.name

        with st.spinner("Analyse en cours..."):
            texte, tables = ExtracteurDocuments.detect_and_extract(temp_path)
            type_doc, score = modules["classifieur"].predire(texte)
            entites = modules["ner"].fusionner(texte)
            nb_chunks = modules["indexeur"].indexer_document(texte, metadatas=[{"source": uploaded_file.name}])
        st.success(f"Document traité : {type_doc} (confiance {score:.2f})")
        st.session_state.type_doc = type_doc
        st.session_state.doc_valide = (type_doc == "rapport annuel")
        if not st.session_state.doc_valide:
            st.error("⚠️ Ce document n'est pas un rapport annuel. Le chat ne sera pas disponible.")
        else:
            st.info("✅ Rapport annuel détecté. Vous pouvez poser des questions.")
        st.write(f"**Chunks indexés :** {nb_chunks}")
        st.json({"type": type_doc, "entites": entites})
        os.unlink(temp_path)

    st.header("2. Statut")
    st.info("Modèles chargés localement (pas besoin d'Ollama)")

st.header("💬 Posez vos questions")

if st.session_state.get("doc_valide", False):
    if "messages" not in st.session_state:
        st.session_state.messages = []
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
    if prompt := st.chat_input("Ex: Quel est le PNB 2024 ?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            with st.spinner("Recherche..."):
                reponse = modules["chatbot"].generer_reponse(prompt)
            st.markdown(reponse)
        st.session_state.messages.append({"role": "assistant", "content": reponse})
else:
    st.info("📌 Veuillez d'abord importer un rapport annuel pour poser des questions.")