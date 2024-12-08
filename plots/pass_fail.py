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

# Set up the plot with 4 subplots (one for each year)
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Loop through each year and create a pie chart for each
years = ["2021", "2022", "2023", "2024"]
for i, year in enumerate(years):
    ax = axes[i//2, i%2]  # Get the correct subplot axis
    # Filter the DataFrame for the specific year
    year_data = df_all_years[df_all_years["Year"] == year]
    
    # Calculate the counts of passed and failed exams
    passed = (year_data["SEISUND"] == "SOORITATUD").sum()
    failed = (year_data["SEISUND"] == "MITTE_SOORITATUD").sum()
    
    # Data for pie chart
    labels = ["Passed", "Failed"]
    sizes = [passed, failed]
    colors = ["#66b3ff", "#ff6666"]
    explode = (0.1, 0)
    
    # Plot the pie chart
    ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
    ax.set_title(f"Exam Results for {year}")
    ax.axis('equal')

# Adjust the layout
plt.tight_layout()

# Show the plot
plt.show()
