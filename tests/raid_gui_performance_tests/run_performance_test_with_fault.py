import time
import csv
from tkinter import messagebox


def run_performance_test_with_fault(self, num_operations, data_size):
    if not self.current_raid:
        messagebox.showerror("Error", "No RAID array selected.")
        return

    test_data = "A" * data_size  # Test data to write

    # Disk failure simulation
    self.current_raid.simulate_fault(1)  # Disk failure 1

    # Measure write performance with fault
    start_time = time.perf_counter()
    for i in range(num_operations):
        self.current_raid.write(test_data)
    end_time = time.perf_counter()
    write_time = end_time - start_time

    # Measure read performance with fault
    start_time = time.perf_counter()
    for i in range(num_operations):
        self.current_raid.read(i % len(test_data))
    end_time = time.perf_counter()
    read_time = end_time - start_time

    # Save data to CSV file
    with open("raid_fault_performance.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([self.raid_type_var.get(), "Disk Fault", num_operations, data_size, write_time, read_time])

    messagebox.showinfo("Test Completed", f"Write time with fault: {write_time:.4f}s\nRead time with fault: {read_time:.4f}s")
