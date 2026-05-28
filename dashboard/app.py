import pandas as pd
import streamlit as st
import plotly.express as px


DATA_PATH = "data/truecareer_clustered_output.csv"


st.set_page_config(
    page_title="TrueCareer Dashboard",
    page_icon="🎓",
    layout="wide"
)


@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)
    return df


df = load_data()

st.title("🎓 TrueCareer Dashboard")
st.write("Assessment-driven career guidance and course recommendation prototype for Vietnamese high school students.")

st.info(
    "This dashboard uses a synthetic Vietnam-context dataset for prototype demonstration only. "
    "It does not represent real student records."
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Students", len(df))

with col2:
    st.metric("Dataset Version", df["generated_version"].iloc[0])

with col3:
    st.metric("Number of Clusters", df["kmeans_cluster_id"].nunique())


st.subheader("Student Cluster Distribution")
cluster_counts = df["kmeans_cluster_id"].value_counts().reset_index()
cluster_counts.columns = ["Cluster ID", "Number of Students"]
fig_cluster = px.bar(
    cluster_counts,
    x="Cluster ID",
    y="Number of Students",
    title="K-Means Cluster Distribution"
)
st.plotly_chart(fig_cluster, use_container_width=True)


st.subheader("Recommended Major Distribution")
major_counts = df["recommended_major"].value_counts().reset_index()
major_counts.columns = ["Recommended Major", "Number of Students"]
fig_major = px.bar(
    major_counts,
    x="Recommended Major",
    y="Number of Students",
    title="Recommended Major Distribution"
)
st.plotly_chart(fig_major, use_container_width=True)


st.subheader("Filter Student Profiles")

admission_options = ["All"] + sorted(df["admission_subject_group"].unique().tolist())
selected_admission = st.selectbox("Admission Subject Group", admission_options)

orientation_options = ["All"] + sorted(df["high_school_subject_orientation"].unique().tolist())
selected_orientation = st.selectbox("High School Subject Orientation", orientation_options)

filtered_df = df.copy()

if selected_admission != "All":
    filtered_df = filtered_df[filtered_df["admission_subject_group"] == selected_admission]

if selected_orientation != "All":
    filtered_df = filtered_df[filtered_df["high_school_subject_orientation"] == selected_orientation]

st.write("Filtered records:", len(filtered_df))

st.dataframe(
    filtered_df[
        [
            "student_id",
            "gpa_band",
            "admission_subject_group",
            "high_school_subject_orientation",
            "student_cluster",
            "kmeans_cluster_id",
            "recommended_major",
            "recommended_mentor_type",
            "recommended_career_path",
        ]
    ],
    use_container_width=True
)