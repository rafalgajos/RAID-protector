from src.disk import Disk


class RAIDBase:
    def __init__(self, num_disks, disk_size):
        self.disks = [Disk(disk_size) for _ in range(num_disks)]
        self.disk_size = disk_size
        self.num_disks = num_disks

    def write(self, data):
        """Data storage interface - to be implemented in derived classes."""
        raise NotImplementedError

    def read(self, index):
        """Data reading interface - to be implemented in derived classes."""
        raise NotImplementedError

    def simulate_fault(self, disk_id):
        """Disk failure simulation."""
        if 0 <= disk_id < self.num_disks:
            self.disks[disk_id].available = False
            print(f"Disk {disk_id} is now unavailable (fault injected).")
        else:
            print(f"Fault Error: Disk {disk_id} does not exist.")

    def simulate_sector_fault(self, disk_id, sector_id):
        """Simulates a faulty sector on a specific disk."""
        if 0 <= disk_id < self.num_disks:
            self.disks[disk_id].simulate_sector_fault(sector_id)
        else:
            print(f"Fault Error: Disk {disk_id} does not exist.")

    def simulate_communication_fault(self, disk_id):
        """Simulates a communication fault on a specific disk."""
        if 0 <= disk_id < self.num_disks:
            self.disks[disk_id].simulate_communication_fault()
        else:
            print(f"Fault Error: Disk {disk_id} does not exist.")
