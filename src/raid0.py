from src.raid_base import RAIDBase


class RAID0(RAIDBase):
    def __init__(self, num_disks, disk_size):
        super().__init__(num_disks, disk_size)

    def write(self, data):
        """Writes data to the disks in RAID0 (striping) mode."""
        for i, value in enumerate(data):
            disk_index = i % self.num_disks
            sector_index = i // self.num_disks
            self.disks[disk_index].write(sector_index, value)
            print(f"Writing {value} to disk {disk_index} at sector {sector_index}")

    def read(self, index):
        """Reads data from disks in RAID0 (striping) mode."""
        disk_index = index % self.num_disks
        sector_index = index // self.num_disks
        return self.disks[disk_index].read(sector_index)
