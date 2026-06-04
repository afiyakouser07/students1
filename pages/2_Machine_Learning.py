import streamlit as st
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from utils.data_loader import load_data

st.title("🤖 Placement Prediction")

df = load_data()

encoder = LabelEncoder()

df["placement_status"] = encoder.fit_transform(
    df["placement_status"]
)

X = df.drop(
    "placement_status",
    axis=1
)

y = df["placement_status"]

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier()

model.fit(
    X_train,
    y_train
)

accuracy = model.score(
    X_test,
    y_test
)

st.success(
    f"Model Accuracy: {accuracy*100:.2f}%"
)

st.subheader("Feature Importance")

importance = pd.DataFrame({
    "Feature":X.columns,
    "Importance":model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

st.bar_chart(
    importance.set_index("Feature")
)
