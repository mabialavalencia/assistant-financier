from gliner import GLiNER
import re

class NERFinancier:
    def __init__(self):
        self.model = GLiNER.from_pretrained("urchade/gliner_multi")
        self.entites_financieres = [
            "montant_HT", "montant_TTC", "montant_TVA",
            "date_facture", "date_echeance",
            "numero_facture", "IBAN", "SIRET", "nom_entreprise"
        ]

    def extraire_gliner(self, texte):
        return self.model.predict_entities(texte, self.entites_financieres)

    @staticmethod
    def extraire_regex(texte):
        montant_ttc = re.findall(r'(\d+[\d\s]*[,.]?\d*)\s*€?\s*TTC', texte, re.IGNORECASE)
        iban = re.findall(r'FR\d{2}\s?\d{4}\s?\d{4}\s?\d{4}\s?\d{4}\s?\d{3}', texte)
        siret = re.findall(r'\d{3}\s?\d{3}\s?\d{3}\s?\d{5}', texte)
        return {
            "montants_TTC": montant_ttc,
            "IBANs": iban,
            "SIRETs": siret
        }

    def fusionner(self, texte):
        gliner_ent = self.extraire_gliner(texte)
        regex_ent = self.extraire_regex(texte)
        return {"gliner": gliner_ent, "regex": regex_ent}