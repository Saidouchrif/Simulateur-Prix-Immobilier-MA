import joblib
import numpy as np
import pandas as pd

# Charger le modèle entraîné
model = joblib.load(r'C:\Users\saido\Pycharm\Simplon\Brief 1\model.pkl')

# Récupérer la liste des colonnes utilisées à l'entraînement
if hasattr(model, 'feature_names_in_'):
    feature_names = list(model.feature_names_in_)
else:
    # Pour les pipelines ou modèles sans cet attribut, charger X d'entraînement sauvegardé ou le lister manuellement
    raise ValueError("Impossible de retrouver les noms de colonnes d'entraînement automatiquement.")

# Exemple d'entrée à tester (adapter les valeurs selon votre cas)
example = {
    'salon': 1,
    'nb_rooms': 4,
    'nb_baths': 2,
    'surface_area': 500,
    'price_per_m2': 40,
    'total_rooms': 2,
    'rooms_baths_ratio': 1.5,
    # Ajoutez ici la ville, par exemple Casablanca
    'city_Casablanca': 2,
    # Les autres villes seront mises à 0 automatiquement
}

# Créer un vecteur d'entrée complet avec toutes les colonnes attendues
row = {col: 0 for col in feature_names}
row.update(example)
X_new = pd.DataFrame([row], columns=feature_names)

# Prédire
pred = model.predict(X_new)[0]
print(f'Prix prédit : {pred:.2f}')

# ---
# Pour tester :
# 1. Modifie le dictionnaire `example` pour la ville et les valeurs souhaitées.
# 2. Exécute :  
#    ```bash
#    python test_model.py
#    ```
# 3. Le script gère automatiquement toutes les colonnes attendues par le modèle.
# --- 