import unittest
from src.raid0 import RAID0


class TestRAID0(unittest.TestCase):
    def setUp(self):
        # Set up RAID0 instance for each test
        self.raid0 = RAID0(3, 10)
        self.sample_data = "abcdefghij"

    def test_raid0_normal_operation(self):
        print("\n--- Testing RAID0 Normal Operation ---")
        # Normal write and read
        self.raid0.write(self.sample_data)

        for i in range(len(self.sample_data)):
            self.assertEqual(
                self.raid0.read(i), 
                self.sample_data[i], 
                f"RAID0: Read failed at index {i} in normal operation"
            )
        print("RAID0: Normal operation passed.")

    def test_raid0_disk_failure(self):
        print("\n--- Testing RAID0 Disk Failure ---")
        self.raid0.write(self.sample_data)

        # Inject fault on Disk 1 (making it unavailable)
        self.raid0.simulate_fault(1)

        # RAID0 should fail to read data from Disk 1
        for i in range(1, len(self.sample_data), 3):
            self.assertIsNone(
                self.raid0.read(i),
                f"RAID0: Failed to handle disk failure for index {i}"
            )
        print("RAID0: Disk failure test passed.")

    def test_raid0_sector_failure(self):
        print("\n--- Testing RAID0 Sector Failure ---")
        self.raid0.write(self.sample_data)

        # Inject sector fault on disk 0, sector 0
        self.raid0.simulate_sector_fault(0, 0)

        # Expecting a read from the bad sector to return an error
        result = self.raid0.read(0)
        self.assertIsNone(result, "RAID0: Sector fault should cause read failure")
        print("RAID0: Sector failure test passed.")


if __name__ == "__main__":
    print("Running detailed RAID0 tests...")
    unittest.main()
