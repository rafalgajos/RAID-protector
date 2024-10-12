import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Progressbar
import time
import json
from src.raid0 import RAID0
from src.raid1 import RAID1
from src.raid3 import RAID3


class RAIDMonitorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("RAID Monitor")

        # RAID array setup
        self.raid0 = RAID0(4, 128)
        self.raid1 = RAID1(4, 128)
        self.raid3 = RAID3(4, 128)

        self.current_raid = None  # Selected RAID array

        # Dropdown for selecting RAID type
        self.raid_type_var = tk.StringVar(value="RAID0")
        self.raid_type_menu = tk.OptionMenu(master, self.raid_type_var, "RAID0", "RAID1", "RAID3", command=self.select_raid)
        self.raid_type_menu.grid(row=0, column=0)

        # Entry for input data
        self.data_entry = tk.Entry(master, width=50)
        self.data_entry.grid(row=1, column=0, columnspan=3)

        # Buttons for Write/Read
        self.write_button = tk.Button(master, text="Write Data", command=self.write_data)
        self.write_button.grid(row=2, column=0)

        self.read_button = tk.Button(master, text="Read Data", command=self.read_data)
        self.read_button.grid(row=2, column=1)

        # Monitor for RAID state
        self.state_text = tk.Text(master, height=10, width=80)
        self.state_text.grid(row=3, column=0, columnspan=3)

        # Labels for disks, progress bars and percent labels
        self.disk_labels = []
        self.disk_progress = []
        self.disk_percent_labels = []

        for i in range(4):
            label = tk.Label(master, text=f"Disk {i}")
            label.grid(row=4 + i, column=0)

            progress = Progressbar(master, orient="horizontal", length=200, mode="determinate")
            progress.grid(row=4 + i, column=1)

            percent_label = tk.Label(master, text="0%")
            percent_label.grid(row=4 + i, column=2)

            self.disk_labels.append(label)
            self.disk_progress.append(progress)
            self.disk_percent_labels.append(percent_label)

        # Buttons for simulating faults
        self.fault_button = tk.Button(master, text="Simulate Disk Fault", command=self.simulate_disk_fault)
        self.fault_button.grid(row=8, column=0)

        self.sector_fault_button = tk.Button(master, text="Simulate Sector Fault", command=self.simulate_sector_fault)
        self.sector_fault_button.grid(row=8, column=1)

        self.communication_fault_button = tk.Button(master, text="Simulate Communication Fault", command=self.simulate_communication_fault)
        self.communication_fault_button.grid(row=8, column=2)

        # Buttons for additional functionalities
        self.performance_test_button = tk.Button(master, text="Run Performance Test", command=lambda: self.run_performance_test(10000, 128))
        self.performance_test_button.grid(row=9, column=0)

        self.export_status_button = tk.Button(master, text="Export RAID Status", command=self.export_raid_status)
        self.export_status_button.grid(row=9, column=1)

        self.reset_button = tk.Button(master, text="Reset RAID", command=self.reset_raid)
        self.reset_button.grid(row=9, column=2)

        self.update_state()

    def select_raid(self, raid_type):
        """Select RAID array based on user choice."""
        if raid_type == "RAID0":
            self.current_raid = self.raid0
        elif raid_type == "RAID1":
            self.current_raid = self.raid1
        elif raid_type == "RAID3":
            self.current_raid = self.raid3

        self.update_state()

    def write_data(self):
        """Write data to the RAID array."""
        data = self.data_entry.get()
        if self.current_raid:
            self.current_raid.write(data)
            self.update_state()

    def read_data(self):
        """Read data from the RAID array."""
        index = self.data_entry.get()
        if self.current_raid and index.isdigit():
            result = self.current_raid.read(int(index))
            if result is not None:
                messagebox.showinfo("Read Result", f"Data at index {index}: {result}")
            else:
                messagebox.showerror("Read Error", "Failed to read data.")
        else:
            messagebox.showerror("Input Error", "Please enter a valid index.")

    def simulate_disk_fault(self):
        """Simulate a disk fault."""
        disk_id = self.data_entry.get()
        if self.current_raid and disk_id.isdigit():
            self.current_raid.simulate_fault(int(disk_id))
            self.update_state()

    def simulate_sector_fault(self):
        """Simulate a sector fault."""
        fault_info = self.data_entry.get().split(',')

        # Sprawdzamy, czy podano poprawny format danych (disk_id, sector_id)
        if len(fault_info) == 2 and all(x.strip().isdigit() for x in fault_info):
            disk_id, sector_id = map(int, fault_info)

            # Sprawdzamy, czy numer dysku mieści się w zakresie dostępnych dysków
            if 0 <= disk_id < len(self.current_raid.disks):
                # Sprawdzamy, czy numer sektora jest poprawny
                if 0 <= sector_id < self.current_raid.disk_size:
                    self.current_raid.simulate_sector_fault(disk_id, sector_id)
                    messagebox.showinfo("Sector Fault", f"Simulated fault at Disk {disk_id}, Sector {sector_id}")
                    self.update_state()
                else:
                    messagebox.showerror("Error", f"Invalid sector ID. Please enter a sector ID between 0 and {self.current_raid.disk_size - 1}.")
            else:
                messagebox.showerror("Error", f"Invalid disk ID. Please enter a disk ID between 0 and {len(self.current_raid.disks) - 1}.")
        else:
            messagebox.showerror("Input Error", "Please enter data in the format 'disk_id,sector_id' (e.g., '0,1').")

    def simulate_communication_fault(self):
        """Simulate a communication fault on a specific disk."""
        disk_id = self.data_entry.get().strip()  # Pobierz i usuń zbędne spacje
        if disk_id.isdigit():
            disk_id = int(disk_id)
            # Sprawdzamy, czy numer dysku mieści się w zakresie dostępnych dysków
            if 0 <= disk_id < len(self.current_raid.disks):
                self.current_raid.simulate_communication_fault(disk_id)
                messagebox.showinfo("Communication Fault", f"Simulated communication fault on Disk {disk_id}")
                self.update_state()
            else:
                messagebox.showerror("Error", f"Invalid disk ID. Please enter a disk ID between 0 and {len(self.current_raid.disks) - 1}.")
        else:
            messagebox.showerror("Input Error", "Please enter a valid disk ID (a number).")

    def update_state(self):
        """Update the state of the RAID array in the GUI."""
        if self.current_raid:
            total_size = self.current_raid.disk_size

            for i, disk in enumerate(self.current_raid.disks):
                # Update disk status (color depending on availability)
                if disk.available:
                    self.disk_labels[i].config(fg="green")
                else:
                    self.disk_labels[i].config(fg="red")

                # Calculate disk usage
                used_sectors = sum(1 for sector in disk.data if sector != '')
                usage_percentage = (used_sectors / total_size) * 100

                # Update progress bar for each disk
                self.disk_progress[i].config(value=usage_percentage)

                # Update the percent label
                self.disk_percent_labels[i].config(text=f"{usage_percentage:.1f}%")

            # Update text field showing detailed disk data
            self.state_text.delete(1.0, tk.END)
            for i, disk in enumerate(self.current_raid.disks):
                self.state_text.insert(tk.END, f"Disk {i} [Status: {'Available' if disk.available else 'Faulty'}]: {disk.data}\n")

    def run_performance_test(self, num_operations, data_size):
        """Run a performance test by writing and reading a large amount of data."""
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
            self.current_raid.read(i % len(test_data))  # Ensure we are reading valid sectors
        end_time = time.perf_counter()
        read_time = end_time - start_time

        # Log performance results
        report = {
            "RAID Type": self.raid_type_var.get(),
            "Number of Disks": self.current_raid.num_disks,
            "Disk Size": self.current_raid.disk_size,
            "Number of Operations": num_operations,
            "Data Size (bytes)": data_size,
            "Write Time (seconds)": write_time,
            "Read Time (seconds)": read_time
        }

        with open("performance_report.json", "w") as file:
            json.dump(report, file, indent=4)

        messagebox.showinfo("Test Completed", f"Write time: {write_time:.4f}s\nRead time: {read_time:.4f}s")

    def export_raid_status(self):
        """Export current RAID status to a JSON file."""
        if not self.current_raid:
            messagebox.showerror("Error", "No RAID array selected.")
            return

        raid_status = {
            "RAID Type": self.raid_type_var.get(),
            "Disks": []
        }

        for i, disk in enumerate(self.current_raid.disks):
            disk_info = {
                "Disk ID": i,
                "Available": disk.available,
                "Faulty Sectors": disk.faulty_sectors,
                "Communication Fault": disk.communication_fault,
                "Used Sectors": [sector for sector in disk.data if sector != '']
            }
            raid_status["Disks"].append(disk_info)

        with open("raid_status.json", "w") as file:
            json.dump(raid_status, file, indent=4)

        messagebox.showinfo("Export Completed", "RAID status has been exported to 'raid_status.json'.")

    def reset_raid(self):
        """Reset the RAID array to the initial state."""
        if self.current_raid:
            for disk in self.current_raid.disks:
                disk.data = [''] * disk.size
                disk.available = True
                disk.faulty_sectors = []
                disk.communication_fault = False
            self.update_state()
            messagebox.showinfo("RAID Reset", "RAID array has been reset to the initial state.")


if __name__ == "__main__":
    root = tk.Tk()
    app = RAIDMonitorApp(root)
    root.mainloop()
