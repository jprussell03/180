import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Step 1: Read the data
file_path = r'C:\Users\lakec\Downloads\baseball.xlsx'
data = pd.read_excel(file_path)

# Step 2: Prepare the data
features = ['Runs Scored', 'Runs Allowed', 'Wins', 'OBP', 'SLG', 'Team Batting Average']
X = data[features]
y = data['Playoffs']

# Step 3: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train a classification model
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 5: Evaluate the model's performance
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy of the model:", accuracy)

# Step 6: Use the trained model to make predictions for the team MIL
team_MIL = [[750, 600, 90, 0.350, 0.450, 0.270]]  # Example values for the team MIL
prediction = model.predict(team_MIL)

# Step 7: Print the prediction
if prediction[0] == 1:
    print("The team MIL will make it to the playoffs.")
else:
    print("The team MIL will not make it to the playoffs.")
print("baseball stats")