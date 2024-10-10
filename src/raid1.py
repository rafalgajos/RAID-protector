from raid_base import RAIDBase


class RAID1(RAIDBase):
    def __init__(self, num_disks, disk_size):
        if num_disks < 2:
            raise ValueError("RAID1 requires at least 2 disks.")
        super().__init__(num_disks, disk_size)

    def write(self, data):
        """Saves data on all drives in RAID1 (mirroring) mode."""
        for i in range(len(data)):
            for disk in self.disks:
                disk.write(i, data[i])
                print(f"Writing {data[i]} to disk {self.disks.index(disk)} at sector {i}")

    def read(self, index):
        """Reads data from the first available drive in RAID1 mode."""
        for disk in self.disks:
            if disk.available:
                return disk.read(index)
        print("Read Error: No available disks in RAID1 array.")
        return None
