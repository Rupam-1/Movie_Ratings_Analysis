<h1 align="center">Movie Ratings Analysis</h1>
<p align="left">
  <a href="http://temp-url.com" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
</p>

Welcome to the **Movie Ratings Analysis** repository! This project analyzes movie ratings using a dataset containing details about various movies, including their year, duration, rating, genre, director, and actors. The script performs data preprocessing, cleanup, and statistical analysis to extract meaningful insights about trends in movie ratings.

## Contents

1. [Project Documentation](#) *(Add Link Here)*
2. [Dataset (IMDb_Movies_India.csv)](#) *(Add Link Here)*
3. [Script File (movie_analysis.py)](#) *(Add Link Here)*

## Project Overview

- **Objective**: Analyze and extract insights from a dataset of movie ratings.
- **Tools Used**: Python (pandas library)
- **Outcome**: Process and analyze movie data, generate useful insights, and summarize key trends.

## Project Plan

In this project, we will:

- 📥 **Read and preprocess** the movie dataset, handling different file encodings, removing duplicates, and filling missing values.
- 🔄 **Clean and standardize** data types and replace missing values.
- 📊 **Analyze** trends such as:
  - Average and median ratings
  - Average and median duration
  - Top-rated movies
  - Most popular directors and actors
  - Yearly rating trends
  - Correlation between movie duration and rating

## Functions Overview

The script consists of the following functions:

### `read_data(file_path)`
Reads the movie dataset from a CSV file, handling different encoding formats to avoid errors.

### `cleanup_data(data)`
Cleans the dataset by:
- Removing duplicates
- Handling missing values for key fields like `Year`, `Rating`, and `Duration`
- Converting data types (e.g., `Year` to integer, `Votes` to numeric values)
- Replacing missing categorical values with "Unknown"

### `analyze_data(cleaned_data)`
Performs data analysis to extract useful insights, including:
- Overall statistics like average ratings and duration
- Best year based on average ratings
- Correlation between movie duration and rating
- Lists of top-rated and most-voted movies
- Most popular directors and actors

### `final_results(file_path)`
A wrapper function that calls the previous functions sequentially and returns the final analysis results.

## Installation

### Prerequisites

Ensure you have Python installed on your system. You also need to install the required Python library:

```bash
pip install pandas
```

## Usage

### Importing and Running the Script

To use this module in your project, follow these steps:

```python
from Assignment1.file_read import final_results

file_path = "C:\\Users\\RUPAM\\Downloads\\IMDb_Movies_India.csv"
results = final_results(file_path)

for key, value in results.items():
    print(f"{key}:\n{value}\n")
```

## Project Structure

```
├── movie_analysis.py  # Main script for data processing and analysis
├── README.md          # Documentation
└── IMDb_Movies_India.csv  # Dataset (not included in repo)
```

## Example Output

```json
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
```

## Contribution

Feel free to contribute by opening issues or submitting pull requests. Your feedback and suggestions are appreciated.

## Contact

For any questions or inquiries, please email me at [your-email@example.com](mailto:your-email@example.com)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

