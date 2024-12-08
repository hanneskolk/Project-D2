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

# Calculate the total number of exams per driving school
school_exam_counts = df_all_years.groupby("VIIMANE_AUTOKOOL").size().reset_index(name="Total Exams")

# Select top 10 schools with the highest number of exams
top_10_schools = school_exam_counts.sort_values(by="Total Exams", ascending=False).head(10)

# Filter the main DataFrame to include only these top 10 schools
df_top_schools = df_all_years[df_all_years["VIIMANE_AUTOKOOL"].isin(top_10_schools["VIIMANE_AUTOKOOL"])]

# Calculate pass rates by driving school for the selected top 10 schools
pass_rate_by_school_top = df_top_schools.groupby("VIIMANE_AUTOKOOL").apply(
    lambda x: (x["SEISUND"] == "SOORITATUD").mean() * 100
).reset_index(name="Pass Rate")

# Sort the results by pass rate in ascending order
pass_rate_by_school_top = pass_rate_by_school_top.sort_values("Pass Rate")

# Plot the results for top 10 schools
plt.figure(figsize=(12, 8))
plt.barh(pass_rate_by_school_top["VIIMANE_AUTOKOOL"], pass_rate_by_school_top["Pass Rate"], color="lightcoral")
plt.xlabel("Pass Rate (%)")
plt.ylabel("Driving School")
plt.title("Pass Rate by Top 10 Driving Schools (2021-2024)")
plt.tight_layout()
plt.show()
