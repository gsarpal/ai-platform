from pathlib import Path
import pickle

from sklearn.linear_model import LogisticRegression


# Simple training data:
# [age, monthly_spend]
X = [
    [25, 1000],
    [30, 1500],
    [35, 2000],
    [40, 4000],
    [45, 5000],
    [50, 6000],
]

# 0 = no churn, 1 = churn
y = [0, 0, 0, 1, 1, 1]


model = LogisticRegression()
model.fit(X, y)


model_path = Path("models/churn_v1.pkl")
model_path.parent.mkdir(parents=True, exist_ok=True)

with open(model_path, "wb") as file:
    pickle.dump(model, file)

print(f"Model created: {model_path}")