from raid0 import RAID0
from raid1 import RAID1
from raid3 import RAID3


def test_raid():
    # Test RAID0
    print("Testing RAID0...")
    raid0 = RAID0(3, 10)
    raid0.write("abcdefghij")
    print(raid0.read(0))  # Should read ‘a’

    # Test RAID1
    print("\nTesting RAID1...")
    raid1 = RAID1(2, 10)
    raid1.write("abcdefghij")
    print(raid1.read(0))  # Should read ‘a’

    # Test RAID3
    print("\nTesting RAID3...")
    raid3 = RAID3(3, 10)
    raid3.write("abcdefghij")
    print(raid3.read(0))  # Should read ‘a’


if __name__ == "__main__":
    test_raid()
