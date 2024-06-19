import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

file_path = 'WC24_DATA.xlsx'
sheet_name = 'Sheet1'
data = pd.read_excel(file_path,sheet_name=sheet_name)

# Feature Engineering
data['venue'] = data['venue'].astype('category').cat.codes
data['batting_team'] = data['batting_team'].astype('category').cat.codes
data['bowling_team'] = data['bowling_team'].astype('category').cat.codes

# Create features and labels
X = data[['venue', 'batting_team', 'bowling_team', 'toss_result', 'first_innings']]
y = data['total_score']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)

# Evaluation metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f'MAE: {mae}')
print(f'MSE: {mse}')
print(f'RMSE: {rmse}')

# Example prediction
sample_data = np.array([[1, 2, 3, 1, 0]])  # Replace with actual sample data
predicted_score = model.predict(sample_data)
print(f'Predicted Score: {predicted_score[0]}')
