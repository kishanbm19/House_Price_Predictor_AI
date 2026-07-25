# 🏠 House Price Predictor

A Machine Learning project that predicts the estimated price of a house based on key property features such as house size, number of bedrooms, bathrooms, parking spaces, and house age. The project demonstrates the complete machine learning workflow, including data preprocessing, model training, evaluation, and prediction using Scikit-learn.

---

## 📌 Features

* Predicts house prices using Machine Learning.
* Performs data preprocessing before training.
* Trains a Linear Regression model using Scikit-learn.
* Evaluates model performance using R² Score and Mean Squared Error (MSE).
* Saves the trained model using Joblib.
* Supports house price prediction through a command-line interface.

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Git & GitHub

---

## 📂 Project Structure

```text
House-Price-Predictor/
│
├── Dataset/
│   └── house_price_dataset.csv
│
├── models/
│   └── house_price_model.pkl
│
├── train.py
├── predict.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Dataset

The dataset includes the following features:

* House Size (sqft)
* Number of Bedrooms
* Number of Bathrooms
* Number of Parking Lots
* House Age
* House Price (Target)

These features are used to train a regression model for predicting house prices.

---

## 🤖 Machine Learning Model

The project uses **Linear Regression** to estimate house prices based on the provided property features.

The trained model is saved as:

```text
models/house_price_model.pkl
```

---

## 📈 Model Evaluation

The model is evaluated using:

* R² Score
* Mean Squared Error (MSE)

These metrics help measure the prediction accuracy of the regression model.

---

## ▶️ Training the Model

Run the following command:

```bash
python train.py
```

The trained model is automatically saved inside the `models/` directory.

---

## 🔮 Making Predictions

Run:

```bash
python predict.py
```

Example Input:

```text
Enter House size(sqft): 1200
Enter the number of bedrooms: 2
Enter the number of bathrooms: 2
Enter the number of available parking lots: 1
Enter the House age: 10
```

Example Output:

```text
Estimated House Price:
₹54,43,548.39
```

---

## 🚀 Future Improvements

* Train the model on a larger real-world housing dataset.
* Include additional features such as location, furnishing status, nearby amenities, and property type.
* Compare multiple regression algorithms for improved accuracy.
* Develop a web interface using Flask or Django.
* Deploy the trained model as a web application.

---

## 📦 Requirements

```text
pandas
numpy
scikit-learn
joblib
```
