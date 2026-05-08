# classifieur.py
from transformers import pipeline

class ClassifieurDocuments:
    def __init__(self):
        self.classifier = pipeline("zero-shot-classification", 
                                   model="facebook/bart-large-mnli")
        self.categories = [
            "facture", "relevé bancaire", "contrat financier",
            "rapport annuel", "bilan comptable", "devis", "note de frais"
        ]

    def predire(self, texte):
        result = self.classifier(texte[:3000], self.categories)
        return result['labels'][0], result['scores'][0]