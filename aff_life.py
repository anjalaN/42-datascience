#!/usr/bin/env python3
import matplotlib.pyplot as plt
from load_csv import load_dataset

def plot_life_expectancy(file_path, country):
    """
    Plots the life expectancy over time for the given country.

    Parameters:
    file_path (str): The path to the dataset file.
    country (str): The country to plot data for.
    """
    # Load the dataset
    df = load_dataset(file_path)

    if df is not None:
        # Filter data for the specified country
        country_data = df[df['country'] == country]

        # Extract years and life expectancy values
        years = country_data.columns[1:]
        life_expectancy = country_data.iloc[0, 1:]

        #convert years to integers
        years = years.astype(int)

        # Plot the data
        plt.plot(years, life_expectancy, marker='o')

         # Set custom x-axis ticks
        plt.xticks(range(1800, 2101, 40))  # Change the interval to 40 years (1800, 1840, 1880, ...)

        # Set chart title and labels
        plt.title(f'{country} Life Expectancy projections')
        plt.xlabel('Year')
        plt.ylabel('Life Expectancy')
        plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

        # Display the plot
        plt.tight_layout()
        plt.show()
    else:
        print("Failed to load the dataset.")

if __name__ == "__main__":
    file_path = "life_expectancy_years.csv"
    country = "France"
    plot_life_expectancy(file_path, country)
