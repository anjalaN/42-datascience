#!/usr/bin/env python3
import matplotlib.pyplot as plt
from load_csv import load_dataset

def plot_population(file_path, country1, country2):
    """
    Plots the population projections for two countries from 1800 to 2050.

    Parameters:
    file_path (str): The path to the dataset file.
    country1 (str): The first country to plot.
    country2 (str): The second country to plot.
    """
    # Load the dataset
    df = load_dataset(file_path)

    if df is not None:
        try:
            # Filter data for the selected countries
            if country1 not in df['country'].values or country2 not in df['country'].values:
                print(f"Error: One or both countries ('{country1}', '{country2}') not found in the dataset.")
                return

            data_country1 = df[df['country'] == country1].iloc[0, 1:]
            data_country2 = df[df['country'] == country2].iloc[0, 1:]

            # Extract years (columns) and population values
            years = data_country1.index.astype(int)
            population1 = data_country1.values
            population2 = data_country2.values

            # Plot population projections with custom settings
            plt.plot(years, population1, label=country1,  color='green', linewidth=1)
            plt.plot(years, population2, label=country2, color='blue', linewidth=1)

            # Add title, axis labels, and legend
            plt.title('Population Projections ')
            plt.xlabel('Year')
            plt.ylabel('Population')
            plt.legend()

            # Remove any additional gridlines or tick marks causing visual artifacts
            plt.grid(False)  # Disables the gridlines
            plt.tick_params(axis='y', length=0)  # Removes tick marks on the y-axis
            # Set x-axis ticks for better readability
            plt.xticks(range(1800, 2051, 40), rotation=45)
           
            # Optimize layout and display the plot
            plt.tight_layout()

            plt.show()
        except KeyError as e:
            print(f"Key error: {e}. Ensure the dataset contains the expected structure and data.")
        except ValueError as e:
            print(f"Value error: {e}. Ensure the dataset's columns can be interpreted as integers (e.g., years).")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    else:
        print("Failed to load the dataset.")

if __name__ == "__main__":
    # Example usage
    file_path = "population_total.csv"
    country1 = "France"  # Replace with your campus's country
    country2 = "Belgium"  # Replace with another country of your choice
    plot_population(file_path, country1, country2)
