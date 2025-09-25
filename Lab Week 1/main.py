import pandas as pd
import matplotlib.pyplot as plt

# Load original dataset
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df_original = pd.read_csv(url)

# Step 1: Count missing values before cleaning
missing_before = df_original.isnull().sum()

# Keep the old data to compare against
df_cleaned = df_original.copy()

# Clean the data - drop irrelevant columns
df_cleaned.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)
# Clean the data - add median age to null fields for age
df_cleaned['Age'] = df_cleaned['Age'].fillna(df_cleaned['Age'].median())
# Clean the data - add mode age to null fields for embarked
df_cleaned['Embarked'] = df_cleaned['Embarked'].fillna(df_cleaned['Embarked'].mode()[0])
# Clean the data - Convert 'Sex' to numeric
df_cleaned['Sex'] = df_cleaned['Sex'].map({'male': 0, 'female': 1})
# Clean the data - Convert Embarked
df = pd.get_dummies(df_cleaned, columns=['Embarked'], drop_first=True)

# Count missing values after cleaning
missing_after = df_cleaned.isnull().sum()

# Combine into a DataFrame for plotting
before_cleaning = pd.DataFrame({
    'Before Cleaning': missing_before,
})

# After cleaning
after_cleaning = pd.DataFrame({
    'After Cleaning': missing_after,
})

# Plot side-by-side bar chart
before_cleaning.plot(kind='bar', color=['orange'])
after_cleaning.plot(kind='bar', color=['green'])
plt.title('Missing Values Before and After Cleaning')
plt.ylabel('Number of Missing Values')
plt.show()
