import streamlit as st
import pandas as pd
import plotly.express as px
from analyzer import analyze_feedback

st.title("PreventativeScan Feedback Analysis Tool")

# -------------------------
# FILE UPLOAD
# -------------------------
uploaded_file = st.file_uploader("Upload Feedback CSV")

if uploaded_file:

    # -------------------------
    # LOAD DATA SAFELY
    # -------------------------
    df = pd.read_csv(uploaded_file, engine="python")

    # Fix malformed CSVs (single column issue)
    if df.shape[1] == 1:
        df = df.iloc[:, 0].astype(str).str.split(",", expand=True)

    # Ensure correct column count
    df = df.iloc[:, :5]

    df.columns = [
        "response_id",
        "nps_score",
        "feedback_text",
        "response_date",
        "member_location"
    ]

    df.columns = df.columns.str.strip()

    st.subheader("Raw Data Preview")
    st.dataframe(df.head())

    # -------------------------
    # RUN ANALYSIS BUTTON
    # -------------------------
    if st.button("Run Analysis"):

        st.write("Running analysis...")

        categories = []
        sentiments = []
        severities = []

        progress = st.progress(0)

        # -------------------------
        # LOOP THROUGH FEEDBACK
        # -------------------------
        for i, row in df.iterrows():

            text = row.get("feedback_text", "")

            if pd.isna(text):
                text = ""

            result = analyze_feedback(str(text))

            categories.append(result["category"])
            sentiments.append(result["sentiment"])

            # -------------------------
            # RULE-BASED SEVERITY
            # -------------------------
            try:
                score = float(row["nps_score"])
            except:
                score = 7

            if score <= 3:
                severity = "high"
            elif score <= 6:
                severity = "medium"
            else:
                severity = "low"

            severities.append(severity)

            progress.progress((i + 1) / len(df))

        # -------------------------
        # ADD RESULTS TO DATAFRAME
        # -------------------------
        df["category"] = categories
        df["sentiment"] = sentiments
        df["severity"] = severities

        st.success("Analysis complete")

        # -------------------------
        # TOP ISSUES
        # -------------------------
        st.subheader("Member Segments Affected")

        segment_summary = (
            df.groupby(["member_location", "category"])
            .size()
            .reset_index(name="count")
            .sort_values("count", ascending=False)
        )

        st.dataframe(segment_summary.head(10))
        st.subheader("Top Issues")

        issue_summary = (
            df.groupby("category")
            .size()
            .reset_index(name="count")
            .sort_values("count", ascending=False)
        )

        st.dataframe(issue_summary)

        fig = px.bar(
            issue_summary,
            x="category",
            y="count",
            title="Issue Frequency"
        )

        st.plotly_chart(fig)

        # -------------------------
        # ALERTS
        # -------------------------
        st.subheader("Alerts")

        negative_pct = len(df[df["sentiment"] == "negative"]) / len(df)
        high_severity_count = len(df[df["severity"] == "high"])

        if negative_pct > 0.05:
            st.error("🚨 Negative feedback exceeds 5% threshold")

        if high_severity_count > 10:
            st.error("🚨 High severity feedback spike detected")

        # -------------------------
        # KEY INSIGHT
        # -------------------------
        st.subheader("Key Insight")

        if len(issue_summary) > 0:
            top_issue = issue_summary.iloc[0]
            st.write(
                f"Top issue: **{top_issue['category']}** "
                f"({top_issue['count']} cases)"
            )

        # -------------------------
        # SAMPLE QUOTES
        # -------------------------
        st.subheader("Sample Feedback")

        for category in issue_summary["category"].head(5):

            st.markdown(f"### {category}")

            examples = df[df["category"] == category]["feedback_text"].head(2)

            for e in examples:
                st.write(f"- {e}")

        # -------------------------
        # DOWNLOAD OUTPUT
        # -------------------------
        csv = df.to_csv(index=False)

        st.download_button(
            "Download Analysis CSV",
            csv,
            "analysis_output.csv",
            "text/csv"
        )