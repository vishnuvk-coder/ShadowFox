import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import joblib

# Load dataset
df = pd.read_csv("car data.csv")

# Create new feature
df['Car_Age'] = 2026 - df['Year']

# Drop unnecessary columns
df.drop(['Car_Name', 'Year'], axis=1, inplace=True)

# Convert categorical columns
df = pd.get_dummies(df, drop_first=True)

# Split features and target
X = df.drop('Selling_Price', axis=1)
y = df['Selling_Price']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

# Accuracy
score = r2_score(y_test, predictions)

print(f"Model Accuracy: {score * 100:.2f}%")

# Save model
joblib.dump(model, "car_price_model.pkl")

print("Model saved successfully!")