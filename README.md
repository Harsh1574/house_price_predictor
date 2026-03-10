# 🏠 California House Price Predictor

> An end-to-end Machine Learning web application that predicts California house prices using the **California Housing Dataset**, powered by **XGBoost** and deployed with a **Flask** backend.

---

## 🚀 Live Demo

> _Deployment link coming soon_

---

## 📌 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Dataset](#dataset)
- [Model Performance](#model-performance)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [How It Works](#how-it-works)
- [Planned Enhancements](#planned-enhancements)
- [Contributing](#contributing)

---

## 🧠 Overview

This project tackles a classic **regression problem** — predicting median house prices across California districts. Given block-level demographic and geographic features, the model estimates a property's value using the **XGBoost Regressor**, one of the most powerful gradient-boosting frameworks available.

The project includes a polished **Flask web app** where users can input housing features and instantly receive a price estimate, along with a built-in **Loan Calculator** that auto-computes EMI, down payment, and loan amount based on the predicted price.

---

## ✨ Features

- 🤖 **XGBoost Regression Model** trained on the California Housing Dataset
- 🌐 **Flask Web App** with a clean, responsive UI
- 🌙 **Dark / Light Mode Toggle** for better accessibility
- 💰 **Integrated Loan Calculator** — auto-populates with the predicted price and allows users to adjust interest rate, down payment percentage, and tenure
- 🔁 **Form Persistence** — input values are retained after prediction for easy comparison
- 📦 **Serialized Model** via `joblib` for fast inference

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.x |
| ML Framework | XGBoost, scikit-learn |
| Web Framework | Flask |
| Data Handling | Pandas, NumPy |
| Model Serialization | Joblib |
| Frontend | HTML5, CSS3, JavaScript |
| Fonts | Google Fonts (Poppins) |

---

## 📊 Dataset

**Source:** California Housing Dataset (derived from the 1990 U.S. Census)

| Feature | Description |
|---|---|
| `MedInc` | Median income of households in the block (in tens of thousands of USD) |
| `HouseAge` | Median age of houses in the block (years) |
| `AveRooms` | Average number of rooms per household |
| `AveBedrms` | Average number of bedrooms per household |
| `Population` | Total population of the block |
| `AveOccup` | Average number of occupants per household |
| `Latitude` | Latitude coordinate of the block |
| `Longitude` | Longitude coordinate of the block |
| `MedHouseVal` ⭐ | **Target** — Median house value (in hundreds of thousands of USD) |

> **Note:** The target variable is expressed in units of $100,000. The web app automatically converts predictions to full USD for display.

---

## 📈 Model Performance

| Metric | Train | Test |
|---|---|---|
| **R² Score** | ~0.94 | ~0.83 |
| **MAE** | ~0.10 | ~0.19 |

> _Exact values will vary based on environment and XGBoost version. Run `train_model.py` to reproduce._

The model achieves strong generalization on unseen data. The gap between train and test R² is a known characteristic of XGBoost on this dataset and will be addressed through hyperparameter tuning in upcoming iterations.

---

## 📁 Project Structure

```
House Price Predictor/
│
├── dataset/
│   └── house_prices.csv          # California Housing Dataset
│
├── templates/
│   └── index.html                # Frontend — prediction form + loan calculator
│
├── static/
│   └── style.css                 # Styling with dark/light mode support
│
├── train_model.py                # Data prep, model training & evaluation
├── application.py                # Flask app — routes and prediction logic
├── house_price_model.pkl         # Serialized trained XGBoost model
├── requirements.txt              # Python dependencies
└── README.md
```

---

## ⚙️ Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/house-price-predictor.git
cd house-price-predictor

# 2. Install dependencies
pip install -r requirements.txt

# 3. Train the model (generates house_price_model.pkl)
python train_model.py

# 4. Start the Flask server
python application.py
```

Then open your browser and navigate to `http://127.0.0.1:5000`.

### Requirements

```
flask
numpy
pandas
scikit-learn
xgboost
joblib
```

---

## ⚙️ How It Works

```
User Input (8 features)
        ↓
Flask POST /predict
        ↓
Load house_price_model.pkl
        ↓
XGBRegressor.predict()
        ↓
Convert output (×$100,000)
        ↓
Display Estimated Price + Loan Calculator
```

1. The user fills in 8 housing features on the web form.
2. On submission, Flask collects and preprocesses the input.
3. The pre-trained XGBoost model predicts the median house value.
4. The result is scaled to full USD and displayed.
5. The integrated loan calculator auto-fills with the predicted price for instant financial planning.

---

## 🔮 Planned Enhancements

This project is actively being developed. Here's what's coming next:

### 🔬 Model & ML
- [ ] **Algorithm Benchmarking** — Compare XGBoost against Random Forest, Linear Regression, Ridge, Lasso, SVR, and LightGBM to empirically identify the best model
- [ ] **Hyperparameter Tuning** — Use GridSearchCV / RandomizedSearchCV / Optuna to optimize XGBoost parameters (`n_estimators`, `max_depth`, `learning_rate`, etc.)
- [ ] **Cross-Validation** — Replace single train/test split with K-Fold cross-validation for more robust evaluation
- [ ] **Feature Engineering** — Derive new features such as `rooms_per_person`, `bedrooms_per_room`, and `income_per_room`
- [ ] **Feature Importance Visualization** — Plot SHAP values or XGBoost feature importances to explain model decisions
- [ ] **Outlier Detection & Removal** — Analyze the effect of removing outliers (e.g., houses capped at $500,001) on model accuracy
- [ ] **Geospatial Analysis** — Map predictions by latitude/longitude to surface geographic pricing patterns

### 🌐 Web App
- [ ] **Interactive Price Map** — Visualize predicted prices on a California map using Folium or Leaflet.js
- [ ] **Prediction History** — Let users compare multiple predictions side-by-side in a session
- [ ] **Confidence Intervals** — Display a price range instead of a single point estimate
- [ ] **Input Validation & Tooltips** — Add contextual guidance for each input field

### 🚀 Deployment
- [ ] **Cloud Deployment** — Host on AWS Elastic Beanstalk, Render, or Heroku
- [ ] **Dockerize** — Package the application in a Docker container for consistent deployment
- [ ] **REST API** — Expose a `/api/predict` endpoint for programmatic access

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m 'Add my feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---



> ⭐ If you found this project useful, consider giving it a star on GitHub!
