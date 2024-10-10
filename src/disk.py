class Disk:
    def __init__(self, size):
        # Initialisation of disk with specified size (in sectors)
        self.size = size
        self.data = [''] * size  # Empty sector list
        self.available = True  # Disk availability flag# Disk availability flag

    def write(self, index, value):
        """Writes data to the sector with the given index."""
        if self.available and 0 <= index < self.size:
            self.data[index] = value
        else:
            print(f"Write Error: Disk unavailable or index {index} out of bounds")

    def read(self, index):
        """Reads data from a sector with a given index."""
        if self.available and 0 <= index < self.size:
            return self.data[index]
        else:
            print(f"Read Error: Disk unavailable or index {index} out of bounds")
            return None
