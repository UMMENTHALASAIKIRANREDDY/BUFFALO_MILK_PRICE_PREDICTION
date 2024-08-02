import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Load the Dataset
file_path = r'C:\Users\LENOVO\Desktop\mini_project\website\BM Rate.csv'
data = pd.read_csv(file_path)

# Data Preprocessing
data = data[['RateDate', 'SNF', 'FAT', 'Rate']]
data['RateDate'] = pd.to_datetime(data['RateDate'], errors='coerce')

# Calculate the number of days since a reference date
reference_date = pd.Timestamp('2000-01-01')
data['DaysSinceRefDate'] = (data['RateDate'] - reference_date).dt.days

# Separate features and target variable
X = data[['DaysSinceRefDate', 'SNF', 'FAT']]
y = data['Rate']
# Split the Data into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
from sklearn.ensemble import RandomForestRegressor

# Initialize the RandomForestRegressor
rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42, oob_score=True)

# Train the Model
rf_regressor.fit(X_train, y_train)
from sklearn.metrics import mean_squared_error, r2_score

# Make Predictions on the Test Set
y_pred = rf_regressor.predict(X_test)

# Evaluate the Model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
oob_score = rf_regressor.oob_score_

# Print key metrics including OOB score
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')
print(f'Out-of-Bag (OOB) Score: {oob_score:.4f}')
import joblib

# Save the trained model
joblib.dump(rf_regressor, 'rf_regressor_model.pkl')
