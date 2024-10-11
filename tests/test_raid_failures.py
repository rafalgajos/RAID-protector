from src.raid0 import RAID0
from src.raid1 import RAID1
from src.raid3 import RAID3
from src.disk import Disk


def test_raid0_faults():
    raid0 = RAID0(3, 10)
    sample_data = "abcdefghij"
    print("\n--- Testing RAID0 Fault Injection ---")

    # Normal write and read
    raid0.write(sample_data)
    assert raid0.read(0) == 'a', "RAID0: Read before fault failed"

    # Inject disk fault (making disk 1 unavailable)
    print("\nInjecting fault on Disk 1 in RAID0...")
    raid0.simulate_fault(1)
    assert raid0.read(1) is None, "RAID0: Faulted disk should not return data"

    # Inject sector fault on disk 0, sector 0
    print("\nInjecting sector fault on Disk 0, Sector 0 in RAID0...")
    raid0.simulate_sector_fault(0, 0)
    assert raid0.read(0) is None, "RAID0: Faulty sector should not return data"

    # Inject communication fault on disk 2
    print("\nInjecting communication fault on Disk 2 in RAID0...")
    raid0.simulate_communication_fault(2)
    assert raid0.read(2) is None, "RAID0: Disk with communication fault should not return data"


def test_raid1_faults():
    raid1 = RAID1(2, 10)
    sample_data = "abcdefghij"
    print("\n--- Testing RAID1 Fault Injection ---")

    # Normal write and read
    raid1.write(sample_data)
    assert raid1.read(0) == 'a', "RAID1: Read before fault failed"

    # Inject disk fault (making disk 0 unavailable)
    print("\nInjecting fault on Disk 0 in RAID1...")
    raid1.simulate_fault(0)
    assert raid1.read(0) == 'a', "RAID1: Read should still work after one disk fault"

    # Inject disk fault on all disks (RAID1 should fail now)
    print("\nInjecting fault on Disk 1 in RAID1...")
    raid1.simulate_fault(1)
    assert raid1.read(0) is None, "RAID1: No disks available, read should fail"


def test_raid3_faults():
    raid3 = RAID3(3, 10)
    sample_data = "abcdefghij"
    print("\n--- Testing RAID3 Fault Injection ---")

    # Normal write and read
    raid3.write(sample_data)
    assert raid3.read(0) == 'a', "RAID3: Read before fault failed"

    # Inject disk fault (data disk)
    print("\nInjecting fault on Disk 0 in RAID3...")
    raid3.simulate_fault(0)

    # We expect the data to be reconstructed with parity
    assert raid3.read(0) == 'a', "RAID3: Failed to reconstruct data after Disk 0 fault"

    # Inject sector fault on disk 1, sector 0
    print("\nInjecting sector fault on Disk 1, Sector 0 in RAID3...")
    raid3.simulate_sector_fault(1, 0)
    assert raid3.read(1) is None, "RAID3: Faulty sector should not return data"

    # Inject communication fault on parity disk
    print("\nInjecting communication fault on Parity Disk in RAID3...")
    raid3.simulate_communication_fault(2)

    # At this point we have a disk 0 failure and a parity disk communication error,
    # and a bad sector on disk 1 - RAID3 should not be able to read the data.
    assert raid3.read(0) is None, "RAID3: Should fail to read with faulty disk and parity disk communication fault"


def test_sector_fault_simulation():
    disk = Disk(10)  # Create a disk of 10 sectors
    disk.simulate_sector_fault(1)  # Damage to sector 1
    assert 1 in disk.faulty_sectors, "Sector 1 should be marked as damaged."
    print("Sector fault simulation test passed.")


if __name__ == "__main__":
    print("Running RAID fault injection tests...")

    test_sector_fault_simulation()

    # Testing RAID0
    test_raid0_faults()

    # Testing RAID1
    test_raid1_faults()

    # Testing RAID3
    test_raid3_faults()

    print("All RAID fault injection tests completed.")
