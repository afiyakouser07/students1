import plotly.express as px


def score_distribution(df):
    return px.histogram(
        df,
        x="exam_score",
        nbins=30,
        title="Exam Score Distribution"
    )


def placement_distribution(df):
    return px.pie(
        df,
        names="placement_status",
        title="Placement Distribution"
    )


def study_vs_score(df):
    return px.scatter(
        df,
        x="study_hours",
        y="exam_score",
        color="placement_status",
        title="Study Hours vs Exam Score"
    )


def attendance_vs_score(df):
    return px.scatter(
        df,
        x="attendance",
        y="exam_score",
        color="placement_status",
        title="Attendance vs Exam Score"
    )


def sleep_vs_score(df):
    return px.scatter(
        df,
        x="sleep_hours",
        y="exam_score",
        color="placement_status",
        title="Sleep Hours vs Exam Score"
    )


def internet_vs_score(df):
    return px.scatter(
        df,
        x="internet_usage",
        y="exam_score",
        color="placement_status",
        title="Internet Usage vs Exam Score"
    )


def previous_vs_score(df):
    return px.scatter(
        df,
        x="previous_score",
        y="exam_score",
        color="placement_status",
        title="Previous Score vs Exam Score"
    )


def assignment_vs_score(df):
    return px.box(
        df,
        x="assignments_completed",
        y="exam_score",
        title="Assignments Completed vs Exam Score"
    )
