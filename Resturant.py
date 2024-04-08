import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Step 1: Read the data
file_path = r'C:\Users\russelljp03\Downloads\Restaurant Revenue.xlsx'
data = pd.read_excel(file_path)

# Step 2: Prepare the data
features = ['Number_of_Customers', 'Menu_Price', 'Marketing_Spend', 
            'Average_Customer_Spending', 'Promotions', 'Reviews']
X = data[features]
y = data['Monthly_Revenue']

# Step 3: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train a regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Evaluate the model's performance
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Step 6: Use the trained model to make predictions
# Here, you can input new data to predict the monthly revenue
# For example, you can create a dictionary with new values for the features
new_data = {
    'Number_of_Customers': [100],
    'Menu_Price': [25],
    'Marketing_Spend': [500],
    'Average_Customer_Spending': [20],
    'Promotions': [1],
    'Reviews': [50]
}
new_df = pd.DataFrame(new_data)
predicted_revenue = model.predict(new_df)

# Step 7: Print or display the predicted monthly revenue
print("Predicted Monthly Revenue:", predicted_revenue)
print("Yay Money!!")