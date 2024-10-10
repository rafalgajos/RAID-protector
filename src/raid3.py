from raid_base import RAIDBase


class RAID3(RAIDBase):
    def __init__(self, num_disks, disk_size):
        if num_disks < 3:
            raise ValueError("RAID3 requires at least 3 disks (2 data + 1 parity).")
        super().__init__(num_disks, disk_size)

    def write(self, data):
        """Writes data with parity in RAID3 mode."""
        for i in range(0, len(data), self.num_disks - 1):
            # Data block division for RAID3
            data_block = data[i:i + (self.num_disks - 1)]
            parity = 0
            for value in data_block:
                parity ^= ord(value)  # Simple parity XOR
            for j, value in enumerate(data_block):
                self.disks[j].write(i // (self.num_disks - 1), value)
                print(f"Writing {value} to disk {j} at sector {i // (self.num_disks - 1)}")
            self.disks[-1].write(i // (self.num_disks - 1), chr(parity))  # Parity recording
            # print(f"Writing parity {chr(parity)} to disk {self.num_disks - 1}")
            parity = hex(parity)
            print(f"Writing parity {parity} to disk {self.num_disks - 1}")

    def read(self, index):
        """Reads data in RAID3 mode with parity consideration."""
        disk_index = index % (self.num_disks - 1)
        sector_index = index // (self.num_disks - 1)
        return self.disks[disk_index].read(sector_index)
