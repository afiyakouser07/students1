import streamlit as st

from utils.data_loader import load_data

st.title("📈 Business Insights")

df = load_data()

correlation = (
    df.corr(numeric_only=True)["exam_score"]
    .sort_values(ascending=False)
)

st.subheader("Factors Affecting Exam Score")

st.dataframe(correlation)

st.markdown("""
### Key Insights

✅ Previous Score strongly affects Exam Score

✅ More Study Hours improve performance

✅ Better Attendance increases scores

✅ Completing Assignments boosts marks

✅ Excessive Internet Usage impacts performance

✅ Students with higher scores are more likely to get placed
""")
