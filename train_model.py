import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import joblib

df = pd.read_csv("nepal_house_data.csv")

X = df.drop("total_price", axis=1)
y = df["total_price"]

cat_features = ["location"]
num_features = [col for col in X.columns if col not in cat_features]

preprocess = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown="ignore"), cat_features)
], remainder="passthrough")

model = Pipeline([
    ("prep", preprocess),
    ("rf", RandomForestRegressor(
        n_estimators=250,
        max_depth=20,
        random_state=42
    ))
])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model.fit(X_train, y_train)

preds = model.predict(X_test)
print("R2 Score:", r2_score(y_test, preds))

joblib.dump(model, "nepal_house_price_model.pkl")
print("✅ Model saved")
