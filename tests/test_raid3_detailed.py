from src.raid3 import RAID3


def test_raid3_normal_operation():
    raid3 = RAID3(3, 10)
    sample_data = "abcdefghij"
    print("\n--- Testing RAID3 Normal Operation ---")

    # Normal write and read
    raid3.write(sample_data)

    for i in range(len(sample_data)):
        assert raid3.read(i) == sample_data[i], f"RAID3: Read failed at index {i} in normal operation"
    print("RAID3: Normal operation passed.")


def test_raid3_disk_failure():
    raid3 = RAID3(3, 10)
    sample_data = "abcdefghij"
    print("\n--- Testing RAID3 Disk Failure ---")

    raid3.write(sample_data)

    # Inject fault on Disk 0 (data disk)
    raid3.simulate_fault(0)

    # Checking if the data is restored by parity
    for i in range(0, len(sample_data), 2):  # Reading from affected disks
        assert raid3.read(i) == sample_data[i], f"RAID3: Failed to reconstruct data for index {i} after Disk 0 failure"

    print("RAID3: Disk failure recovery passed.")


def test_raid3_parity_disk_failure():
    raid3 = RAID3(3, 10)
    sample_data = "abcdefghij"
    print("\n--- Testing RAID3 Parity Disk Failure ---")

    raid3.write(sample_data)

    # Inject communication fault on Parity Disk (Disk 2)
    raid3.simulate_communication_fault(2)

    # RAID3 should still read data from the working disks despite parity failure
    for i in range(len(sample_data)):
        assert raid3.read(i) == sample_data[i], f"RAID3: Failed to read data at index {i} with parity disk failure"

    print("RAID3: Parity disk failure recovery passed.")


def test_raid3_sector_failure():
    raid3 = RAID3(3, 10)
    sample_data = "abcdefghij"
    print("\n--- Testing RAID3 Sector Failure ---")

    raid3.write(sample_data)

    # Simulation of sector failure on disk 0, sector 0
    raid3.simulate_sector_fault(0, 0)
    print(f"Disk 0 faulty sectors: {raid3.disks[0].faulty_sectors}")  # Debugging

    # Expecting a read from the bad sector to return an error
    result = raid3.read(0)
    print(f"Read result for sector 0 on disk 0: {result}")  # Debugging
    assert result is None, "RAID3: Sector fault should cause read failure"
    print("RAID3: Sector failure passed.")


def test_raid3_combined_failures():
    raid3 = RAID3(3, 10)
    sample_data = "abcdefghij"
    print("\n--- Testing RAID3 Combined Failures ---")

    raid3.write(sample_data)

    # Inject fault on Disk 0 (data disk) and communication fault on parity disk (Disk 2)
    raid3.simulate_fault(0)
    raid3.simulate_communication_fault(2)

    # RAID3 should now be unable to read data from drive 0 as it has no parity access
    assert raid3.read(
        0) is None, "RAID3: Should fail to read with data disk failure and parity disk communication fault"

    print("RAID3: Combined failures test passed.")


if __name__ == "__main__":
    print("Running detailed RAID3 tests...")

    # Testy RAID3
    test_raid3_normal_operation()       # Normal operating test
    test_raid3_disk_failure()           # Failure test of one working disk
    test_raid3_parity_disk_failure()    # Parity disk failure test
    test_raid3_sector_failure()         # Sector failure test
    test_raid3_combined_failures()      # Combined fault test (working disk + parity disk)

    print("All detailed RAID3 tests completed.")
