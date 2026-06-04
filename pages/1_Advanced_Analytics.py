import streamlit as st
from utils.data_loader import load_data
from utils.charts import *

st.title("📊 Advanced Analytics")

df = load_data()

st.plotly_chart(
    study_vs_score(df),
    use_container_width=True
)

st.plotly_chart(
    attendance_vs_score(df),
    use_container_width=True
)

st.plotly_chart(
    sleep_vs_score(df),
    use_container_width=True
)

st.plotly_chart(
    previous_vs_score(df),
    use_container_width=True
)
