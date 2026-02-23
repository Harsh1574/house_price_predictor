import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error
import joblib
import os

# Set paths
base_dir = r"e:\Machine Learning\House Price Predictor"
dataset_path = os.path.join(base_dir, "dataset", "house_prices.csv")
model_path = os.path.join(base_dir, "house_price_model.pkl")

print(f"Loading dataset from: {dataset_path}")

# Load the dataset
try:
    data = pd.read_csv(dataset_path)
except FileNotFoundError:
    print(f"Error: Dataset not found at {dataset_path}")
    exit(1)

# Prepare data
# Features: MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude
X = data.drop(columns='MedHouseVal', axis=1)
Y = data['MedHouseVal']

print("Dataset loaded successfully.")
print(f"Features: {list(X.columns)}")

# Split data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

# Initialize and train model
print("Training XGBRegressor model...")
model = xgb.XGBRegressor()
model.fit(X_train, Y_train)

# Evaluate
print("Evaluating model...")
train_preds = model.predict(X_train)
test_preds = model.predict(X_test)

train_r2 = r2_score(Y_train, train_preds)
test_r2 = r2_score(Y_test, test_preds)
train_mae = mean_absolute_error(Y_train, train_preds)
test_mae = mean_absolute_error(Y_test, test_preds)

print(f"Train R2 Score: {train_r2:.4f}")
print(f"Test R2 Score: {test_r2:.4f}")
print(f"Train MAE: {train_mae:.4f}")
print(f"Test MAE: {test_mae:.4f}")

# Save model
print(f"Saving model to {model_path}...")
joblib.dump(model, model_path)
print("Model saved successfully.")
