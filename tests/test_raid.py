import unittest
from src.raid0 import RAID0
from src.raid1 import RAID1
from src.raid3 import RAID3


class TestRAID(unittest.TestCase):
    def setUp(self):
        self.raid0 = RAID0(3, 10)
        self.raid1 = RAID1(2, 10)
        self.raid3 = RAID3(3, 10)

    def test_raid0_write_read(self):
        self.raid0.write("abcdefghij")
        self.assertEqual(self.raid0.read(0), 'a')
        self.assertEqual(self.raid0.read(4), 'e')

    def test_raid1_write_read(self):
        self.raid1.write("abcdefghij")
        self.assertEqual(self.raid1.read(0), 'a')
        self.assertEqual(self.raid1.read(5), 'f')

    def test_raid3_write_read(self):
        self.raid3.write("abcdefghij")
        self.assertEqual(self.raid3.read(0), 'a')
        self.assertEqual(self.raid3.read(7), 'h')


if __name__ == "__main__":
    unittest.main()
