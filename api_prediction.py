from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

# Charger le modèle
model = joblib.load(r'C:\Users\saido\Pycharm\Simplon\Brief 1\model.pkl')

# Charger les noms des colonnes utilisées à l'entraînement
if hasattr(model, 'feature_names_in_'):
    feature_names = list(model.feature_names_in_)
else:
    raise ValueError("Impossible de retrouver les noms de colonnes d'entraînement automatiquement.")

# Initialiser Flask
app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        features = data["features"]  # dict contenant toutes les infos comme "city_name", "salon", etc.

        # Créer un vecteur d'entrée avec 0 par défaut
        input_data = {col: 0 for col in feature_names}

        # Remplir les valeurs numériques
        for key in features:
            if key in input_data:
                input_data[key] = features[key]

        # Gérer la colonne encodée de la ville, exemple : city_name="Casablanca" => "city_Casablanca"=1
        city = features.get("city_name")
        if city:
            city_col = f"city_{city}"
            if city_col in input_data:
                input_data[city_col] = 1

        # Créer un DataFrame
        X_input = pd.DataFrame([input_data], columns=feature_names)

        # Prédiction
        prediction = model.predict(X_input)[0]

        return jsonify({"prediction": round(prediction, 2)})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
