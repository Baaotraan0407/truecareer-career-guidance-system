import pandas as pd


DATA_PATH = "data/truecareer_clustered_output.csv"


def load_clustered_data(path=DATA_PATH):
    """Load clustered TrueCareer dataset."""
    df = pd.read_csv(path)
    return df


def show_recommendation_summary(df):
    """Show recommendation output distribution."""
    print("Recommended major distribution:")
    print(df["recommended_major"].value_counts())

    print("\nRecommended mentor type distribution:")
    print(df["recommended_mentor_type"].value_counts())

    print("\nRecommended career path examples:")
    print(df[["student_id", "student_cluster", "kmeans_cluster_id", "recommended_major", "recommended_career_path"]].head(10))


if __name__ == "__main__":
    dataset = load_clustered_data()
    show_recommendation_summary(dataset)