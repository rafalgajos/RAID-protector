import unittest
from src.disk import Disk


class TestDisk(unittest.TestCase):
    def setUp(self):
        self.disk = Disk(10)

    def test_write_read_normal_operation(self):
        print("\n--- Testing Disk Write and Read Normal Operation ---")
        self.disk.write(0, 'a')
        self.disk.write(1, 'b')
        self.assertEqual(self.disk.read(0), 'a', "Failed to read value 'a' from sector 0.")
        self.assertEqual(self.disk.read(1), 'b', "Failed to read value 'b' from sector 1.")
        print("Disk: Normal write and read operations passed.")

    def test_write_out_of_bounds(self):
        print("\n--- Testing Write Out of Bounds ---")
        self.disk.write(10, 'z')  # Index out of bounds
        self.assertNotEqual(self.disk.read(10), 'z', "Should not be able to write to an out of bounds index.")
        print("Disk: Write out of bounds handled correctly.")

    def test_read_out_of_bounds(self):
        print("\n--- Testing Read Out of Bounds ---")
        result = self.disk.read(10)  # Index out of bounds
        self.assertIsNone(result, "Reading out of bounds should return None.")
        print("Disk: Read out of bounds handled correctly.")

    def test_sector_fault(self):
        print("\n--- Testing Sector Fault ---")
        self.disk.simulate_sector_fault(0)
        self.disk.write(0, 'a')  # Should fail to write
        result = self.disk.read(0)  # Should return None
        self.assertIsNone(result, "Reading from a faulty sector should return None.")
        print("Disk: Sector fault handled correctly.")

    def test_communication_fault(self):
        print("\n--- Testing Communication Fault ---")
        self.disk.simulate_communication_fault()
        self.disk.write(1, 'b')  # Should fail to write due to communication fault
        result = self.disk.read(1)  # Should return None
        self.assertIsNone(result, "Reading with communication fault should return None.")
        self.disk.reset_communication_fault()
        self.disk.write(1, 'b')  # Should succeed now
        self.assertEqual(self.disk.read(1), 'b', "Failed to write/read after resetting communication fault.")
        print("Disk: Communication fault handled correctly.")

    def test_multiple_sector_faults(self):
        print("\n--- Testing Multiple Sector Faults ---")
        self.disk.simulate_sector_fault(0)
        self.disk.simulate_sector_fault(1)
        self.disk.write(0, 'a')  # Should fail to write to sector 0
        self.disk.write(1, 'b')  # Should fail to write to sector 1
        result_0 = self.disk.read(0)
        result_1 = self.disk.read(1)
        self.assertIsNone(result_0, "Reading from a faulty sector 0 should return None.")
        self.assertIsNone(result_1, "Reading from a faulty sector 1 should return None.")
        print("Disk: Multiple sector faults handled correctly.")


if __name__ == "__main__":
    print("Running Disk class tests...")
    unittest.main()
