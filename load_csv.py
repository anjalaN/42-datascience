#!/user/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt

def load_dataset(file_path):
    """
    Read dataset form the given file path, and read returns the dataFrame,

    Parameters:
    file_path (str): the path to the dataset file.

    Returns: The dataset as a pandas DataFrame. Returns None if an error occurs. 
    """
    try:
        #Read the dataset
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"an error occured: {e}")
        return None
    
if __name__ == "__main__":
    #Example usage
    file_path = "life_expectancy_years.csv"
    df = load_dataset(file_path)
    if df is not None:
        print(df.head())
    else:
        print("Failed to load the dataset.")