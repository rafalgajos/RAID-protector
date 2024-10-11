from src.raid0 import RAID0


def test_raid0_normal_operation():
    raid0 = RAID0(3, 10)
    sample_data = "abcdefghij"
    print("\n--- Testing RAID0 Normal Operation ---")

    # Normal write and read
    raid0.write(sample_data)

    for i in range(len(sample_data)):
        assert raid0.read(i) == sample_data[i], f"RAID0: Read failed at index {i} in normal operation"
    print("RAID0: Normal operation passed.")


def test_raid0_disk_failure():
    raid0 = RAID0(3, 10)
    sample_data = "abcdefghij"
    print("\n--- Testing RAID0 Disk Failure ---")

    raid0.write(sample_data)

    # Inject fault on Disk 1 (making it unavailable)
    raid0.simulate_fault(1)

    # RAID0 should fail to read data from Disk 1
    for i in range(1, len(sample_data), 3):
        assert raid0.read(i) is None, f"RAID0: Failed to handle disk failure for index {i}"

    print("RAID0: Disk failure test passed.")


def test_raid0_sector_failure():
    raid0 = RAID0(3, 10)
    sample_data = "abcdefghij"
    print("\n--- Testing RAID0 Sector Failure ---")

    raid0.write(sample_data)

    # Inject sector fault on disk 0, sector 0
    raid0.simulate_sector_fault(0, 0)
    print(f"Disk 0 faulty sectors: {raid0.disks[0].faulty_sectors}")  # Debugging

    # Expecting a read from the bad sector to return an error
    result = raid0.read(0)
    print(f"Read result for sector 0 on disk 0: {result}")  # Debugging
    assert result is None, "RAID0: Sector fault should cause read failure"
    print("RAID0: Sector failure passed.")


if __name__ == "__main__":
    print("Running detailed RAID0 tests...")

    # Testy RAID0
    test_raid0_normal_operation()       # Normal operating test
    test_raid0_disk_failure()           # Failure test of one working disk
    test_raid0_sector_failure()         # Sector failure test

    print("All detailed RAID0 tests completed.")
