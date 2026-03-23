import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# correct data (use lists)
data = {
    "experience": [1, 2, 3, 4, 5],
    "salary": [20000, 30000, 50000, 70000, 90000]
}

df = pd.DataFrame(data)

# features and target
x = df[['experience']]
y = df['salary']

# model
model = LinearRegression()
model.fit(x, y)

# save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model Trained and saved!")

