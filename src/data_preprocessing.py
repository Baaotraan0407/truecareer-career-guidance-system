"""
TrueCareer dataset preprocessing and inspection script.

This script previews the dataset and performs basic quality checks before
clustering and recommendation analysis.
"""

from pathlib import Path

import pandas as pd


DATA_PATH = Path("data/truecareer_dataset_v1_4_vietnam_context.csv")

EXPECTED_COLUMNS = [
    "student_id",
    "gender",
    "grade_level",
    "gpa_band",
    "admission_subject_group",
    "high_school_subject_orientation",
    "location_type",
    "family_income_level",
    "willing_to_relocate",
    "preferred_study_budget",
    "career_priority",
    "role_model_field",
    "student_cluster",
    "recommended_major",
    "recommended_courses",
    "recommended_mentor_type",
    "recommended_career_path",
    "data_type",
    "assessment_source",
    "generation_method",
    "generated_version",
]


def load_dataset(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load the TrueCareer dataset."""
    if not path.exists():
        raise FileNotFoundError(
            f"Dataset file not found: {path}. "
            "Please make sure the dataset is stored in the data/ folder."
        )

    return pd.read_csv(path)


def validate_dataset(df: pd.DataFrame) -> None:
    """Run basic dataset validation checks."""
    missing_expected_columns = [
        col for col in EXPECTED_COLUMNS if col not in df.columns
    ]

    if missing_expected_columns:
        raise ValueError(f"Missing expected columns: {missing_expected_columns}")

    duplicate_student_ids = df["student_id"].duplicated().sum()
    missing_values = df.isna().sum().sum()

    print("Validation summary:")
    print(f"- Duplicate student_id values: {duplicate_student_ids}")
    print(f"- Total missing values: {missing_values}")

    if "generated_version" in df.columns:
        versions = df["generated_version"].dropna().unique().tolist()
        print(f"- Dataset version(s): {versions}")

    if "data_type" in df.columns:
        data_types = df["data_type"].dropna().unique().tolist()
        print(f"- Data type(s): {data_types}")


def preview_dataset(df: pd.DataFrame) -> None:
    """Print basic dataset information."""
    print("Dataset shape:", df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nFirst 5 rows:")
    print(df.head())

    print("\nKey categorical distributions:")

    key_columns = [
        "admission_subject_group",
        "high_school_subject_orientation",
        "student_cluster",
        "recommended_major",
    ]

    for column in key_columns:
        if column in df.columns:
            print(f"\n{column}:")
            print(df[column].value_counts())


def main() -> None:
    """Load, validate, and preview the dataset."""
    dataset = load_dataset()
    validate_dataset(dataset)
    print()
    preview_dataset(dataset)


if __name__ == "__main__":
    main()
