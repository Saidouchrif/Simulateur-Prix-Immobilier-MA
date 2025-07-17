Simulateur d’évaluation immobilière - SalesHouses

## Description
Ce projet prédit le prix de vente d’un appartement au Maroc à partir de caractéristiques clés.

## Structure des fichiers
- simulateur_immobilier.py : Script principal
- model.pkl : Modèle entraîné
- [votre fichier CSV] : Données sources

## Instructions
1. Installer les dépendances : `pip install -r requirements.txt`
2. Lancer le script : `python simulateur_immobilier.py`
3. (Optionnel) Lancer l’API Flask pour la prédiction

## Utilisation de l’API
- Endpoint : POST /predict
- Body JSON : {"feature1": valeur, "feature2": valeur, ...}
- Réponse : {"predicted_price": valeur}