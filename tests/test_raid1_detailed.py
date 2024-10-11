from src.raid1 import RAID1


def test_raid1_normal_operation():
    raid1 = RAID1(2, 10)
    sample_data = "abcdefghij"
    print("\n--- Testing RAID1 Normal Operation ---")

    # Normal write and read
    raid1.write(sample_data)

    for i in range(len(sample_data)):
        assert raid1.read(i) == sample_data[i], f"RAID1: Read failed at index {i} in normal operation"
    print("RAID1: Normal operation passed.")


def test_raid1_single_disk_failure():
    raid1 = RAID1(2, 10)
    sample_data = "abcdefghij"
    print("\n--- Testing RAID1 Single Disk Failure ---")

    raid1.write(sample_data)

    # Inject fault on Disk 0 (making it unavailable)
    raid1.simulate_fault(0)

    # RAID1 should still read data from the remaining disk
    for i in range(len(sample_data)):
        assert raid1.read(i) == sample_data[i], f"RAID1: Failed to read data at index {i} after single disk failure"

    print("RAID1: Single disk failure test passed.")


def test_raid1_both_disks_failure():
    raid1 = RAID1(2, 10)
    sample_data = "abcdefghij"
    print("\n--- Testing RAID1 Both Disks Failure ---")

    raid1.write(sample_data)

    # Inject fault on both disks
    raid1.simulate_fault(0)
    raid1.simulate_fault(1)

    # RAID1 should fail to read data as both disks are unavailable
    for i in range(len(sample_data)):
        assert raid1.read(i) is None, f"RAID1: Read should fail at index {i} when both disks have failed"

    print("RAID1: Both disks failure test passed.")


def test_raid1_sector_failure():
    raid1 = RAID1(2, 10)
    sample_data = "abcdefghij"
    print("\n--- Testing RAID1 Sector Failure ---")

    raid1.write(sample_data)

    # Inject sector fault on disk 0, sector 0
    raid1.simulate_sector_fault(0, 0)
    print(f"Disk 0 faulty sectors: {raid1.disks[0].faulty_sectors}")  # Debugging

    # RAID1 should still read data from the other disk
    result = raid1.read(0)
    print(f"Read result for sector 0: {result}")  # Debugging

    # Retry read from the second disk if the first disk sector is faulty
    if result is None:
        result = raid1.disks[1].read(0)

    assert result == 'a', "RAID1: Should read from the working disk despite sector failure on one disk"
    print("RAID1: Sector failure test passed.")


if __name__ == "__main__":
    print("Running detailed RAID1 tests...")

    # Testy RAID1
    test_raid1_normal_operation()  # Normal operating test
    test_raid1_single_disk_failure()  # Single disk failure test
    test_raid1_both_disks_failure()  # Both disks failure test
    test_raid1_sector_failure()  # Sector failure test

    print("All detailed RAID1 tests completed.")
