import pandas as pd


DATA_PATH = "data/truecareer_dataset_v1_4_vietnam_context.csv"


def load_dataset(path=DATA_PATH):
    """Load the TrueCareer dataset."""
    df = pd.read_csv(path)
    return df


def preview_dataset(df):
    """Print basic dataset information."""
    print("Dataset shape:", df.shape)
    print("\nColumns:")
    print(df.columns.tolist())
    print("\nFirst 5 rows:")
    print(df.head())


if __name__ == "__main__":
    dataset = load_dataset()
    preview_dataset(dataset)