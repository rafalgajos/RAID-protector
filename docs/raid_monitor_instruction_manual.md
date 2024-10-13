## [English Version]

# RAID Monitor Application User Manual

The "RAID Monitor" application is a tool designed to monitor and manage RAID 0, RAID 1, and RAID 3 arrays. The following manual provides step-by-step instructions on how to use the available features.

### 1. Selecting RAID Type

**Example:**

1. Open the application.
2. From the drop-down menu, select **RAID0**.
   - After selecting RAID0, the application will display information about the state of each disk in the RAID0 array (e.g., sector usage, disk availability).
3. You can now work with RAID0. If you want to change the RAID type, simply choose a different one (e.g., RAID1 or RAID3) from the drop-down menu.

### 2. Entering and Writing Data

**Example:**

1. In the text field (below the drop-down menu), enter data, e.g., **"Test data for RAID"**.
2. Click the **"Write Data"** button.
   - The data will be written to the RAID array. Depending on the selected RAID type (RAID0, RAID1, RAID3), the data will be distributed across the disks according to the RAID logic.
3. The disk status monitor will update to reflect the sectors used on the disks. For example, if you select RAID1, the data will be mirrored across two disks.

**Example for RAID1:**

- Enter the data **"Important files"**.
- RAID1 will store this data on two separate disks, ensuring redundancy.

### 3. Reading Data

**Example:**

1. Enter the sector index from which you want to read the data, e.g., **"0"** (if the data is stored in sector 0).
2. Click the **"Read Data"** button.
   - The application will read the data from the selected sector and display it in a pop-up window.

**Example with an invalid index:**

- If you enter an invalid index, e.g., **"100"**, and the data is only stored in the first few sectors, the application will display an error message indicating that it couldn't read the data from that sector.

### 4. Simulating Faults

#### 4.1 Simulating a Disk Fault

**Example:**

1. Enter the disk number you want to fail, e.g., **"1"** (disk 1).
2. Click the **"Simulate Disk Fault"** button.
   - The selected disk will be marked as failed, and the disk status in the monitor will be updated. The disk will now be displayed in red, and its usage will stop.
   - If using RAID1 or RAID3, the data may still be accessible from other disks even after a failure.

**Example for RAID1:**

- RAID1 has redundancy, so even after a disk failure, the data will remain accessible on the second disk.

#### 4.2 Simulating a Sector Fault

**Example:**

1. Enter the data in the format **"disk_id, sector_id"**, e.g., **"0,1"** (which represents sector 1 on disk 0).
2. Click the **"Simulate Sector Fault"** button.
   - The application will simulate a fault in the specified sector, and the fault information will be reflected in the disk status monitor.

**Example with an invalid sector:**

- If you enter incorrect data, e.g., **"4,1"** (where disk 4 doesn't exist), the application will show an error message indicating the invalid disk number.

#### 4.3 Simulating a Communication Fault

**Example:**

1. Enter the disk number that will experience communication issues, e.g., **"2"**.
2. Click the **"Simulate Communication Fault"** button.
   - The application will simulate a communication fault with the selected disk, and the disk status will be updated accordingly.

### 5. Performance Test

**Example:**

1. Click the **"Run Performance Test"** button.
2. The application will perform a series of data write and read operations (10000 operations with data size of 128 bytes).
3. After the test is complete, a pop-up window will show the time required for the test. The test results will be saved in the file **"performance_report.json"**.

**Example for RAID0:**

- RAID0 will perform faster because the data is striped across all disks. The test result for RAID0 will be shorter compared to RAID1, which mirrors data on two disks simultaneously.

### 6. Exporting RAID Status

**Example:**

1. Click the **"Export RAID Status"** button.
2. The status of the RAID array (e.g., disk state, sector usage, faults) will be exported to the file **"raid_status.json"**.
3. This file will contain detailed information about each disk's status, including faulty sectors or communication issues.

**Example for RAID3:**

- In the JSON file, you'll find information about the RAID3 disks, where parity data is stored on one disk and the other disks store the actual data.

### 7. Resetting RAID

**Example:**

1. Click the **"Reset RAID"** button.
2. The application will reset all disks to their initial state, clearing stored data and fixing any disk or sector faults.
3. The disk status monitor will be updated, and all disks will be marked as available.

**Example after simulating a fault:**

- After simulating a disk fault, click the **"Reset RAID"** button to restore the disk to its normal state.

---

## [Polish Version]

# Instrukcja obsługi aplikacji RAID Monitor

Aplikacja "RAID Monitor" to narzędzie służące do monitorowania i zarządzania macierzami RAID 0, RAID 1 i RAID 3. Poniższa instrukcja krok po kroku wyjaśnia, jak korzystać z dostępnych funkcji.

### 1. Wybór typu RAID

**Przykład:**

1. Otwórz aplikację.
2. Z rozwijanego menu wybierz **RAID0**.
   - Po wyborze RAID0 aplikacja wyświetli informacje o stanie każdego z dysków macierzy RAID0 (np. użycie sektorów, dostępność dysków).
3. Możesz teraz pracować z RAID0. Jeśli chcesz zmienić typ RAID, po prostu wybierz inny typ (np. RAID1 lub RAID3) z rozwijanego menu.

### 2. Wprowadzanie i zapisywanie danych

**Przykład:**

1. W polu tekstowym (pod rozwijanym menu) wpisz dane, np. **"Testowe dane dla RAID"**.
2. Kliknij przycisk **"Write Data"**.
   - Dane zostaną zapisane w macierzy RAID. W zależności od wybranego typu RAID (RAID0, RAID1, RAID3), dane zostaną zapisane na różnych dyskach zgodnie z logiką RAID.
3. Monitor stanu macierzy zaktualizuje użycie sektorów na dyskach. Na przykład, jeśli wybierzesz RAID1, dane zostaną zapisane na dwóch dyskach (duplikowane).

**Przykład dla RAID1:**

- Wpisz dane **"Ważne pliki"**.
- RAID1 zapisze te dane na dwóch różnych dyskach, co zapewnia redundancję danych.

### 3. Odczytywanie danych

**Przykład:**

1. Wprowadź numer sektora, z którego chcesz odczytać dane, np. **"0"** (jeśli dane zostały zapisane w sektorze 0).
2. Kliknij przycisk **"Read Data"**.
   - Aplikacja odczyta dane zapisane w tym sektorze i wyświetli je w oknie dialogowym.

**Przykład z błędnym indeksem:**

- Jeśli wpiszesz nieprawidłowy indeks, np. **"100"**, a dane są zapisane tylko w pierwszych sektorach, aplikacja wyświetli błąd, informując, że nie można odczytać danych z tego sektora.

### 4. Symulowanie awarii

#### 4.1 Symulowanie awarii dysku

**Przykład:**

1. Wprowadź numer dysku, który chcesz uszkodzić, np. **"1"** (oznacza dysk 1).
2. Kliknij przycisk **"Simulate Disk Fault"**.
   - Aplikacja oznaczy wybrany dysk jako uszkodzony, a jego stan zostanie zaktualizowany w monitorze stanu. Dysk będzie teraz wyświetlany na czerwono, a jego użycie zostanie zatrzymane.
   - Jeśli korzystasz z RAID1 lub RAID3, dane mogą być nadal dostępne z innych dysków, nawet po awarii.

**Przykład dla RAID1:**

- RAID1 ma redundancję, więc nawet po awarii dysku dane będą dostępne na drugim dysku.

#### 4.2 Symulowanie awarii sektora

**Przykład:**

1. Wprowadź dane w formacie **"dysk_id, sektor_id"**, np. **"0,1"** (co oznacza sektor 1 na dysku 0).
2. Kliknij przycisk **"Simulate Sector Fault"**.
   - Aplikacja uszkodzi wybrany sektor, a w monitorze stanu pojawi się informacja o awarii.

**Przykład z błędnym sektorem:**

- Jeśli wprowadzisz nieprawidłowe dane, np. **"4,1"**, aplikacja wyświetli komunikat o błędzie, informując o niewłaściwym numerze dysku.

#### 4.3 Symulowanie awarii komunikacji

**Przykład:**

1. Wprowadź numer dysku, z którym ma wystąpić problem komunikacji, np. **"2"**.
2. Kliknij przycisk **"Simulate Communication Fault"**.
   - Aplikacja wyświetli błąd komunikacji z wybranym dyskiem, a jego stan zostanie zaktualizowany w monitorze stanu.

### 5. Test wydajności

**Przykład:**

1. Kliknij przycisk **"Run Performance Test"**.
2. Aplikacja wykona serię operacji zapisu i odczytu danych (10000 operacji o rozmiarze 128 bajtów).
3. Po zakończeniu testu pojawi się okno dialogowe z czasem potrzebnym na wykonanie testu. Wyniki testu zostaną zapisane w pliku **"performance_report.json"**.

**Przykład dla RAID0:**

- RAID0 będzie zapisywał dane szybciej, ponieważ dane są rozdzielane między wszystkie dyski. Wynik testu dla RAID0 będzie krótszy niż dla RAID1, ponieważ RAID1 zapisuje dane na dwóch dyskach jednocześnie.

### 6. Eksportowanie statusu RAID

**Przykład:**

1. Kliknij przycisk **"Export RAID Status"**.
2. Status macierzy RAID (np. stan dysków, zużycie sektorów, awarie) zostanie wyeksportowany do pliku **"raid_status.json"**.
3. Plik ten będzie zawierał szczegółowe informacje o stanie każdego dysku, w tym o uszkodzonych sektorach lub problemach z komunikacją.

**Przykład dla RAID3:**

- W pliku JSON zobaczysz informacje o dyskach w RAID3, gdzie parzystość jest przechowywana na jednym z dysków, a dane na pozostałych.

### 7. Resetowanie macierzy RAID

**Przykład:**

1. Kliknij przycisk **"Reset RAID"**.
2. Aplikacja przywróci wszystkie dyski do stanu początkowego, usuwając zapisane dane oraz naprawiając ewentualne awarie dysków i sektorów.
3. Monitor stanu zostanie zaktualizowany, a wszystkie dyski będą oznaczone jako dostępne.

**Przykład po symulowaniu awarii:**

- Po symulowaniu awarii dysku kliknij przycisk **"Reset RAID"**, aby przywrócić dysk do sprawności.
