import joblib
import pandas as pd

# Load model
model = joblib.load("car_price_model.pkl")

# Example car details
data = {
    'Present_Price': [5.59],
    'Kms_Driven': [27000],
    'Owner': [0],
    'Car_Age': [5],
    'Fuel_Type_Diesel': [0],
    'Fuel_Type_Petrol': [1],
    'Seller_Type_Individual': [0],
    'Transmission_Manual': [1]
}

df = pd.DataFrame(data)

# Predict price
prediction = model.predict(df)

print(f"Predicted Selling Price: ₹{prediction[0]:.2f} Lakhs")