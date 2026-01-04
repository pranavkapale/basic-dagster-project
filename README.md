# Basic Dagster Project

## 📌 Overview
This project is designed for learning the basics of [Dagster](https://dagster.io/), a data orchestrator for machine learning, analytics, and ETL. It demonstrates how to scaffold a Dagster project and build assets, jobs, schedules, and sensors.

**Key Features:**
* **Dagster UI:** Provides a web-based interface for managing and monitoring pipelines.
* **Asset Development:** Assets are defined in `car_data/assets.py` and automatically loaded.
* **Testing:** Unit tests are included in the `car_data_tests` directory.
* **Scheduling:** Supports schedules and sensors for job automation.

## 🏗 Architecture
1. **Code Location:** The Dagster code location is scaffolded and installed as a Python package.
2. **Assets:** Assets are defined in Python and loaded dynamically.
3. **Testing:** Unit tests are written using `pytest`.
4. **Schedules and Sensors:** Automate job execution with Dagster Daemon.

## 🛠 Tech Stack
* **Language:** Python
* **Orchestration:** Dagster
* **Testing Framework:** Pytest

## 🚀 How to Run

### Prerequisites
* Python installed on your system.
* Install the project dependencies.

### Steps
1. **Install the project as a Python package:**
    ```bash
    pip install -e ".[dev]"
    ```

2. **Start the Dagster UI web server:**
    ```bash
    dagster dev
    ```
    Open [http://localhost:3000](http://localhost:3000) in your browser to access the Dagster UI.

3. **Run Unit Tests:**
    ```bash
    pytest car_data_tests
    ```

## 📊 Dataset
The dataset used in this project can be found under the Microsoft Azure [carprice](https://github.com/Azure/carprice/blob/master/dataset/carprice.csv) project.

## Additional Info

### Schedules and Sensors
To enable [Schedules](https://docs.dagster.io/guides/automate/schedules/) or [Sensors](https://docs.dagster.io/guides/automate/sensors/), ensure the [Dagster Daemon](https://docs.dagster.io/guides/deploy/execution/dagster-daemon) process is running. This is done automatically when you run `dagster dev`.

## 📚 Acknowledgments
Special thanks to the YouTube channel [BugBytes](https://www.youtube.com/@bugbytes3923) for their helpful video tutorial: ["Dagster Tutorial"](https://youtu.be/sKqDq4TFbmY?si=z9qTLQ1BuGLl1LWB).
