"""
TrueCareer recommendation summary script.

This script summarizes the recommendation outputs generated from the
synthetic dataset and the clustering workflow.
"""

from pathlib import Path

import pandas as pd


DATA_PATH = Path("data/truecareer_clustered_output.csv")
SUMMARY_OUTPUT_PATH = Path("data/truecareer_recommendation_summary.csv")

REQUIRED_COLUMNS = [
    "student_id",
    "student_cluster",
    "kmeans_cluster_id",
    "recommended_major",
    "recommended_courses",
    "recommended_mentor_type",
    "recommended_career_path",
]


def load_clustered_data(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load the clustered TrueCareer dataset."""
    if not path.exists():
        raise FileNotFoundError(
            f"Clustered dataset not found: {path}. "
            "Please run python src/clustering.py first."
        )

    return pd.read_csv(path)


def validate_required_columns(df: pd.DataFrame) -> None:
    """Check that recommendation-related columns exist."""
    missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")


def build_recommendation_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Build a summary table by reference cluster and recommendation outputs."""
    summary = (
        df.groupby(
            [
                "student_cluster",
                "recommended_major",
                "recommended_courses",
                "recommended_mentor_type",
                "recommended_career_path",
            ]
        )
        .size()
        .reset_index(name="student_count")
        .sort_values(["student_cluster", "student_count"], ascending=[True, False])
    )

    return summary


def show_recommendation_summary(df: pd.DataFrame) -> None:
    """Print recommendation distributions and examples."""
    print("Recommended major distribution:")
    print(df["recommended_major"].value_counts())

    print("\nRecommended mentor type distribution:")
    print(df["recommended_mentor_type"].value_counts())

    print("\nK-Means cluster distribution:")
    print(df["kmeans_cluster_id"].value_counts().sort_index())

    print("\nReference student cluster distribution:")
    print(df["student_cluster"].value_counts())

    print("\nRecommendation examples:")
    example_columns = [
        "student_id",
        "student_cluster",
        "kmeans_cluster_id",
        "recommended_major",
        "recommended_mentor_type",
        "recommended_career_path",
    ]
    print(df[example_columns].head(10))


def save_recommendation_summary(
    summary: pd.DataFrame,
    output_path: Path = SUMMARY_OUTPUT_PATH,
) -> None:
    """Save the recommendation summary table."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(output_path, index=False)


def main() -> None:
    """Run recommendation summary workflow."""
    dataset = load_clustered_data()
    validate_required_columns(dataset)

    show_recommendation_summary(dataset)

    summary = build_recommendation_summary(dataset)
    save_recommendation_summary(summary)

    print("\nRecommendation summary saved to:")
    print(SUMMARY_OUTPUT_PATH)


if __name__ == "__main__":
    main()
