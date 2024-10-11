from raid0 import RAID0
from raid1 import RAID1
from raid3 import RAID3


def main():
    print("Initializing RAID arrays for testing...")
    raid0 = RAID0(3, 10)
    raid1 = RAID1(2, 10)
    raid3 = RAID3(3, 10)

    # Sample data to test writing
    sample_data = "abcdefghij"

    print("\n--- Testing RAID0 ---")
    raid0.write(sample_data)
    print(f"RAID0 Read Index 0: {raid0.read(0)}")  # Should read 'a'

    print("\n--- Testing RAID1 ---")
    raid1.write(sample_data)
    print(f"RAID1 Read Index 0: {raid1.read(0)}")  # Should read 'a'

    print("\n--- Testing RAID3 ---")
    raid3.write(sample_data)
    print(f"RAID3 Read Index 0: {raid3.read(0)}")  # Should read 'a'


if __name__ == "__main__":
    main()
