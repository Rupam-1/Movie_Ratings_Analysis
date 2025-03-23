## Movie Ratings Analysis

# Project Overview

This project analyzes movie ratings using a dataset containing details about various movies, including their year, duration, rating, genre, director, and actors. The script performs data preprocessing, cleanup, and statistical analysis to extract meaningful insights about the trends in movie ratings.

Features

Read and preprocess movie data: Handles different file encodings, removes duplicates, and fills missing values.

Data cleanup: Converts data types, replaces missing values, and normalizes certain fields.

Analysis of trends:

Average and median ratings

Average and median duration

Top-rated movies

Most popular directors and actors

Yearly rating trends

Correlation between movie duration and rating

Functions Overview

The script consists of the following functions:

read_data(file_path)

Reads the movie dataset from a CSV file, handling different encoding formats to avoid errors.

cleanup_data(data)

Cleans the dataset by:

Removing duplicates

Handling missing values for key fields like Year, Rating, and Duration

Converting data types (e.g., Year to integer, Votes to numeric values)

Replacing missing categorical values with "Unknown"

analyze_data(cleaned_data)

Performs data analysis to extract useful insights, including:

Overall statistics like average ratings and duration

Best year based on average ratings

Correlation between movie duration and rating

Lists of top-rated and most-voted movies

Most popular directors and actors

final_results(file_path)

A wrapper function that calls the previous functions sequentially and returns the final analysis results.

Installation

Prerequisites

Ensure you have Python installed on your system. You also need to install the required Python library:

pip install pandas

Usage

Importing and Running the Script

To use this module in your project, follow these steps:

from Assignment1.file_read import final_results

file_path = "C:\\Users\\RUPAM\\Downloads\\IMDb_Movies_India.csv"
results = final_results(file_path)

for key, value in results.items():
    print(f"{key}:\n{value}\n")

Project Structure

├── movie_analysis.py  # Main script for data processing and analysis
├── README.md          # Documentation
└── IMDb_Movies_India.csv  # Dataset (not included in repo)

Example Output

{
  "Data Trends": {
    "Total Movies": 5000,
    "Average Rating": 7.2,
    "Median Rating": 7.0,
    "Average Duration": 120,
    "Median Duration": 118,
    "Oldest Movie Year": 1950,
    "Newest Movie Year": 2023
  },
  "Best Year": 2010,
  "Best Year Average Rating": 8.1,
  "Duration vs Rating Correlation": 0.35,
  "Top 10 Movies Overall": [...],
  "Top Directors": [...]
}

Contributing

Feel free to open issues or submit pull requests if you would like to improve this project.

License

This project is licensed under the MIT License - see the LICENSE file for details.

