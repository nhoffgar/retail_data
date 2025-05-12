import requests
from bs4 import BeautifulSoup
import pandas as pd
# Load CSV file
df = pd.read_csv("ecommdata.csv")

# View first few rows and basic info
print(df.head())
print(df.info())
print(df.describe())
# Check for missing values
print(df.isnull().sum())   
# Check for duplicates
print(df.duplicated().sum())