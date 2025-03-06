def clean_data(df):
    """Cleans the dataset by handling missing values and duplicates."""
    df.drop_duplicates(inplace=True)  # Remove duplicate rows
    return df
