
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_excel("NIE_ISE_Student_Data.xlsx")

# --- EDA ---
print("Dataset Shape:", df.shape)
print("\nData Types:\n", df.dtypes)
print("\nNull Values:\n", df.isnull().sum())
print("\nStatistical Summary:\n", df.describe(include='all'))

# --- Preprocessing ---
# Fill missing Test1, Test2 marks with mean
test_columns = [col for col in df.columns if "Test" in col]
df[test_columns] = df[test_columns].fillna(df[test_columns].mean())

# Fill SEE absentees with 0
see_columns = [col for col in df.columns if "SEE" in col]
df[see_columns] = df[see_columns].fillna(0)

# Encode categorical features
df['Background'] = df['Background'].map({'Urban': 1, 'Village': 0})
df['Name'] = df['Name'].astype('category').cat.codes

# --- Feature Engineering ---
subjects = ['DSA', 'OOP', 'CO', 'DBMS', 'SE']
for subject in subjects:
    df[f'{subject}_Total'] = df[f'{subject}_Test1'] + df[f'{subject}_Test2'] + df[f'{subject}_SEE']

# Overall totals and averages
df['Overall_Total'] = df[[f'{sub}_Total' for sub in subjects]].sum(axis=1)
df['Overall_Avg'] = df['Overall_Total'] / len(subjects)

# --- Visualizations (Optional) ---
plt.figure(figsize=(10, 6))
sns.histplot(df['Overall_Avg'], kde=True, bins=30)
plt.title("Distribution of Overall Averages")
plt.xlabel("Average Marks")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
