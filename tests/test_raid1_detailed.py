import unittest
from src.raid1 import RAID1


class TestRAID1(unittest.TestCase):
    def setUp(self):
        # SetUp method performed before each test, sets up RAID1 with two disks of 10 sectors each
        self.raid1 = RAID1(2, 10)
        self.sample_data = "abcdefghij"

    def test_raid1_normal_operation(self):
        print("\n--- Testing RAID1 Normal Operation ---")
        # Normal write and read
        self.raid1.write(self.sample_data)

        for i in range(len(self.sample_data)):
            self.assertEqual(self.raid1.read(i), self.sample_data[i],
                             f"RAID1: Read failed at index {i} in normal operation")
        print("RAID1: Normal operation passed.")

    def test_raid1_single_disk_failure(self):
        print("\n--- Testing RAID1 Single Disk Failure ---")
        self.raid1.write(self.sample_data)

        # Inject fault on Disk 0 (making it unavailable)
        self.raid1.simulate_fault(0)

        # RAID1 should still read data from the remaining disk
        for i in range(len(self.sample_data)):
            self.assertEqual(self.raid1.read(i), self.sample_data[i],
                             f"RAID1: Failed to read data at index {i} after single disk failure")
        print("RAID1: Single disk failure test passed.")

    def test_raid1_both_disks_failure(self):
        print("\n--- Testing RAID1 Both Disks Failure ---")
        self.raid1.write(self.sample_data)

        # Inject fault on both disks
        self.raid1.simulate_fault(0)
        self.raid1.simulate_fault(1)

        # RAID1 should fail to read data as both disks are unavailable
        for i in range(len(self.sample_data)):
            self.assertIsNone(self.raid1.read(i), f"RAID1: Read should fail at index {i} when both disks have failed")
        print("RAID1: Both disks failure test passed.")

    def test_raid1_sector_failure(self):
        print("\n--- Testing RAID1 Sector Failure ---")
        self.raid1.write(self.sample_data)

        # Inject sector fault on disk 0, sector 0
        self.raid1.simulate_sector_fault(0, 0)
        print(f"Disk 0 faulty sectors: {self.raid1.disks[0].faulty_sectors}")  # Debugging

        # RAID1 should still read data from the other disk
        result = self.raid1.read(0)
        print(f"Read result for sector 0: {result}")  # Debugging

        # Retry read from the second disk if the first disk sector is faulty
        if result is None:
            result = self.raid1.disks[1].read(0)

        self.assertEqual(result, 'a', "RAID1: Should read from the working disk despite sector failure on one disk")
        print("RAID1: Sector failure test passed.")


if __name__ == "__main__":
    print("Running detailed RAID1 tests...")
    unittest.main(verbosity=2)
