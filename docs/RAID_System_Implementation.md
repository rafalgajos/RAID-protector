# [ENGLISH VERSION]

# RAID Monitoring System Implementation Description

## 1. **Graphical User Interface (GUI)**

The interface was built using the **Tkinter** library, which allows creating window-based graphical applications in Python. The user can select the RAID type, enter data into the array, read it, and simulate various types of failures. The application also displays the status of RAID disks through:

- **Progress bars** for each disk, showing sector usage,
- **Colored indicators** signaling the status of disks (green – disk is operational, red – disk is faulty),
- **Text box** displaying detailed information about the disks and stored data.

### Key GUI Components:
- **RAID selection menu** – allows the user to select one of the RAID types (RAID0, RAID1, RAID3),
- **Text fields** – for entering data to be written or read from the RAID array,
- **Action buttons** – for writing data, reading data, simulating faults, and exporting RAID status,
- **Disk monitoring** – via progress bars and percentage labels showing sector usage.

### GUI Code
The main application class is `RAIDMonitorApp`, which initializes all Tkinter components and defines event handling, such as button clicks and RAID type selection.

## 2. **RAID Types Support**

The system implements three different RAID types: **RAID0**, **RAID1**, and **RAID3**. Each of these types has different mechanisms for reading and writing data, with implementations based on the `RAIDBase` class, which defines the general structure of a RAID array.

### RAID0 (Striping)
- Data is evenly distributed across disks in blocks. This results in fast read and write speeds but no redundancy, so if one disk fails, all data is lost.
- Implemented in the `RAID0` class, where data is written alternately across multiple disks.

### RAID1 (Mirroring)
- Data is copied to all disks in the array. RAID1 provides full redundancy, but it’s less efficient in terms of disk space since every disk contains the same data.
- Implemented in the `RAID1` class, where each write operation is replicated on all available disks.

### RAID3 (Striping with Parity)
- Data is distributed across multiple disks, and one disk stores parity information, allowing data recovery if one disk fails.
- Implemented in the `RAID3` class, where data is written in sectors across different disks, and the additional disk stores parity information.

## 3. **Fault Simulation**

The system allows simulating different types of faults:

### Disk Failure Simulation
- The `simulate_disk_fault()` function lets the user select a disk to be marked as unavailable, simulating a physical disk failure.

### Sector Fault Simulation
- The `simulate_sector_fault()` function enables simulating a faulty sector on a specific disk. The sector becomes unreadable, simulating a sector-level failure.

### Communication Fault Simulation
- The `simulate_communication_fault()` function simulates a communication failure for a disk, preventing data from being written or read.

## 4. **Performance Testing**

The system supports performance testing via the `run_performance_test()` function, which enables testing the RAID array under load. These tests write and read large amounts of data, and the results (write and read times) are saved in a JSON file.

### Example Test Report:
```json
{
    "RAID Type": "RAID0",
    "Number of Disks": 4,
    "Disk Size": 128,
    "Number of Operations": 10000,
    "Data Size (bytes)": 128,
    "Write Time (seconds)": 2.45,
    "Read Time (seconds)": 1.78
}
```
## 5. **RAID Status Export**

The RAID array status can be exported to a JSON file using the export_raid_status() function. This file contains detailed information about each disk, such as availability, faulty sectors list, and the data stored on the disk.

### Example Structure of ```raid_status.json```:
```json
{
    "RAID Type": "RAID1",
    "Disks": [
        {
            "Disk ID": 0,
            "Available": true,
            "Faulty Sectors": [],
            "Communication Fault": false,
            "Used Sectors": ["a", "b", "c"]
        },
        {
            "Disk ID": 1,
            "Available": true,
            "Faulty Sectors": [3],
            "Communication Fault": false,
            "Used Sectors": ["a", "b", "c"]
        }
    ]
}
```
## 6. **RAID Array Reset**

The ```reset_raid()``` function resets the RAID array to its initial state by removing all stored data, repairing all faulty disks and sectors, and restoring communication with each disk. This functionality is especially useful for re-running tests or experiments without the influence of previous failures.

## 7. **Conclusion**

The RAID monitoring system offers:

- A complete graphical interface for managing RAID arrays,
- Data input and retrieval,
- Fault simulation for disks, sectors, and communication,
- Performance testing under load,
- Export of results and RAID status.

---

---

---

# [POLISH VERSION]

# Opis Implementacji Systemu Monitorowania RAID

## 1. **Interfejs Graficzny (GUI)**

Interfejs został zbudowany przy użyciu biblioteki **Tkinter**, która umożliwia tworzenie okienkowych aplikacji graficznych w Pythonie. Użytkownik może wybierać typ macierzy RAID, wprowadzać dane do macierzy, odczytywać je oraz symulować różnego rodzaju awarie. Aplikacja przedstawia także stan dysków w macierzy poprzez:

- **Pasek postępu** dla każdego dysku, pokazujący zużycie sektora,
- **Kolorowe wskaźniki** sygnalizujące stan dysków (zielony – dysk działa poprawnie, czerwony – dysk uszkodzony),
- **Pole tekstowe**, które wyświetla szczegółowy stan dysków i zapisanych danych.

### Kluczowe elementy GUI:
- **Menu wyboru RAID** – pozwala na wybranie jednego z typów RAID (RAID0, RAID1, RAID3),
- **Pola tekstowe** – do wprowadzania danych, które mają zostać zapisane lub odczytane z macierzy RAID,
- **Przyciski akcji** – do zapisu danych, odczytu danych, symulacji usterek oraz eksportu stanu RAID,
- **Monitorowanie dysków** – za pomocą paska postępu i etykiet procentowych pokazujących zużycie sektorów.

### Kod GUI
Główna klasa aplikacji to `RAIDMonitorApp`, która inicjalizuje wszystkie komponenty Tkintera i definiuje obsługę zdarzeń, takich jak kliknięcie przycisków czy zmiana wybranego typu RAID.

## 2. **Obsługa Typów RAID**

W systemie zaimplementowano trzy różne typy macierzy RAID: **RAID0**, **RAID1** i **RAID3**. Każdy z nich ma różne mechanizmy zapisu i odczytu danych, a implementacja bazuje na klasie bazowej `RAIDBase`, która definiuje ogólną strukturę macierzy RAID.

### RAID0 (Striping)
- Dane są zapisywane równomiernie na dyskach, podzielone na bloki. Dzięki temu odczyt i zapis mogą być bardzo szybkie, jednak brak jest nadmiarowości, więc uszkodzenie jednego dysku prowadzi do utraty danych.
- Zaimplementowane w klasie `RAID0`, gdzie dane są zapisywane na różnych dyskach w sposób naprzemienny.

### RAID1 (Mirroring)
- Dane są kopiowane na wszystkie dyski w macierzy. RAID1 zapewnia pełną redundancję, ale jest mniej efektywny pod względem wykorzystania przestrzeni dyskowej, ponieważ każdy dysk zawiera tę samą kopię danych.
- Zaimplementowane w klasie `RAID1`, gdzie każda operacja zapisu jest powielana na wszystkich dostępnych dyskach.

### RAID3 (Striping z parzystością)
- Dane są rozkładane na wiele dysków, a na jednym z dysków zapisywana jest informacja o parzystości, umożliwiająca odtworzenie danych w przypadku awarii jednego z dysków.
- Zaimplementowane w klasie `RAID3`, gdzie dane są zapisywane w sektorach na różnych dyskach, a dodatkowy dysk przechowuje informacje o parzystości.

## 3. **Symulacja Usterek**

System umożliwia symulację różnych rodzajów usterek:

### Symulacja Awarii Dysku
- Funkcja `simulate_disk_fault()` pozwala użytkownikowi wybrać dysk, który zostanie oznaczony jako niedostępny, co symuluje fizyczną awarię dysku.

### Symulacja Usterek Sektorów
- Funkcja `simulate_sector_fault()` umożliwia wprowadzenie usterki w danym sektorze na wybranym dysku. Ten sektor staje się wtedy nieczytelny, co symuluje awarię na poziomie sektora.

### Symulacja Awarii Komunikacji
- Funkcja `simulate_communication_fault()` symuluje awarię komunikacyjną dysku, co uniemożliwia zapisywanie i odczytywanie danych z tego dysku.

## 4. **Testy Wydajnościowe**

System obsługuje testy wydajnościowe poprzez funkcję `run_performance_test()`, która umożliwia przetestowanie macierzy RAID pod obciążeniem. Testy te zapisują i odczytują dużą ilość danych, a ich wyniki (czasy zapisu i odczytu) są zapisywane w pliku JSON.

### Przykład raportu z testów:
```json
{
    "RAID Type": "RAID0",
    "Number of Disks": 4,
    "Disk Size": 128,
    "Number of Operations": 10000,
    "Data Size (bytes)": 128,
    "Write Time (seconds)": 2.45,
    "Read Time (seconds)": 1.78
}
```
## 5. **Eksportowanie Stanu RAID**

Stan macierzy RAID może zostać wyeksportowany do pliku JSON za pomocą funkcji export_raid_status(). Plik ten zawiera szczegółowe informacje o każdym dysku, takie jak dostępność, listę uszkodzonych sektorów, a także dane zapisane na dysku.

### Przykład struktury pliku```raid_status.json```:
```json
{
    "RAID Type": "RAID1",
    "Disks": [
        {
            "Disk ID": 0,
            "Available": true,
            "Faulty Sectors": [],
            "Communication Fault": false,
            "Used Sectors": ["a", "b", "c"]
        },
        {
            "Disk ID": 1,
            "Available": true,
            "Faulty Sectors": [3],
            "Communication Fault": false,
            "Used Sectors": ["a", "b", "c"]
        }
    ]
}
```
## 6. **Resetowanie Macierzy RAID**

Funkcja ```reset_raid()``` przywraca macierz RAID do początkowego stanu, usuwając wszystkie zapisane dane, naprawiając wszystkie uszkodzone dyski i sektory, oraz przywracając poprawną komunikację z każdym dyskiem. Ta funkcjonalność jest szczególnie użyteczna do ponownego uruchamiania testów lub eksperymentów bez wpływu poprzednich awarii.

## 7. **Podsumowanie**

System monitorowania RAID oferuje:

- Pełny interfejs graficzny umożliwiający zarządzanie macierzami RAID,
- Wprowadzanie i odczyt danych,
- Symulację awarii dysków, sektorów i komunikacji,
- Testy wydajnościowe pod obciążeniem,
- Eksport wyników oraz stanu RAID.