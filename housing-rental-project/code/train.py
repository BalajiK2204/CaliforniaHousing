import mlflow
import mlflow.sklearn
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd

data = fetch_california_housing(as_frame=True)
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

with mlflow.start_run():
    model = LinearRegression()
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    mlflow.log_metric("r2_score", score)
    mlflow.sklearn.log_model(model, artifact_path="model")  # Use artifact_path, not name
    print("Model trained and logged with MLflow.")