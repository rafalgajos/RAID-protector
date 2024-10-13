import pandas as pd
import matplotlib.pyplot as plt
import os

# Get the current directory of the script and create the full path to the CSV file
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_dir, "../data/raid_fault_performance.csv")

# Load data from CSV file
data = pd.read_csv(csv_file_path, names=["RAID Level", "Fault Type", "Number of Operations", "Data Size", "Write Time", "Read Time"])

# Convert "Write Time" and "Read Time" columns to numeric, coercing errors
data["Write Time"] = pd.to_numeric(data["Write Time"], errors="coerce")
data["Read Time"] = pd.to_numeric(data["Read Time"], errors="coerce")

# Plot Write Time using bar plot, skipping rows with "Error"
plt.figure(figsize=(10, 6))
valid_write_data = data.dropna(subset=["Write Time"])
plt.bar(valid_write_data["RAID Level"], valid_write_data["Write Time"], color='b', label='Write Time')
plt.title("RAID Write Performance with Disk Fault")
plt.xlabel("RAID Level")
plt.ylabel("Write Time (seconds)")
plt.legend()
plt.show()

# Plot Read Time using bar plot, skipping rows with "Error"
plt.figure(figsize=(10, 6))
valid_read_data = data.dropna(subset=["Read Time"])
plt.bar(valid_read_data["RAID Level"], valid_read_data["Read Time"], color='g', label='Read Time')
plt.title("RAID Read Performance with Disk Fault")
plt.xlabel("RAID Level")
plt.ylabel("Read Time (seconds)")
plt.legend()
plt.show()
