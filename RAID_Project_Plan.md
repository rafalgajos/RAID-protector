# Project Documentation

## English Version

### 1. Project Topic 

**Topic**: Simulation of RAID0, RAID1, RAID3 disk arrays with fault injection and performance analysis capabilities.  

**Brief Description**:  
The project aims to create an application that simulates RAID0, RAID1, and RAID3 disk arrays. The application should allow testing under load, fault injection, and generating performance statistics. The goal is to analyze fault tolerance and compare the performance of different RAID types under simulated conditions.  

### 2. Project Goals 

- **RAID0, RAID1, RAID3 Simulation**:  
  Implementation and analysis of three types of RAID arrays.  

- **Fault Injection**:  
  Simulation of at least 3 different types of faults (e.g., damaged sectors, unavailable disks, communication errors).  

- **Performance Analysis**:  
  Testing under various loads.  
  Generating performance reports (throughput, response time).  

- **Graphical Interface**:  
  Visual monitoring of the array's status.  
  Manual fault injection.  

### 3. Functional Scope 

- **RAID Array Simulation**:  
  - **RAID0**: Striping without redundancy.  
  - **RAID1**: Mirroring of data.  
  - **RAID3**: Parity data stored on a dedicated disk.  

- **Read and Write Operations**:  
  - Data distribution across disks based on RAID type.  
  - Data reconstruction in case of failures.  

- **Fault Simulation**:  
  - Simulation of disk unavailability.  
  - Simulation of damaged sectors.  
  - Simulation of communication issues.  

- **Generating Statistics**:  
  - Analysis of operation times, throughput, disk load.  
  - Generating performance reports in PDF/CSV format.  

- **Graphical Interface**:  
  - Visualization of the RAID array.  
  - Monitoring the status of each disk.  
  - Possibility to manually introduce faults.  

### 4. Preliminary System Architecture 

- **RAID Simulation Module**:  
  - Implementation of RAID algorithms.  
  - Handling sector operations and data management.  

- **Fault Injection Module**:  
  - Simulation of various faults.  
  - Mechanisms for responding to faults.  

- **Performance Analysis Module**:  
  - Collecting statistics.  
  - Generating performance reports.  

- **GUI Module**:  
  - Visualization of the array status.  
  - User interaction with the system.  


---

# Dokumentacja Projektu

## Wersja Polska

### 1. Temat Projektu 

**Temat**: Symulacja macierzy dyskowych typu RAID0, RAID1, RAID3 z możliwością wstrzykiwania błędów i analizy wydajności.  

**Krótki opis**:  
Projekt ma na celu stworzenie aplikacji symulującej działanie macierzy RAID0, RAID1 i RAID3. Aplikacja powinna umożliwiać przeprowadzanie testów pod obciążeniem, wstrzykiwanie usterek oraz generowanie statystyk wydajności. Celem jest analiza odporności na awarie i porównanie wydajności różnych typów RAID w warunkach symulowanych.  

### 2. Cele Projektu 

- **Symulacja RAID0, RAID1, RAID3**:  
  Implementacja i analiza trzech typów macierzy RAID.  

- **Wstrzykiwanie awarii**:  
  Symulacja co najmniej 3 różnych typów awarii (np. uszkodzone sektory, niedostępne dyski, błędy komunikacyjne).  

- **Analiza wydajności**:  
  Testy pod różnymi obciążeniami.  
  Generowanie raportów wydajnościowych (przepustowość, czas odpowiedzi).  

- **Interfejs Graficzny**:  
  Graficzne monitorowanie stanu macierzy.  
  Ręczne wprowadzanie usterek.  

### 3. Zakres Funkcjonalności 

- **Symulacja macierzy RAID**:  
  - **RAID0**: Oparte na paskowaniu, bez redundancji.  
  - **RAID1**: Lustrzane kopiowanie danych.  
  - **RAID3**: Przechowywanie danych parzystości na jednym dysku.  

- **Operacje Odczytu i Zapisu**:  
  - Podział danych na dyski zgodnie z typem RAID.  
  - Rekonstrukcja danych w przypadku awarii.  

- **Symulacja Awarii**:  
  - Symulacja niedostępności dysku.  
  - Symulacja uszkodzonych sektorów.  
  - Symulacja problemów komunikacyjnych.  

- **Generowanie Statystyk**:  
  - Analiza czasu operacji, przepustowości, obciążenia dysków.  
  - Generowanie raportów wydajnościowych w formacie PDF /CSV.  

- **Interfejs Graficzny**:  
  - Wizualizacja macierzy RAID.  
  - Monitorowanie stanu każdego z dysków.  
  - Możliwość wprowadzania ręcznych usterek.  

## 4. Wstępna Architektura Systemu 

- **Moduł RAID Simulation**:  
  - Realizacja algorytmów RAID.  
  - Obsługa operacji na sektorach i zarządzanie danymi.  

- **Moduł Fault Injection**:  
  - Symulacja różnych usterek.  
  - Mechanizmy reakcji na awarie.  

- **Moduł Performance Analysis**:  
  - Zbieranie statystyk.  
  - Generowanie raportów wydajnościowych.  

- **Moduł GUI**:  
  - Wizualizacja stanu macierzy.  
  - Interakcja użytkownika z systemem.  
