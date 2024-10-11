class Disk:
    def __init__(self, size):
        self.size = size
        self.data = [''] * size  # Empty sector list
        self.available = True  # Disk availability flag
        self.faulty_sectors = []  # List of faulty sectors
        self.communication_fault = False  # Communication fault flag

    def write(self, index, value):
        """Writes data to the sector with the given index."""
        if self.available and not self.communication_fault:
            if index in self.faulty_sectors:
                print(f"Write Error: Sector {index} is faulty on disk.")
            elif 0 <= index < self.size:
                self.data[index] = value
            else:
                print(f"Write Error: Index {index} out of bounds.")
        else:
            print(f"Write Error: Disk unavailable or communication fault.")

    def read(self, index):
        """Reads data from a sector with a given index."""
        if self.available and not self.communication_fault:
            if index in self.faulty_sectors:
                print(f"Read Error: Sector {index} is faulty on disk.")
                return None  # Reading from a bad sector
            elif 0 <= index < self.size:
                return self.data[index]
            else:
                print(f"Read Error: Index {index} out of bounds.")
                return None
        else:
            print(f"Read Error: Disk unavailable or communication fault.")
            return None

    def simulate_sector_fault(self, index):
        """Simulates a faulty sector on the disk."""
        if 0 <= index < self.size:
            self.faulty_sectors.append(index)
            print(f"Sector {index} on disk marked as faulty.")
        else:
            print(f"Fault Error: Index {index} out of bounds.")

    def simulate_communication_fault(self):
        """Simulates a communication fault on the disk."""
        self.communication_fault = True
        print("Communication fault simulated on disk.")

    def reset_communication_fault(self):
        """Resets the communication fault on the disk."""
        self.communication_fault = False
        print("Communication fault reset on disk.")
