import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


DATA_PATH = "data/truecareer_dataset_v1_4_vietnam_context.csv"
OUTPUT_PATH = "data/truecareer_clustered_output.csv"

FEATURE_COLUMNS = [
    "math_skill",
    "language_skill",
    "analytical_skill",
    "creativity",
    "problem_solving",
    "technology_interest",
    "business_interest",
    "finance_interest",
    "social_interest",
    "design_interest",
    "communication_skill",
    "leadership",
    "teamwork_preference",
    "adaptability",
    "stress_tolerance",
    "practical_learning_preference",
    "mentor_need",
    "roadmap_need",
    "guidance_need",
    "learning_motivation",
    "labor_market_awareness",
    "growth_mindset",
]


def run_clustering():
    df = pd.read_csv(DATA_PATH)

    X = df[FEATURE_COLUMNS]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    kmeans = KMeans(n_clusters=6, random_state=42, n_init=10)
    df["kmeans_cluster_id"] = kmeans.fit_predict(X_scaled)

    df.to_csv(OUTPUT_PATH, index=False)

    print("Clustering completed.")
    print("Output saved to:", OUTPUT_PATH)
    print("\nCluster distribution:")
    print(df["kmeans_cluster_id"].value_counts().sort_index())


if __name__ == "__main__":
    run_clustering()