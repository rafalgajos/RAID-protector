import time
import csv
from tkinter import messagebox


def run_performance_test(self, num_operations, data_size):
    if not self.current_raid:
        messagebox.showerror("Error", "No RAID array selected.")
        return

    test_data = "A" * data_size  # Test data to write

    # Measure write performance
    start_time = time.perf_counter()
    for i in range(num_operations):
        self.current_raid.write(test_data)
    end_time = time.perf_counter()
    write_time = end_time - start_time

    # Measure read performance
    start_time = time.perf_counter()
    for i in range(num_operations):
        self.current_raid.read(i % len(test_data))
    end_time = time.perf_counter()
    read_time = end_time - start_time

    # Save data to CSV file
    with open("raid_performance.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([self.raid_type_var.get(), num_operations, data_size, write_time, read_time])

    messagebox.showinfo("Test Completed", f"Write time: {write_time:.4f}s\nRead time: {read_time:.4f}s")
