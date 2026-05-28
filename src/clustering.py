"""
TrueCareer K-Means clustering script.

This script:
1. Loads the synthetic Vietnam-context TrueCareer dataset.
2. Selects only numeric assessment-related features.
3. Standardizes the selected features.
4. Runs K-Means clustering with k = 6.
5. Saves the clustered dataset.
6. Saves a cluster profile summary for interpretation.
"""

from pathlib import Path

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler


DATA_PATH = Path("data/truecareer_dataset_v1_4_vietnam_context.csv")
OUTPUT_PATH = Path("data/truecareer_clustered_output.csv")
CLUSTER_PROFILE_PATH = Path("data/truecareer_cluster_profile_summary.csv")

N_CLUSTERS = 6
RANDOM_STATE = 42

FEATURE_COLUMNS = [
    # Academic skills
    "math_skill",
    "language_skill",
    "analytical_skill",
    "creativity",
    "problem_solving",

    # Interest orientation
    "technology_interest",
    "business_interest",
    "finance_interest",
    "social_interest",
    "design_interest",

    # Personality and work style
    "communication_skill",
    "leadership",
    "teamwork_preference",
    "adaptability",
    "stress_tolerance",

    # Learning behavior and guidance needs
    "practical_learning_preference",
    "mentor_need",
    "roadmap_need",
    "guidance_need",
    "learning_motivation",
    "labor_market_awareness",
    "growth_mindset",
]


def load_dataset(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load the TrueCareer dataset from CSV."""
    if not path.exists():
        raise FileNotFoundError(
            f"Dataset file not found: {path}. "
            "Please make sure the dataset is stored in the data/ folder."
        )

    return pd.read_csv(path)


def validate_feature_columns(df: pd.DataFrame, feature_columns: list[str]) -> None:
    """Validate that all clustering feature columns exist and are numeric."""
    missing_columns = [col for col in feature_columns if col not in df.columns]

    if missing_columns:
        raise ValueError(f"Missing feature columns: {missing_columns}")

    non_numeric_columns = [
        col for col in feature_columns
        if not pd.api.types.is_numeric_dtype(df[col])
    ]

    if non_numeric_columns:
        raise TypeError(f"Non-numeric feature columns found: {non_numeric_columns}")


def run_kmeans_clustering(
    df: pd.DataFrame,
    feature_columns: list[str],
    n_clusters: int = N_CLUSTERS,
    random_state: int = RANDOM_STATE,
) -> tuple[pd.DataFrame, float]:
    """Run K-Means clustering using numeric assessment-related features."""
    X = df[feature_columns].copy()

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    kmeans = KMeans(
        n_clusters=n_clusters,
        random_state=random_state,
        n_init=10,
    )

    clustered_df = df.copy()
    clustered_df["kmeans_cluster_id"] = kmeans.fit_predict(X_scaled)

    silhouette = silhouette_score(X_scaled, clustered_df["kmeans_cluster_id"])

    return clustered_df, silhouette


def generate_cluster_profile(
    clustered_df: pd.DataFrame,
    feature_columns: list[str],
) -> pd.DataFrame:
    """Create a cluster profile table based on average feature scores."""
    cluster_profile = (
        clustered_df.groupby("kmeans_cluster_id")[feature_columns]
        .mean()
        .round(2)
        .reset_index()
    )

    cluster_sizes = (
        clustered_df["kmeans_cluster_id"]
        .value_counts()
        .sort_index()
        .rename_axis("kmeans_cluster_id")
        .reset_index(name="student_count")
    )

    return cluster_sizes.merge(cluster_profile, on="kmeans_cluster_id", how="left")


def save_outputs(
    clustered_df: pd.DataFrame,
    cluster_profile: pd.DataFrame,
    output_path: Path = OUTPUT_PATH,
    profile_path: Path = CLUSTER_PROFILE_PATH,
) -> None:
    """Save clustered dataset and cluster profile summary."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    clustered_df.to_csv(output_path, index=False)
    cluster_profile.to_csv(profile_path, index=False)


def main() -> None:
    """Run the full clustering workflow."""
    df = load_dataset()
    validate_feature_columns(df, FEATURE_COLUMNS)

    clustered_df, silhouette = run_kmeans_clustering(
        df=df,
        feature_columns=FEATURE_COLUMNS,
        n_clusters=N_CLUSTERS,
        random_state=RANDOM_STATE,
    )

    cluster_profile = generate_cluster_profile(
        clustered_df=clustered_df,
        feature_columns=FEATURE_COLUMNS,
    )

    save_outputs(clustered_df, cluster_profile)

    print("K-Means clustering completed.")
    print(f"Number of clusters: {N_CLUSTERS}")
    print(f"Feature columns used: {len(FEATURE_COLUMNS)}")
    print(f"Silhouette score: {silhouette:.4f}")

    print("\nCluster distribution:")
    print(clustered_df["kmeans_cluster_id"].value_counts().sort_index())

    print("\nCluster profile summary saved to:")
    print(CLUSTER_PROFILE_PATH)

    print("\nClustered output saved to:")
    print(OUTPUT_PATH)


if __name__ == "__main__":
    main()
