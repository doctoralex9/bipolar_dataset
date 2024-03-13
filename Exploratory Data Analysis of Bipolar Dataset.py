#Exploratory Data Analysis of Bipolar Dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sqlite3
# Load data from Excel file
data = pd.read_excel('bipolar_dataset.xlsx') 
print ('the firts rows of the DataFrame:')
print (data.head())
#Check the data types of each column
print ('the data types of each column:')
print (data.dtypes)
#Check for missing values
print('missing values:')
print (data.isnull().sum())
#Perform summary statistics on numerical columns
print("summary statistics:")
print (data.describe())
#Data Visualization
#Plot histograms for numerical columns
plt.hist(data['n_chars'],bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Character Count')
plt.xlabel('Number of Characters')
plt.ylabel('Frequnecy')
plt.show()
#Data Analysis
#Calculate the mean, median, and standard deviation of numerical columns
mean_n_chars = np.mean(data['n_chars'])
median_n_chars=np.median(data['n_chars'])
print ('mean number of characters',mean_n_chars)
print('median number of characters',median_n_chars)
# Connect to SQLite database
conn = sqlite3.connect('bipolar_dataset.db')
# Convert DataFrame to SQLite table
data.to_sql('bipolar_dataset',conn, if_exists='replace' , index=False)
# Commit changes and close connection
conn.commit()
conn.close()