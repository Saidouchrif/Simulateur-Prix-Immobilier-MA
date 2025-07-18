
# Simulateur d’Évaluation Immobilière - SalesHouses

## Objectif
Ce projet vise à prédire le **prix de vente d’un bien immobilier au Maroc** (appartement, maison, etc.) à partir de ses caractéristiques (surface, nombre de pièces, localisation, etc.) grâce à des algorithmes de **machine learning**.

---

## Structure du projet

| Fichier / Dossier        | Description                                         |
|--------------------------|-----------------------------------------------------|
| `Lire_data.ipynb`        | Notebook Jupyter principal d'entraînement du modèle |
| `model.pkl`              | Modèle pré-entraîné enregistré avec joblib/pickle   |
| `api_prediction.py` *(optionnel)*   | API Flask pour exposer la prédiction en ligne       |
| `README.txt`             | Liste des dépendances à installer                   |
| `data/` *(optionnel)*    | Contient le fichier CSV source des données         |

---

## Installation

1. **Cloner le projet** (ou télécharger le dossier) :
   ```bash
   git clone https://github.com/Saidouchrif/Application-AI-brief2.git
   cd Application-Ai-brief2
   ```

2. **Créer un environnement virtuel (optionnel mais recommandé)** :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Installer les dépendances** :
   ```bash
   pip install -r README.txt
   ```

---

## Exécution (entraînement du modèle)

1. **Ouvrir et exécuter le notebook** :
   ```bash
   jupyter notebook Lire_data.ipynb
   ```

2. **Ou exécuter le script Python** :
   ```bash
   python test_model.py
   ```

---

## API Flask (optionnelle)

### Lancer l’API :
```bash
python api_prediction.py
```

### Exemple de requête POST :
```
URL : http://localhost:5000/predict
Méthode : POST
Header : Content-Type: application/json
Corps JSON :
{
  "features": {
    "salon": 1,
    "nb_rooms": 2,
    "nb_baths": 2,
    "surface_area": 90,
    "price_per_m2": 50,
    "total_rooms": 1,
    "rooms_baths_ratio": 1.5,
    "city_name": "Mohammedia"
  }
}

```

### Réponse attendue :
```json
{
  "predicted_price": 1350000
}
```

---

## Algorithmes utilisés

- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor
- Support Vector Regression (SVR)
- XGBoost
- LightGBM (modèle principal optimisé)

---

##  À venir (idées d'amélioration)
- Interface web (Streamlit ou Flask Frontend)
- Ajout de données géographiques (distance au centre-ville)
- Analyse des quartiers et zones populaires
- Hébergement de l’API sur Render ou Heroku

---

## Auteur

Projet réalisé par **[Said ouchrif]**, développeur passionné par la data science et l'immobilier.
