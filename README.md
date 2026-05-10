# 🚀 Analyse Financière & Extraction Documentaire IA

## 📌 Description du projet

Ce projet a pour objectif d’automatiser l’extraction et l’analyse de documents financiers grâce à l’intelligence artificielle et au traitement automatique de documents.

La solution permet de :

* Extraire automatiquement du texte depuis des PDF, images et documents Word
* Gérer les documents scannés grâce à l’OCR
* Détecter et structurer des tableaux
* Préparer les données pour des applications IA et NLP
* Construire une base pour un assistant conversationnel sur documents financiers

---

# 🎯 Problématique

Dans de nombreuses entreprises, les équipes financières et administratives passent un temps considérable à lire et analyser manuellement des documents :

* Factures
* Rapports financiers
* Contrats
* Documents comptables
* PDF scannés

L’objectif de ce projet est d’automatiser cette étape afin de :

✅ réduire le temps de traitement

✅ limiter les erreurs humaines

✅ améliorer la productivité

✅ préparer les données pour l’analyse IA

---

# ⚙️ Fonctionnalités

## ✅ Extraction multi-format

Le pipeline prend en charge :

* PDF
* DOCX
* Images (PNG, JPG, JPEG, TIFF)

---

## ✅ OCR automatique

Les documents scannés sont traités grâce à Tesseract OCR.

---

## ✅ Extraction de tableaux

Les tableaux présents dans les documents sont automatiquement détectés et convertis en DataFrame Pandas.

---

## ✅ Pipeline intelligent

Architecture actuelle :

```text
Documents → Extraction → OCR → Structuration → IA
```

---

# 🛠️ Stack Technique

| Technologie   | Utilisation                            |
| ------------- | -------------------------------------- |
| Python        | Développement principal                |
| pdfplumber    | Extraction de texte PDF                |
| Tesseract OCR | OCR pour documents scannés             |
| pdf2image     | Conversion PDF → images                |
| Pillow        | Traitement d’images                    |
| Pandas        | Structuration des données              |
| python-docx   | Lecture de documents Word              |
| Streamlit     | Interface utilisateur (future version) |
| Transformers  | NLP & IA générative                    |
| ChromaDB      | Recherche vectorielle                  |


---

# 🚀 Installation

## 1. Cloner le projet

```bash
git clone <URL_DU_REPO>
cd analyse_financiere
```

---

## 2. Créer un environnement virtuel

```bash
python -m venv venv
```

---

## 3. Activer l’environnement virtuel

### Windows

```bash
venv\Scripts\activate
```

---

## 4. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

# 🔥 Dépendances système

## Tesseract OCR

Installer Tesseract OCR :

[https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)

---

## Poppler

Installer Poppler pour Windows :

[https://github.com/oschwartz10612/poppler-windows/releases](https://github.com/oschwartz10612/poppler-windows/releases)

---

# ▶️ Exemple d’utilisation


```python
from extracteur_documents import ExtracteurDocuments

# chemin du fichier à analyser
fichier = r"C:\Users\Valencia\Downloads\rapport-annuel.pdf"

# extraction du texte et des tableaux
texte, tables = ExtracteurDocuments.detect_and_extract(fichier)

# affichage du texte
print(texte[:1000])

# nombre de tableaux détectés
print("Nombre de tables :", len(tables))
```

---

# 📊 Cas d’usage

Cette solution peut être utilisée pour :

* Analyse financière automatisée
* Lecture automatique de factures
* Recherche documentaire intelligente
* Analyse de contrats
* Préparation de données pour IA
* Construction d’assistants conversationnels métiers

---

# 🚀 Roadmap

## Prochaines améliorations

* Interface utilisateur avec Streamlit
* Résumé automatique de documents
* Recherche sémantique
* Assistant IA sur documents financiers
* Pipeline RAG
* Déploiement Cloud

---

# 💡 Démonstration

Une vidéo de démonstration du projet sera prochainement disponible.

---

# 👩‍💻 Auteur

Darie-Valencia MABIALA-NZAMBILANOU

 Data & IA Enthusiast

📌 Spécialités :

* Data Analytics
* Machine Learning
* NLP
* IA Générative
* Automatisation documentaire

---

# ⭐ Objectif du projet

Ce projet a été développé dans une logique de montée en compétence sur les architectures IA documentaires et les pipelines d’automatisation intelligents.

L’objectif final est de construire une solution capable d’interagir intelligemment avec des documents métiers.
