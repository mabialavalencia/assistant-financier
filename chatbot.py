import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from indexeur import IndexeurRAG

class ChatbotFinancier:
    def __init__(self, model_name="google/flan-t5-small"):
        self.indexeur = IndexeurRAG()
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(self.device)
        self.max_new_tokens = 150

    def generer_reponse(self, question):
        docs = self.indexeur.rechercher(question, k=4)
        contexte = "\n\n".join([doc.page_content for doc in docs])
        prompt = f"""Réponds uniquement à partir des extraits ci-dessous.
Si l'information n'est pas présente, réponds : "Information non trouvée."

EXTRAITS:
{contexte}

QUESTION: {question}
RÉPONSE:"""

        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512).to(self.device)
        outputs = self.model.generate(**inputs, max_new_tokens=self.max_new_tokens)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)