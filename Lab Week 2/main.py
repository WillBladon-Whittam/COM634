import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statistics
from scipy import stats
import time

df = pd.read_csv("user_behavior_dataset.csv")
df.dropna(inplace=True)
df = df[df['Screen_On_Time'] > 0]

mean_screen = df['Screen_On_Time'].mean()
median_screen = df['Screen_On_Time'].median()
mode_screen = df['Screen_On_Time'].mode()[0]
std_screen = df['Screen_On_Time'].std()
range_screen = df['Screen_On_Time'].max() - df['Screen_On_Time'].min()
print("Screen On Time")
print(f"Mean: {mean_screen:.2f}, Median: {median_screen}, Mode: {mode_screen}")
print(f"Standard Deviation: {std_screen:.2f}, Range: {range_screen}")

# Plot 1: Distribution of Screen-On Time
plt.figure(figsize=(8,5))
sns.histplot(df['Screen_On_Time'], bins=20, kde=True)
plt.title("Distribution of Screen-On Time")
plt.xlabel("Hours per Day")
plt.ylabel("Frequency")

# Plot 2: Boxplot of App Usage Time
plt.figure(figsize=(8,5))
sns.boxplot(x=df['App_Usage_Time'])
plt.title("Boxplot of App Usage Time")
plt.xlabel("Minutes per Day")

# Plot 3: Heatmap of Correlation Between Variables
plt.figure(figsize=(10,6))
sns.heatmap(df[["App_Usage_Time", "Screen_On_Time", "Battery_Drain", "Number_of_Apps_Installed", "Data_Usage", "User_Behavior_Class"]].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Between Variables")

# Plot 4: Average Screen-On Time by Operating System
plt.figure(figsize=(8,5))
os_group = df.groupby('Operating_System')['Screen_On_Time'].mean()
os_group.plot(kind='bar', color=['skyblue', 'salmon'])
plt.title("Average Screen-On Time by Operating System")
plt.ylabel("Hours per Day")

# Display all the plots at once
print(df.describe())

plt.show()  # Only one show at the end
