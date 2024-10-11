import unittest
from src.raid3 import RAID3


class TestRAID3(unittest.TestCase):
    def setUp(self):
        # Configuration performed before each test
        self.raid3 = RAID3(3, 10)
        self.sample_data = "abcdefghij"

    def test_normal_operation(self):
        print("\n--- Testing RAID3 Normal Operation ---")
        self.raid3.write(self.sample_data)

        # Normal reading of data
        for i in range(len(self.sample_data)):
            self.assertEqual(self.raid3.read(i), self.sample_data[i],
                             f"RAID3: Read failed at index {i} in normal operation")
        print("RAID3: Normal operation passed.")

    def test_disk_failure(self):
        print("\n--- Testing RAID3 Disk Failure ---")
        self.raid3.write(self.sample_data)

        # Simulation of disk failure 0 (data disk)
        self.raid3.simulate_fault(0)

        # Checking if data is being recreated via parity
        for i in range(0, len(self.sample_data), 2):  # Reading from faulty discs
            self.assertEqual(self.raid3.read(i), self.sample_data[i],
                             f"RAID3: Failed to reconstruct data for index {i} after Disk 0 failure")
        print("RAID3: Disk failure recovery passed.")

    def test_parity_disk_failure(self):
        print("\n--- Testing RAID3 Parity Disk Failure ---")
        self.raid3.write(self.sample_data)

        # Simulation of communication failure on parity disk (Disk 2)
        self.raid3.simulate_communication_fault(2)

        # RAID3 should continue to read data from working disks despite parity failure
        for i in range(len(self.sample_data)):
            self.assertEqual(self.raid3.read(i), self.sample_data[i],
                             f"RAID3: Failed to read data at index {i} with parity disk failure")
        print("RAID3: Parity disk failure recovery passed.")

    def test_sector_failure(self):
        print("\n--- Testing RAID3 Sector Failure ---")
        self.raid3.write(self.sample_data)

        # Simulation of sector failure on disk 0, sector 0
        self.raid3.simulate_sector_fault(0, 0)

        # Expect reading from faulty sector to return error (None)
        result = self.raid3.read(0)
        self.assertIsNone(result, "RAID3: Sector fault should cause read failure")
        print("RAID3: Sector failure passed.")

    def test_combined_failures(self):
        print("\n--- Testing RAID3 Combined Failures ---")
        self.raid3.write(self.sample_data)

        # Simulating failure of disk 0 (data disk) and failure of communication with the parity disk (disk 2)
        self.raid3.simulate_fault(0)
        self.raid3.simulate_communication_fault(2)

        # RAID3 should not be able to read data from disk 0 because it lacks parity access
        self.assertIsNone(self.raid3.read(0),
                          "RAID3: Should fail to read with data disk failure and parity disk communication fault")
        print("RAID3: Combined failures test passed.")


if __name__ == "__main__":
    print("Running detailed RAID3 tests...")
    unittest.main()
    print("All detailed RAID3 tests completed.")
