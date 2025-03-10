#!/usr/bin/env python3
import pandas as pd

def load_dataset(file_path):
    """
    Reads the dataset from the given file path and returns it as a pandas DataFrame.

    Parameters:
    file_path (str): The path to the dataset file.

    Returns:
    pd.DataFrame: The dataset as a pandas DataFrame. Returns None if an error occurs.
    """
    try:
        # Read the dataset
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    file_path = "population_total.csv"
    df = load_dataset(file_path)
    if df is not None:
        print(df.head())
    else:
        print("Failed to load the dataset.")
