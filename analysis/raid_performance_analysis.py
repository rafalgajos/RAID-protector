import pandas as pd
import matplotlib.pyplot as plt
import os

# Get the current directory of the script and create the full path to the CSV file
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_dir, "../data/raid_performance.csv")

# Load data from CSV file
data = pd.read_csv(csv_file_path, names=["RAID Level", "Number of Operations", "Data Size", "Write Time", "Read Time"])

# Plot Write Time using bar plot
plt.figure(figsize=(10, 6))
plt.bar(data["RAID Level"], data["Write Time"], color='b', label='Write Time')
plt.title("RAID Write Performance")
plt.xlabel("RAID Level")
plt.ylabel("Write Time (seconds)")
plt.legend()
plt.show()

# Plot Read Time using bar plot
plt.figure(figsize=(10, 6))
plt.bar(data["RAID Level"], data["Read Time"], color='g', label='Read Time')
plt.title("RAID Read Performance")
plt.xlabel("RAID Level")
plt.ylabel("Read Time (seconds)")
plt.legend()
plt.show()
