import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = '/mnt/data/ELECTION DATASET.csv'
data = pd.read_csv('ELECTION DATASET.csv')

# Data Cleaning: Convert WINNER to boolean
data['WINNER'] = data['WINNER'].astype(bool)

# Extract required analysis columns
analysis_columns = ['GENDER', 'PARTY', 'NAME', 'TOTAL VOTES', 'STATE', 'WINNER']
required_data = data[analysis_columns]

# Filter winners
winners_data = required_data[required_data['WINNER']]

# Gender-based Analysis
gender_distribution = data['GENDER'].value_counts()

plt.figure(figsize=(10, 6))
gender_distribution.plot(kind='bar', color=['skyblue', 'lightpink'], edgecolor='black', alpha=0.8)
plt.title('Gender Distribution of Candidates', fontsize=16)
plt.xlabel('Gender', fontsize=12)
plt.ylabel('Number of Candidates', fontsize=12)
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('gender_distribution.png')
plt.show()

# Winning Candidates Summary
winning_summary = winners_data[['NAME', 'PARTY', 'TOTAL VOTES', 'STATE', 'GENDER']]
print("\nWinning Candidates Summary:\n")
print(winning_summary)

# Winning Party Analysis
party_winners = winners_data['PARTY'].value_counts()

plt.figure(figsize=(10, 6))
party_winners.plot(kind='bar', color='orange', edgecolor='black', alpha=0.8)
plt.title('Winning Party Distribution', fontsize=16)
plt.xlabel('Party', fontsize=12)
plt.ylabel('Number of Winners', fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.tight_layout()
plt.savefig('winning_party_distribution.png')
plt.show()

# Save Winning Candidates Summary to CSV
output_file = 'winning_candidates_summary.csv'
winning_summary.to_csv(output_file, index=False)
print(f"Winning candidates summary saved to {output_file}")
