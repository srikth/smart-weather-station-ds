import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Load dataset
df = pd.read_csv("weather.csv")

# Explore
print(df.head())
print(df.describe())

# Clean data
df = df.dropna()
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

# Visualization
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Temperature'], label='Temperature (°C)')
plt.title("Daily Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.show()

# Correlation
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()

# Predict next-day temperature using Random Forest
features = ['Humidity', 'Pressure', 'WindSpeed', 'Rainfall']
target = 'Temperature'

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
rmse = mean_squared_error(y_test, y_pred, squared=False)
print(f"RMSE: {rmse:.2f} °C")

# Feature importance
imp = pd.Series(model.feature_importances_, index=features)
imp.plot(kind='barh', title='Feature Importance')
plt.show()
