import pandas as pd
import matplotlib.pyplot as plt

# List of file paths for each year
file_paths = {
    "2021": "./data/se_2021.csv",
    "2022": "./data/se_2022.csv",
    "2023": "./data/se_2023.csv",
    "2024": "./data/se_2024.csv",
}

# Initialize a dictionary to store pass rates by location for each year
pass_rate_data = {}

# Iterate through each year and calculate pass rates
for year, file_path in file_paths.items():
    # Read data for the year
    df = pd.read_csv(file_path)
    
    # Calculate pass rates by location
    pass_rate_by_location = df.groupby("BYROO").apply(
        lambda x: (x["SEISUND"] == "SOORITATUD").mean() * 100
    ).reset_index(name="Pass Rate")
    
    # Store pass rates in the dictionary
    pass_rate_data[year] = pass_rate_by_location

# Create subplots for each year
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(16, 12), sharex=True)
axes = axes.flatten()

# Plot each year's data
for idx, (year, pass_rate_by_location) in enumerate(pass_rate_data.items()):
    ax = axes[idx]
    pass_rate_by_location = pass_rate_by_location.sort_values("Pass Rate")
    ax.barh(pass_rate_by_location["BYROO"], pass_rate_by_location["Pass Rate"], color="skyblue")
    ax.set_title(f"Driving Exam Pass Rate by Location ({year})")
    ax.set_xlabel("Pass Rate (%)")
    ax.set_ylabel("Location")

    ax.grid(axis="x", linestyle="--", alpha=0.7)

# Adjust layout
plt.tight_layout()
plt.show()
