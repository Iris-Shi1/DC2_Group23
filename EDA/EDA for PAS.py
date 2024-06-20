import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#importing the data
xl_file = "PAS_T&Cdashboard_to Q3 23-24.xlsx"
df_mps = pd.read_excel(xl_file, sheet_name='MPS')
df_borough = pd.read_excel(xl_file, sheet_name='Borough')
df_borough = df_borough.drop(columns=['Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9'])

#EDA

# Histogram for the 'Proportion' column in df_borough
plt.figure(figsize=(10, 6))
sns.histplot(df_borough['Proportion'], kde=True)
plt.title('Distribution of Proportion Values in Borough Data')
plt.show()

# Histogram for the 'Proportion' column in df_mps
plt.figure(figsize=(10, 6))
sns.histplot(df_mps['Proportion'], kde=True)
plt.title('Distribution of Proportion Values in MPS Data')
plt.show()

# Bar chart for 'Measure' in Borough data
plt.figure(figsize=(12, 8))
sns.countplot(y='Measure', data=df_borough, order=df_mps['Measure'].value_counts().index)
plt.title('Frequency of Different Measures in MPS Data')
plt.show()

# Bar chart for 'Measure' in MPS data
plt.figure(figsize=(12, 8))
sns.countplot(y='Measure', data=df_mps, order=df_mps['Measure'].value_counts().index)
plt.title('Frequency of Different Measures in MPS Data')
plt.show()

plt.figure(figsize=(12, 8))
sns.barplot(x='Borough', y='Proportion', data=df_borough, ci=None)
plt.xticks(rotation=90)
plt.title('Proportion of "Good Job" Local by Borough')
plt.ylabel('Proportion')
plt.xlabel('Borough')
plt.show()

# Filter the data for the specific measure
df_trust_mps = df_mps[df_mps['Measure'] == 'Trust MPS']

plt.figure(figsize=(12, 8))
sns.lineplot(x='Date', y='Proportion', data=df_trust_mps)
plt.title('Trust in MPS Over Time')
plt.ylabel('Proportion')
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.show()


#How trust changes over time

plt.figure(figsize=(12, 8))
sns.lineplot(x='Date', y='Proportion', data=df_trust_mps)
plt.title('Trust in MPS Over Time')
plt.ylabel('Proportion')
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.show()
