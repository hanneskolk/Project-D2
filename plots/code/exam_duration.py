import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# NOTE: Did not use this plot, as its result was self explanatory

# List of file paths for each year
file_paths = {
    "2021": "./data/se_2021.csv",
    "2022": "./data/se_2022.csv",
    "2023": "./data/se_2023.csv",
    "2024": "./data/se_2024.csv",
}

# Load and concatenate data from all years
df_all_years = pd.concat(
    [pd.read_csv(file_path).assign(Year=year) for year, file_path in file_paths.items()],
    ignore_index=True
)

# Ensure the KESTUS column is numeric (convert if necessary)
df_all_years["KESTUS"] = pd.to_numeric(df_all_years["KESTUS"], errors="coerce")

# Remove rows with missing or invalid durations
df_cleaned = df_all_years.dropna(subset=["KESTUS"])

# Add a binary column for pass/fail
df_cleaned["Passed"] = df_cleaned["SEISUND"] == "SOORITATUD"

# Calculate average duration for passed and failed exams
duration_analysis = df_cleaned.groupby("Passed")["KESTUS"].mean().reset_index()
duration_analysis["Category"] = duration_analysis["Passed"].replace(
    {True: "Passed", False: "Failed"}
)

# Plot average durations
plt.figure(figsize=(8, 6))
sns.barplot(data=duration_analysis, x="Category", y="KESTUS", palette="pastel")
plt.ylabel("Average Duration (Minutes)")
plt.xlabel("Exam Outcome")
plt.title("Exam Duration Analysis: Passed vs Failed")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()

# Show the plot
plt.show()
