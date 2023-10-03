# Computer Awake ⏰

 `computer_awake` is a Python script that automates key presses at a specified interval for a defined duration.

## 📚 Table of Contents

 1. [Built With](#-built-with)
 2. [Getting Started](#-getting-started)
     - [Prerequisites](#-prerequisites)
     - [Installation](#-installation)
     - [Usage](#-usage)
 3. [Contributing](#-contributing)
 4. [License](#-license)

## 🏗 Built With

- [Python 3](https://www.python.org/downloads/)

## ✅ Getting Started

 Follow the guidelines below to get this script up and running.

### 🧾 Prerequisites

 Ensure you have Python 3 and the `keyboard` library installed.

### 💻 Installation

 1. Download and install the latest version of [Python 3](https://www.python.org/downloads/).
 2. Clone the repository:

     ```sh
     git clone https://github.com/matt-wigg/computer-awake.git
     ```

 3. Install the `keyboard` library:

     ```sh
     pip install keyboard
     ```

### 🏁 Usage

 Run the script using the following command in the project's root directory:

 ```sh
 python computer_awake.py
 ```

 or

 ```sh
 python3 computer_awake.py
 ```

 To specify command line arguments:

 ```sh
 python computer_awake.py start --interval <interval> --run-time <run_time> [--key <key>]
 ```

- `<interval>`: Time (in seconds) between key presses.
- `<run_time>`: Duration (in seconds) for the script to run.
- `<key>`: The key to press; defaults to "shift".

 To stop the script:

 ```sh
 CTRL + C
 ```

## 👏 Contributing

 1. Fork the project.
 2. Create a feature branch (`git checkout -b feature/AmazingFeature`).
 3. Commit changes (`git commit -m 'Add AmazingFeature'`).
 4. Push the branch (`git push origin feature/AmazingFeature`).
 5. Open a pull request.

## 🪪 License

 This project is licensed under the MIT License.
