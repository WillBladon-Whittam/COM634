import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

sns.set(style="whitegrid")

# Read in Data
df = pd.read_csv('retail_sales_final.csv')

# Bar chart to show count of missing values per column
plt.figure(figsize=(8,5))
missing_counts = df.isnull().sum()
missing_counts.plot(kind='bar', color='orange')
plt.title("Missing Values per Column")
plt.ylabel("Count")

# Histogram to show distribution of a numerical column
plt.figure(figsize=(8,5))
df['Sales'].plot(kind='hist', bins=20, color='skyblue')
plt.title("Sales Distribution (Messy)")
plt.xlabel("Sales")

# Pie chart to show proportion of missing vs non-missing
plt.figure(figsize=(8,5))
missing_total = df.isnull().sum().sum()
non_missing_total = df.size - missing_total
plt.pie([missing_total, non_missing_total], labels=['Missing', 'Non-Missing'], autopct='%1.1f%%', colors=['red', 'green'])
plt.title("Overall Missing Data Proportion")

# Heatmap to show missing values
plt.figure(figsize=(8,5))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Values Heatmap")

# Boxplot to detect outliers in 'Sales'
plt.figure(figsize=(8,5))
sns.boxplot(x=df['Sales'])
plt.title("Sales Boxplot (Messy)")

# Check for duplicate rows
print("Number of duplicates:", df.duplicated().sum())

# Drop rows with any missing values
df = df.drop_duplicates()
df_cleaned = df.dropna()

# Calculate mean, median, and mode for 'sales'
print("Mean Sales:", df_cleaned['Sales'].mean())
print("Median Sales:", df_cleaned['Sales'].median())
print("Mode Sales:", df_cleaned['Sales'].mode()[0])

# Histogram of 'sales'
plt.figure(figsize=(8,5))
df_cleaned['Sales'].plot(kind='hist', bins=20, color='green')
plt.title("Sales Distribution (Clean)")
plt.xlabel("Sales")

# Boxplot of 'sales'
plt.figure(figsize=(8,5))
sns.boxplot(x=df_cleaned['Sales'])
plt.title("Sales Boxplot (Clean)")

# Correlation heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df_cleaned[["Sales", "Profit"]].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")

# Scatter plot of 'sales' vs 'profit'
plt.figure(figsize=(8,5))
sns.scatterplot(x='Sales', y='Profit', data=df_cleaned)
plt.title("Sales vs Profit")
plt.show()

# Save the cleaned dataset to a new CSV file
df_cleaned.to_csv('retail_sales_clean.csv', index=False)

# First, calculate the mean of the 'Sales' column
mean_sales = df['Sales'].mean()
# Then, fill missing values in 'Sales' with the mean
df['Sales'] = df['Sales'].fillna(mean_sales)
# This helps ensure that missing sales data doesn't distort your analysis

# Replace missing values in 'Profit' with 0
df['Profit'] = df['Profit'].fillna(0)
# This assumes that missing profit means no profit was made

# Replace missing values in 'Country' with the string 'Unknown'
df['Country'] = df['Country'].fillna('Unknown')
# This helps maintain consistency in categorical data


# Fill missing values using the previous row's value
df['Sales'] = df['Sales'].fillna(method='ffill')
# Useful for time-series or sequential data

# Fill missing values using the next row's value
df['Sales'] = df['Sales'].fillna(method='bfill')

# Check how many missing values exist before filling
print("Missing before:", df.isnull().sum())
# Fill missing values (example: fill 'Profit' with 0)
df['Profit'] = df['Profit'].fillna(0)
# Check how many missing values remain after filling
print("Missing after:", df.isnull().sum())