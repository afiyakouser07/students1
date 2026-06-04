import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_data

st.set_page_config(
    page_title="Student Analytics Dashboard",
    page_icon="🎓",
    layout="wide"
)

df = load_data()

st.title("🎓 Student Performance Analytics")

st.markdown("### Deep Analytics Dashboard")

st.sidebar.header("Filters")

placement_filter = st.sidebar.multiselect(
    "Placement Status",
    options=df["placement_status"].unique(),
    default=df["placement_status"].unique()
)

df = df[df["placement_status"].isin(placement_filter)]

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Students",
    len(df)
)

col2.metric(
    "Avg Exam Score",
    round(df["exam_score"].mean(),2)
)

col3.metric(
    "Avg Attendance",
    round(df["attendance"].mean(),2)
)

col4.metric(
    "Placement Rate",
    f"{(df['placement_status'].eq('Placed').mean()*100):.1f}%"
)

st.divider()

left,right = st.columns(2)

with left:

    fig = px.histogram(
        df,
        x="exam_score",
        nbins=30,
        title="Exam Score Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    fig = px.pie(
        df,
        names="placement_status",
        title="Placement Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

corr = df.select_dtypes(
    include="number"
).corr()

fig = px.imshow(
    corr,
    text_auto=True,
    title="Correlation Heatmap"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
