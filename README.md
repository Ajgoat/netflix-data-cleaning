Netflix Dataset Cleaning
Overview
This repository contains a Python script (clean_netflix_data_fixed.py) designed to clean the Netflix dataset (netflix_titles.csv). The script addresses common data quality issues, such as missing values, duplicates, inconsistent text, date formats, column names, and data types, using the pandas library.
Purpose
The script processes the Netflix dataset to:

Identify and handle missing values using .isnull().
Remove duplicate rows with .drop_duplicates().
Standardize text fields (e.g., title, director, country) to title case.
Convert date_added to a consistent dd-mm-yyyy format.
Rename column headers to lowercase with underscores.
Ensure correct data types (e.g., integer for release_year, categorical for type).

Dataset
The script expects the netflix_titles.csv file, which contains columns like show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, and description. Note: The dataset is not included in this repository due to its size and potential licensing restrictions. You can obtain it from sources like Kaggle or other data repositories.
Requirements

Python: Version 3.x
Libraries:
pandas (pip install pandas)


Input File: netflix_titles.csv (place it in the same directory as the script)
Output File: netflix_titles_cleaned.csv (generated after running the script)

Usage

Clone the Repository:
git clone https://github.com/Ajgoat/netflix-data-cleaning.git
cd netflix-data-cleaning


Install Dependencies:
pip install pandas


Add the Dataset:

Place the netflix_titles.csv file in the repository directory.
The .gitignore file excludes this dataset to avoid uploading large or sensitive files.


Run the Script:
python clean_netflix_data_fixed.py


Output:

The script generates netflix_titles_cleaned.csv with the cleaned data.
It prints:
Missing values before and after handling.
Data types of the cleaned dataset.
A preview of the first few rows of the cleaned data.





Cleaning Steps

Handle Missing Values:

Identifies missing values using .isnull().
Fills director, cast, and country with "Unknown".
Drops rows where date_added is missing.
Fills rating and duration with their mode (most frequent value).


Remove Duplicates:

Uses .drop_duplicates() to remove duplicate rows.


Standardize Text:

Converts text columns (title, director, cast, country, listed_in, description) to title case and removes extra spaces.
Converts rating to uppercase for consistency.


Convert Date Formats:

Standardizes date_added to dd-mm-yyyy using pd.to_datetime.
Drops rows where dates cannot be parsed.


Rename Columns:

Converts column names to lowercase and replaces spaces with underscores.


Fix Data Types:

Ensures:
show_id: String
type: Categorical
release_year: Integer (Int64)
duration_numeric: Integer (new column with numeric duration values)


Extracts numeric duration (minutes for movies, seasons for TV shows) into duration_numeric.



Notes

The script uses .loc to avoid pandas' SettingWithCopyWarning, ensuring safe DataFrame modifications.
If the input dataset (netflix_titles.csv) is missing or malformed, the script will raise an error.
The dataset is not included in the repository. Users must source it independently.

Repository Structure
netflix-data-cleaning/
├── clean_netflix_data_fixed.py  # Main cleaning script
├── README.md                    # Project documentation
└── .gitignore                   # Excludes dataset and output files

License
This project is licensed under the MIT License. See the LICENSE file for details.
Contact
For issues or questions, open an issue on this repository or refer to the pandas documentation.
