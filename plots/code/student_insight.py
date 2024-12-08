import pandas as pd
import matplotlib.pyplot as plt

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

# Count the number of attempts per candidate
candidate_attempts = df_all_years["EKSAMI_SOORITAJA"].value_counts().reset_index()
candidate_attempts.columns = ["Candidate", "Attempt Count"]

# Sort candidates by the number of attempts
candidate_attempts_sorted = candidate_attempts.sort_values("Attempt Count", ascending=False).reset_index(drop=True)

# Scatter plot for attempt distribution
plt.figure(figsize=(12, 6))
plt.scatter(
    range(len(candidate_attempts_sorted)), 
    candidate_attempts_sorted["Attempt Count"], 
    alpha=0.7, color="dodgerblue", edgecolor="black"
)
plt.xlabel("Candidates (sorted by attempts)", fontsize=12)
plt.ylabel("Number of Attempts", fontsize=12)
plt.title("Scatter Plot of Exam Attempts per Candidate", fontsize=14)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()

# Show the scatter plot
plt.show()
