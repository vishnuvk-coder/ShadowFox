# Car Selling Price Prediction

This project is a **Machine Learning Model** that predicts the **approximate selling price of a car** based on different features such as fuel type, years of service, showroom price, previous owners, kilometers driven, seller type, and transmission type.

## Project Objective

The goal of this project is to build an ML model that helps users estimate the selling price of a used car.

## Dataset Features

The model uses the following features:

- Car Name
- Year
- Selling Price
- Present Price
- Kilometers Driven
- Fuel Type
- Seller Type
- Transmission Type
- Number of Previous Owners

## Dataset Structure

```text
Car_Price_Prediction/
│
├── car data.csv
├── train.py
├── predict.py
├── requirements.txt
├── screenshots/
└── README.md
```

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Joblib

## Machine Learning Algorithm

This project uses:

```text
Random Forest Regressor
```

for car price prediction.

## Features

- Car Selling Price Prediction
- Data Preprocessing
- Machine Learning Model Training
- Model Evaluation
- Price Prediction System

## How to Run

### Install Required Libraries

```bash
pip install pandas numpy matplotlib scikit-learn joblib
```

### Train the Model

```bash
python train.py
```

### Run Prediction

```bash
python predict.py
```

## Example Prediction

Example output:

```text
Predicted Selling Price: ₹4.52 Lakhs
```

## Output

The system predicts the approximate selling price of a car based on user inputs.
