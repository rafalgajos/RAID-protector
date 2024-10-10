# RAID-protector

---

![RAID Protector](deep_thinking.gif)
---

## Project Description
RAID-protector is a simulation project for RAID0, RAID1, and RAID3 arrays with fault injection and error handling capabilities. It includes a graphical user interface (GUI) for real-time monitoring, testing under various failure scenarios, and generating performance statistics. The goal is to simulate RAID systems, analyze fault tolerance, and measure performance impact under different conditions.

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Project Schedule](#project-schedule)
5. [Contributors](#contributors)
6. [License](#license)

## Features <a name="features"></a>
- **RAID Simulations**: Supports RAID0, RAID1, and RAID3 array types with 4 simulated disks.
- **Fault Injection**: Inject various types of errors (disk unavailability, sector failures, communication issues).
- **Error Handling**: Handle multiple error scenarios dynamically.
- **Performance Analysis**: Generate and display statistics for read/write operations under different RAID configurations.
- **Graphical Interface**: A GUI for managing the RAID systems, injecting errors, and viewing the state of each disk.
- **Documentation and Test Reports**: Full documentation and performance test results.

## Installation <a name="installation"></a>
1. Clone the repository:  
   ```bash
   git clone https://github.com/rafalgajos/RAID-protector.git
   ```
2. Navigate to the project directory:  
   ```bash
   cd RAID-protector
   ```
3. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:  
   ```bash
   python main.py
   ```

## Usage <a name="usage"></a>
1. Start the application.
2. Select the RAID type (RAID0, RAID1, or RAID3).
3. Use the GUI to configure disks and simulate errors.
4. Monitor the state of the RAID array in real-time.
5. Generate performance reports and analyze results.

## Project Schedule <a name="project-schedule"></a>
- **Initial Planning**: Define project scope, gather requirements, and set up initial repository structure.
- **Architecture Setup**: Establish project modules and implement base RAID architectures.
- **RAID Simulation Implementation**: Implement RAID0, RAID1, and RAID3 with fault injection and error-handling mechanisms.
- **GUI Development & Testing**: Develop GUI for RAID monitoring and conduct functional and performance testing.
- **Finalization and Presentation**: Prepare complete documentation, perform final testing, and present the project.

## Contributors <a name="contributors"></a>
- **Natalia Brzezińska**
- **Rafał Gajos**

## License <a name="license"></a>
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
