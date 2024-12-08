import pandas as pd
import matplotlib.pyplot as plt

# List of file paths for each year
file_paths = {
    "2021": "./data/se_2021.csv",
    "2022": "./data/se_2022.csv",
    "2023": "./data/se_2023.csv",
    "2024": "./data/se_2024.csv",
}

# Initialize an empty DataFrame to hold all data
df_all_years = pd.DataFrame()

# Load and concatenate data from each year
for year, file_path in file_paths.items():
    # Read CSV file for the current year
    df = pd.read_csv(file_path)
    
    # Add a column for the year to track the year of the exam
    df['Year'] = year
    
    # Append the data for the current year to the overall DataFrame
    df_all_years = pd.concat([df_all_years, df], ignore_index=True)

# Split 'VEAD' column into individual error types
df_all_years['VEAD'] = df_all_years['VEAD'].fillna('')  # Replace NaNs with empty strings for missing error data
df_all_years['VEAD'] = df_all_years['VEAD'].apply(lambda x: x.split('|') if x else [])

# Flatten the list of errors into separate rows
errors_expanded = df_all_years.explode('VEAD')

# Get the frequency of each error
error_counts = errors_expanded['VEAD'].value_counts().reset_index(name='Count')
error_counts.columns = ['Error', 'Count']

# Filter errors with counts greater than or equal to 1000
error_counts_filtered = error_counts[error_counts['Count'] >= 1000]

# Sort the errors by the count in ascending order
error_counts_filtered = error_counts_filtered.sort_values(by='Count')

# Plotting: Bar chart of error counts
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting the bars
ax.barh(error_counts_filtered['Error'], error_counts_filtered['Count'], color='skyblue')

# Add labels and title
ax.set_xlabel('Count of Occurrences')
ax.set_ylabel('Errors')
ax.set_title('Highest Impact Mistakes (>= 1000 occurrences)')

# Display the plot
plt.tight_layout()
plt.show()
