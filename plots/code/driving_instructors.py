import pandas as pd
import matplotlib.pyplot as plt

# NOTE: Did not use this plot, as it didn't fit on the poster

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

# Add a column to indicate if a driving instructor was present
df_all_years["Instructor Present"] = df_all_years["SOIDUOPETAJA_KAASAS"] == "E"

# Calculate pass rates with and without an instructor present
pass_rates_instructor = df_all_years.groupby("Instructor Present").apply(
    lambda x: (x["SEISUND"] == "SOORITATUD").mean() * 100
).reset_index(name="Pass Rate")

# Label categories for clarity
pass_rates_instructor["Category"] = pass_rates_instructor["Instructor Present"].replace(
    {True: "With Instructor", False: "Without Instructor"}
)

# Plot the pass rates
plt.figure(figsize=(8, 6))
plt.bar(pass_rates_instructor["Category"], pass_rates_instructor["Pass Rate"], color=["skyblue", "salmon"])
plt.ylabel("Pass Rate (%)")
plt.title("Impact on Pass Rates When Driving Instructor is Present at the Exam")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()

# Show the plot
plt.show()
