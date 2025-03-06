import pandas as pd


def load_data(file_path):
    """Loads CSV data into a Pandas DataFrame."""
    try:
        df = pd.read_csv(file_path)
        df["Date"] = pd.to_datetime(df["Date"])  # Convert to datetime
        return df
    except Exception as e:
        print(f"Error loading file: {e}")
        return None
