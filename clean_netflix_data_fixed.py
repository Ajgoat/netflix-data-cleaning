import pandas as pd
from datetime import datetime
import re

  # Load the dataset
df = pd.read_csv(r"C:\Users\DELL\OneDrive\Documents\netflix_titles.csv")

  # Check for missing values
print(df.isnull().sum())

  # Handle missing values
  # Fill missing director, cast, country with 'Unknown'
df.loc[:, 'director'] = df['director'].fillna('Unknown')
df.loc[:, 'cast'] = df['cast'].fillna('Unknown')
df.loc[:, 'country'] = df['country'].fillna('Unknown')

  # Drop rows where date_added is missing (small number, critical field)
df = df.dropna(subset=['date_added'])

  # For rating and duration, fill with mode (most frequent value)
df.loc[:, 'rating'] = df['rating'].fillna(df['rating'].mode()[0])
df.loc[:, 'duration'] = df['duration'].fillna(df['duration'].mode()[0])

  # 2. Remove duplicate rows
df = df.drop_duplicates()

  # 3. Standardize text values
  # Convert text columns to title case for consistency
def standardize_text(text):
    if isinstance(text, str):
        return ' '.join(text.strip().split()).title()
    return text

text_columns = ['title', 'director', 'cast', 'country', 'listed_in', 'description']
for col in text_columns:
    df.loc[:, col] = df[col].apply(standardize_text)

  # Standardize rating to consistent format (e.g., uppercase)
    df.loc[:, 'rating'] = df['rating'].str.upper()

  # 4. Convert date formats
  # Function to parse and standardize dates
def standardize_date(date_str):
    if isinstance(date_str, str):
        try:
              # Remove extra spaces and parse with flexible date parsing
              cleaned_date = ' '.join(date_str.strip().split())
              parsed_date = pd.to_datetime(cleaned_date, format='%B %d, %Y')
              return parsed_date.strftime('%d-%m-%Y')
        except:
              return None
    return None

df.loc[:, 'date_added'] = df['date_added'].apply(standardize_date)
  # Drop rows where date_added couldn't be parsed
df = df.dropna(subset=['date_added'])

  # Convert to lowercase and replace spaces with underscores
df.columns = [re.sub(r'\s+', '_', col.lower().strip()) for col in df.columns]

  # Ensure show_id is string
df.loc[:, 'show_id'] = df['show_id'].astype(str)

  # Ensure type is categorical
df.loc[:, 'type'] = df['type'].astype('category')

  # Ensure release_year is integer
df.loc[:, 'release_year'] = pd.to_numeric(df['release_year'], errors='coerce').astype('Int64')

  # Ensure duration is properly formatted
  # Extract numeric part of duration (for movies in minutes, seasons for TV shows)
def extract_duration(duration):
    if isinstance(duration, str):
         if 'min' in duration:
             return pd.to_numeric(duration.replace(' min', ''), errors='coerce')
         elif 'Season' in duration:
             return pd.to_numeric(duration.split()[0], errors='coerce')
    return None

df.loc[:, 'duration_numeric'] = df['duration'].apply(extract_duration)
df.loc[:, 'duration_numeric'] = df['duration_numeric'].astype('Int64')

  # Verify data types
print(df.dtypes)

  # Check missing values after cleaning
print("\nMissing values after handling:")
print(df.isnull().sum())

  # Save cleaned dataset
df.to_csv('netflix_titles_cleaned.csv', index=False)

  # Display first few rows of cleaned data
print("\nFirst few rows of cleaned data:")
print(df.head())