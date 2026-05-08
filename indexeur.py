from sentence_transformers import SentenceTransformer
import numpy as np
import uuid
import os
import pickle

class IndexeurRAG:
    def __init__(self, persist_dir="./index_data"):
        self.persist_dir = persist_dir
        self.model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
        self.chunks = []
        self.embeddings = []
        self.metadatas = []
        self.ids = []
        os.makedirs(persist_dir, exist_ok=True)
        self._load()

    def _save(self):
        with open(os.path.join(self.persist_dir, "data.pkl"), "wb") as f:
            pickle.dump((self.chunks, self.embeddings, self.metadatas, self.ids), f)

    def _load(self):
        path = os.path.join(self.persist_dir, "data.pkl")
        if os.path.exists(path):
            with open(path, "rb") as f:
                self.chunks, self.embeddings, self.metadatas, self.ids = pickle.load(f)

    def indexer_document(self, texte, metadatas):
        chunks = [texte[i:i+5000] for i in range(0, len(texte), 5000)]
        if not chunks:
            return 0
        if isinstance(metadatas, dict):
            metadatas = [metadatas] * len(chunks)
        elif len(metadatas) == 1 and len(metadatas) < len(chunks):
            metadatas = metadatas * len(chunks)
        new_ids = [str(uuid.uuid4()) for _ in chunks]
        new_embeddings = self.model.encode(chunks)
        self.chunks.extend(chunks)
        self.embeddings.extend(new_embeddings)
        self.metadatas.extend(metadatas)
        self.ids.extend(new_ids)
        self._save()
        return len(chunks)

    def rechercher(self, query, k=4):
        if not self.chunks:
            return []
        query_emb = self.model.encode([query])[0]
        norms = np.linalg.norm(self.embeddings, axis=1)
        query_norm = np.linalg.norm(query_emb)
        if query_norm == 0:
            return []
        scores = np.dot(self.embeddings, query_emb) / (norms * query_norm)
        best_indices = np.argsort(scores)[-k:][::-1]
        class Doc:
            def __init__(self, page_content, metadata):
                self.page_content = page_content
                self.metadata = metadata
        return [Doc(self.chunks[i], self.metadatas[i]) for i in best_indices]