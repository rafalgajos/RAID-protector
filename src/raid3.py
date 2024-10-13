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

        # Check if the sector on the main data disk is faulty
        if sector_index in self.disks[disk_index].faulty_sectors:
            print(f"RAID3 Read Error: Sector {sector_index} is faulty on disk {disk_index}.")
            return None

        # Check if the main disk is available
        if not self.disks[disk_index].available or self.disks[disk_index].communication_fault:
            print(f"Disk {disk_index} unavailable. Attempting to reconstruct data using parity...")

            # Reconstruction of data using XOR from remaining working disks and parity
            reconstructed_value = 0
            for i in range(self.num_disks - 1):  # Loop through all data disks
                if i != disk_index:
                    # Check if the other disk is functional
                    if self.disks[i].available and not self.disks[i].communication_fault:
                        value = self.disks[i].read(sector_index)
                        if value is None or value == '':  # Check if the value is empty or None
                            print(f"RAID3 Read Error: Sector {sector_index} on disk {i} is faulty or unreadable.")
                            return None
                        reconstructed_value ^= ord(value)  # XOR to reconstruct data
                    else:
                        print(f"RAID3 Read Error: Disk {i} unavailable for reconstruction.")
                        return None

            # Now we XOR with parity disk value to finalize reconstruction
            parity_value = self.disks[-1].read(sector_index)
            if parity_value is None or parity_value == '':  # Check if parity value is empty or None
                print(f"RAID3 Read Error: Parity disk sector {sector_index} is unreadable.")
                return None
            reconstructed_value ^= ord(parity_value)

            return chr(reconstructed_value)  # Return reconstructed data

        # If the disk is available and working, just read normally
        value = self.disks[disk_index].read(sector_index)
        if value is None or value == '':  # Check if value is None or empty
            print(f"RAID3 Read Error: Failed to read sector {sector_index} on disk {disk_index}.")
            return None
        return value

