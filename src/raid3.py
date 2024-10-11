from src.raid_base import RAIDBase


class RAID3(RAIDBase):
    def __init__(self, num_disks, disk_size):
        if num_disks < 3:
            raise ValueError("RAID3 requires at least 3 disks (2 data + 1 parity).")
        super().__init__(num_disks, disk_size)

    def write(self, data):
        """Writes data with parity in RAID3 mode."""
        sector_index = -1  # Default value to prevent uninitialized usage
        for i in range(0, len(data), self.num_disks - 1):
            data_block = data[i:i + (self.num_disks - 1)]
            parity = 0
            for value in data_block:
                parity ^= ord(value)  # Simple parity XOR
            for j, value in enumerate(data_block):
                sector_index = i // (self.num_disks - 1)
                # Checking if a sector is corrupted before writing
                if sector_index in self.disks[j].faulty_sectors:
                    print(f"Write Error: Sector {sector_index} is faulty on disk {j}, skipping write.")
                    continue
                self.disks[j].write(sector_index, value)
                print(f"Writing {value} to disk {j} at sector {sector_index}")
            # Parity recording unless sector is faulty
            if sector_index not in self.disks[-1].faulty_sectors:
                self.disks[-1].write(sector_index, chr(parity))  # Parity recording
                print(f"Writing parity {hex(parity)} to disk {self.num_disks - 1}")
            else:
                print(f"Write Error: Sector {sector_index} is faulty on parity disk, skipping parity write.")

    def read(self, index):
        """Reads data in RAID3 mode with parity consideration."""
        disk_index = index % (self.num_disks - 1)  # We calculate the index of the data drive
        sector_index = index // (self.num_disks - 1)

        # Checking if a sector on the data drive is damaged before any operation
        if sector_index in self.disks[disk_index].faulty_sectors:
            print(f"RAID3 Read Error: Sector {sector_index} is faulty on disk {disk_index}.")
            return None  # Returns None immediately if sector is corrupted

        # Check if the working disk is available
        if not self.disks[disk_index].available:
            print(f"Disk {disk_index} unavailable. Attempting to reconstruct data using parity...")

            # Reconstruction of data using XOR from remaining working discs
            reconstructed_value = 0
            for i in range(self.num_disks - 1):
                if i != disk_index:
                    # Check for sector failures on other drives
                    if sector_index in self.disks[i].faulty_sectors:
                        print(f"RAID3 Read Error: Sector {sector_index} is faulty on disk {i}.")
                        return None  # Reading failed due to bad sector
                    value = self.disks[i].read(sector_index)
                    if value is None:
                        return None  # If other disks have a problem, reading fails
                    reconstructed_value ^= ord(value)

            # Reading parity and including it in the reconstruction
            parity_value = self.disks[-1].read(sector_index)
            if parity_value is None:
                return None  # Parity unavailable, reading failed
            reconstructed_value ^= ord(parity_value)

            return chr(reconstructed_value)

        # Normal reading from the working disk
        value = self.disks[disk_index].read(sector_index)

        # If reading from a normal disk returns None or the sector is corrupted, we return None
        if value is None or sector_index in self.disks[disk_index].faulty_sectors:
            print(f"RAID3 Read Error: Failed to read sector {sector_index} on disk {disk_index}.")
            return None

        return value
