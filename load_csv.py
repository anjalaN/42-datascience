#!/usr/bin/env python3
import pandas as pd

def dataset_dimensions(file_path):
    """
    reads dataset from the given file pathe, writes its dimensions to a file, and return the dimensions.

    Parameters:
    file_path(str): The path to the dataset file.

    Returns:
    tuple: The dimensions of the dataset (rows, coloumns). 
    """
    try:
        #Read the dataset
        df = pd.read_csv(file_path)

        #Get the dimension of the dataset
        dimensions = df.shape

        #wrute the dimension to a file
        with open("dataset_dimensions.txt", "w") as file:
            file.write(f"Dimensions of the dataset: {dimensions[0]} rows, {dimensions[1]} columns\n")
            return dimensions, df
    except Exception as e:
            print(f"An error occurred: {e}")
            return None

if __name__ == "__main__":
    file_path = "life_expectancy_years.csv"
    dimensions, df = dataset_dimensions(file_path)
    if dimensions:
        print(f"The dimensions of the dataset are: {dimensions}")
    else:
         print("Fail to  read the dataset")
     