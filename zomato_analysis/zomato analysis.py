# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the Zomato dataset
def load_data(zomato_file):
    """Loads the Zomato dataset from a CSV file."""
    if not os.path.exists(zomato_file):
        print(f"Error: The file '{zomato_file}' does not exist.")
        return None

    try:
        data = pd.read_csv(zomato_file, encoding='latin-1')
        print("Data loaded successfully.")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Data cleaning and preprocessing
def clean_data(data):
    """Cleans and preprocesses the Zomato dataset."""
    try:
        data = data.copy()

        # Drop duplicates
        data.drop_duplicates(inplace=True)

        # Drop rows with missing values
        data.dropna(inplace=True)

        # Remove unnecessary columns
        if 'url' in data.columns:
            data.drop(columns=['url'], inplace=True)

        # Standardize column names
        data.columns = [col.strip().lower().replace(' ', '_') for col in data.columns]

        # Clean specific columns (e.g., removing 'votes' column if not numeric)
        if 'votes' in data.columns and data['votes'].dtype == object:
            data['votes'] = (
                data['votes']
                .str.replace(',', '', regex=True)
                .apply(pd.to_numeric, errors='coerce')
            )
            data.dropna(subset=['votes'], inplace=True)

        print("Data cleaned successfully.")
        return data
    except Exception as e:
        print(f"Error during data cleaning: {e}")
        return None

# Exploratory Data Analysis (EDA)
def perform_eda(data):
    """Performs exploratory data analysis on the dataset."""
    try:
        print("Basic Dataset Information:")
        print(data.info())
        
        print("\nBasic Statistical Summary (including non-numeric columns):")
        print(data.describe(include='all'))  # Include all columns, even non-numeric ones

        print("\nColumns with Missing Values:")
        print(data.isnull().sum())

        # Visualization for 'rating' column (treat as categorical)
        if 'rating' in data.columns:
            plt.figure(figsize=(10, 6))
            sns.countplot(data=data, x=data['rating'].fillna('Not Rated'))  # Treat as categorical
            plt.title('Distribution of Ratings')
            plt.xlabel('Rating')
            plt.ylabel('Count')
            plt.xticks(rotation=45)  # Rotate labels if needed
            plt.show()
        else:
            print("The column 'rating' is not present in the dataset. Skipping rating distribution visualization.")
    except Exception as e:
        print(f"Error during EDA: {e}")


# Feature Engineering and Optimization
def optimize_data(data):
    """Optimizes the dataset for analysis."""
    try:
        data = data.copy()

        # Convert categorical columns to numerical
        categorical_columns = data.select_dtypes(include=['object']).columns
        for col in categorical_columns:
            data[col] = pd.factorize(data[col])[0]

        print("Data optimization completed.")
        return data
    except Exception as e:
        print(f"Error during data optimization: {e}")
        return None
# Function to find the best cuisines
def best_cuisines(data, top_n=5):
    """Finds the top cuisines based on the number of restaurants offering them."""
    if 'cuisines' in data.columns:
        cuisines_count = data['cuisines'].value_counts().head(top_n)
        print("Top Cuisines:")
        print(cuisines_count)

        # Plotting the top cuisines
        plt.figure(figsize=(10, 6))
        cuisines_count.plot(kind='bar', color='skyblue')
        plt.title('Top Cuisines')
        plt.xlabel('Cuisines')
        plt.ylabel('Number of Restaurants')
        plt.xticks(rotation=45)
        plt.show()

        return cuisines_count
    else:
        print("'cuisines' column not found in the dataset.")
        return None

# Function to calculate average cost for two
def average_cost_for_two(data):
    """Calculates the average cost for two people across all restaurants."""
    if 'average_cost_for_two' in data.columns:
        avg_cost = data['average_cost_for_two'].mean()
        print(f"Average Cost for Two: {avg_cost:.2f}")

        # Plotting the average cost
        plt.figure(figsize=(6, 6))
        plt.bar(['Average Cost for Two'], [avg_cost], color='lightgreen')
        plt.title('Average Cost for Two')
        plt.ylabel('Cost')
        plt.show()

        return avg_cost
    else:
        print("'average_cost_for_two' column not found in the dataset.")
        return None

# Main execution block
def main():
    filepath = 'zomato.csv'  # Using the provided Zomato dataset file name
    data = load_data('zomato.csv')

    if data is not None:
        cleaned_data = clean_data(data)
        perform_eda(cleaned_data)
        optimized_data = optimize_data(cleaned_data)
        
        print("Final Optimized Data Preview:")
        print(optimized_data.head())
        
        # Find the best cuisines
        best_cuisines(cleaned_data)
        
        # Calculate the average cost for two
        average_cost_for_two(cleaned_data)

# Run the script
if __name__ == "__main__":
    main()
