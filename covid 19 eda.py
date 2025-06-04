import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Load the dataset
df = pd.read_csv(r"C:\Users\admin\Desktop\COVID-19 Clinical Trials EDA Pandas  (  ML _ FA _ DA projects )\COVID clinical trials.csv") 

# Basic overview
print(df.shape)
print(df.columns)
df.head()

# Summary statistics for numerical columns
print(df.describe())
# Summary statistics for categorical columns
print(df.describe(include='object'))

# Check for missing values
print("Missing value before filling -",df.isnull().sum())

missing_percent = (df.isnull().sum() / len(df)) * 100
print(missing_percent)



# Heatmap of missing values
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import ListedColormap

plt.figure(figsize=(14, 8))

# Define a proper colormap
import matplotlib.pyplot as plt

# Count missing values per column
import matplotlib.pyplot as plt

# Count missing values per column
missing_counts = df.isnull().sum()
missing_counts = missing_counts[missing_counts > 0]  # Keep only columns with missing values

# Plot
plt.figure(figsize=(10, 6))
missing_counts.plot(kind='bar', color='orange', edgecolor='black')
plt.title("Missing Values Count per Column")
plt.xlabel("Columns")
plt.ylabel("Number of Missing Values")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()




# Drop columns with a high percentage of missing values or fill them
df = df.drop(columns=['Acronym', 'Study Documents','Results First Posted'])

# Fill appropriate columns
df['Gender'] = df['Gender'].fillna('All')
df['Interventions'].fillna('Unknown', inplace=True)
df['Phases'].fillna('Not Applicable', inplace=True)
df['Outcome Measures'].fillna('Unknown', inplace=True)
df['Locations'].fillna('Not specified', inplace=True)

print("Missing value After filling -",df.isnull().sum())

Duplicate=(df.duplicated().sum())
print("Number of duplicate rows..:", Duplicate)

# Convert relevant columns to datetime, coercing errors to NaT
date_cols = ['Start Date', 'Primary Completion Date', 'Completion Date']
for col in date_cols:
    df[col] = pd.to_datetime(df[col], errors='coerce')

# Display info about the datetime columns
print(df[date_cols].info())


# Plot the number of trials started over time (grouped by month)
trial_counts = df['Start Date'].dt.to_period('M').value_counts().sort_index()

# Set visualization style
sns.set(style='darkgrid', palette='deep')

trial_counts.plot(
    kind='bar',
    color='skyblue',
    figsize=(14, 6),
    width=0.8
)

plt.title('Trials Started Over Time', fontsize=16, fontweight='bold')
plt.xlabel('Start Month',color="#06433AC7", fontsize=14)
plt.ylabel('Number of Trials',color="#B481E3", fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.xticks(rotation=90,fontsize=7)
plt.tight_layout()
plt.show()



         #Analyze column individually to understand the distribution and key characteristics.

# Count and plot trial statuses
print(df['Status'].value_counts())

df['Status'].value_counts().plot(kind='bar', color="#C8BC0D",figsize=(7, 5), title='Status of Clinical Trials', fontsize=10, width=0.8)
plt.xlabel('Status')
plt.ylabel('Number of Trials')
plt.xticks(rotation=45,color="#010F06C5", fontsize=7, fontweight='bold',)
plt.tight_layout()  
plt.show()


#Phase Distribution: Understand the distribution of trial phases

print(df['Phases'].value_counts())

df['Phases'].value_counts().plot(kind='bar',
title='Distribution of Phases')
plt.xlabel('Phases')
plt.ylabel('Number of Trials')
plt.xticks(rotation=45, color="#010F06C5", fontsize=7, fontweight='bold')
plt.tight_layout()  
plt.show()

#Age Group Distribution analyze
print(df['Age'].value_counts())

df['Age'].value_counts().head(20).plot(kind='bar', title='Age Group Distribution') # Show only top 20 to avoid clutter
plt.xlabel('Age Group')
plt.ylabel('Number of Trials')  
plt.xticks(rotation=45, color="#010F06C5", fontsize=7, fontweight='bold')
plt.tight_layout()
plt.show()

#Explore relationships between different variables(Status vs. Phases):
sns.set(style='darkgrid')
status_phase=pd.crosstab(df['Status'],['Phases'])
print(status_phase)
sns.barplot(data=status_phase,x='Status',y='Phases')
plt.title('Status vs Phases of Clinical Trials')        
plt.xlabel('Status',fontsize=12, fontweight='bold', color="#06433AC7")
plt.ylabel('Phases',fontsize=12, fontweight='bold', color="#B481E3")     
plt.xticks(rotation=45, color="#00000053", fontsize=10, fontweight='bold')
plt.tight_layout()
plt.show()


#Conditions vs. Outcome Measures: Understand the common outcome measures for different conditions.

conditions_outcomes = df.groupby('Conditions')['Outcome Measures']\
    .apply(lambda x: ', '.join(set(x.dropna())))\
    .reset_index()

print(conditions_outcomes)


#1. Save the main cleaned dataset
df.to_csv("final_cleaned_trials.csv", index=False)
print(" Saved: final_cleaned_trials.csv")

#2. Save grouped data: Conditions vs. Outcome Measures
conditions_outcomes.to_csv("conditions_outcomes_summary.csv", index=False)
print(" Saved: conditions_outcomes_summary.csv")

#3. Save the status vs phases summary
status_phase.to_csv("status_vs_phases.csv", index=False)
print("Saved: status_vs_phases.csv")

#4. Save the trial counts over time

# Convert to DataFrame before saving
trial_counts_df = trial_counts.reset_index()
trial_counts_df.columns = ['Start_Month', 'Trial_Count']  # Rename columns for clarity

# Save to CSV
trial_counts_df.to_csv("trial_counts_over_time.csv", index=False)
print(" Saved: trial_counts_over_time.csv")
