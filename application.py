from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)
application = app  # For compatibility with some hosting platforms

# Load the model
base_dir = r"e:\Machine Learning\House Price Predictor"
model_path = os.path.join(base_dir, "house_price_model.pkl")

print(f"Loading model from: {model_path}")
try:
    model = joblib.load(model_path)
    print("Model loaded successfully.")
except Exception as e:
    # Provide clearer guidance when the model can't be unpickled due to missing packages
    if isinstance(e, FileNotFoundError):
        print(f"Error: Model not found at {model_path}. Please run train_model.py first.")
    elif isinstance(e, ModuleNotFoundError) or 'xgboost' in str(e).lower():
        print(f"Error loading model: {e}")
        print("It looks like a required package is missing (for example, 'xgboost').")
        print("Install it with: pip install xgboost")
    else:
        print(f"Error loading model: {e}")

    model = None

@application.route('/')
def home():
    return render_template('index.html')

@application.route('/predict', methods=['POST'])
def predict():
    if not model:
        return render_template('index.html', error="Model not loaded.")

    try:
        # Get values from form
        # Order: MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude
        features = [
            float(request.form['MedInc']),
            float(request.form['HouseAge']),
            float(request.form['AveRooms']),
            float(request.form['AveBedrms']),
            float(request.form['Population']),
            float(request.form['AveOccup']),
            float(request.form['Latitude']),
            float(request.form['Longitude'])
        ]
        
        # Convert to numpy array and reshape for prediction
        final_features = [np.array(features)]
        
        # Predict
        prediction = model.predict(final_features)
        
        # The target is in 100k units, so multiply by 100,000 for display
        # predicted_value = round(prediction[0] * 100000, 2)
        # Actually, let's keep it in the original units but labeled clearly, or convert.
        # The dataset target is "Median house value for California districts, expressed in hundreds of thousands of dollars ($100,000)."
        
        output = round(prediction[0], 3)
        formatted_price = f"${output * 100000:,.2f}"
        raw_price = output * 100000

        return render_template('index.html', prediction_text=f'Estimated House Price: {formatted_price}', prediction_value=raw_price, original_input=request.form)

    except Exception as e:
        return render_template('index.html', error=f"Error making prediction: {str(e)}")

if __name__ == "__main__":
    application.run(debug=True)
