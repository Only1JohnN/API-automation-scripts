# Load-Stress-Test-Automation

Welcome to the **Load-Stress-Test-Automation** repository! This project contains automated scripts for load and stress testing to assess and optimize application performance. The repository provides tools and configurations for simulating various load conditions and stress scenarios to ensure system robustness and reliability.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
  - [Clone the Repository](#clone-the-repository)
  - [Create a Python Virtual Environment](#create-a-python-virtual-environment)
  - [Install Python Dependencies](#install-python-dependencies)
  - [Install JMeter](#install-jmeter)
  - [Configure Your Tests](#configure-your-tests)
  - [Run Load Tests with JMeter](#run-load-tests-with-jmeter)
  - [Run Stress Tests with JMeter](#run-stress-tests-with-jmeter)
  - [Run Load Tests with Pytest](#run-load-tests-with-pytest)
  - [Run Stress Tests with Pytest](#run-stress-tests-with-pytest)
  - [Review Reports](#review-reports)
- [Directory Structure](#directory-structure)
- [License](#license)
- [Contributing](#contributing)
- [Contact](#contact)

## Features

- **Load Testing**: Simulate normal and peak load conditions using JMeter or Python `pytest` to evaluate application performance under typical usage.
- **Stress Testing**: Assess system behavior under extreme conditions using JMeter or Python `pytest` to identify potential breaking points and performance degradation.
- **Comprehensive Reporting**: Generate detailed reports with JMeter and `pytest` to analyze performance metrics and identify bottlenecks.
- **Customizable Configurations**: Easily adjust testing parameters and scenarios to fit different applications and environments.
- **Integration with Pytest**: Utilize `pytest` for running additional custom tests and generating reports.

## Requirements

- **JMeter**: For creating and running load and stress tests.
- **Python**: For custom scripts and integrations.
- **Page Object Model (POM)**: Used for structuring test automation in a maintainable and scalable way.
- **pytest**: Framework for running Python tests and generating reports.
- **Requests Library**: For making HTTP requests in Python tests.

## Setup

### Clone the Repository

```bash
git clone https://github.com/Only1JohnN/Load-Stress-Test-Automation.git
cd Load-Stress-Test-Automation
```

### Create a Python Virtual Environment

To avoid conflicts between dependencies, it's recommended to use a virtual environment. You can create one using `venv`:

```bash
python -m venv venv
```

Activate the virtual environment:

- **On Windows:**

    ```bash
    venv\Scripts\activate
    ```

- **On macOS/Linux:**

    ```bash
    source venv/bin/activate
    ```

### Install Python Dependencies

Install the required Python packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Install JMeter

Follow the instructions on the [Apache JMeter website](https://jmeter.apache.org/download_jmeter.cgi) to download and install JMeter.

### Configure Your Tests

- **JMeter Tests**: Modify the JMeter configuration files and test scripts according to your application’s requirements. Update parameters such as URLs, endpoints, and test data as needed.

- **Pytest Tests**: Write or configure your Python test scripts for load and stress testing. Update URLs and parameters in `load_test.py` and `stress_test.py` as needed.

### Run Load Tests with JMeter

Execute load testing scripts using JMeter:

```bash
jmeter -n -t jmeter/load_test_script.jmx -l results/load_test_results.jtl
```

### Run Stress Tests with JMeter

Execute stress testing scripts similarly:

```bash
jmeter -n -t jmeter/stress_test_script.jmx -l results/stress_test_results.jtl
```

### Run Load Tests with Pytest

Execute Python load tests using `pytest`:

```bash
pytest python/load_test.py
```

### Run Stress Tests with Pytest

Execute Python stress tests using `pytest`:

```bash
pytest python/stress_test.py
```

### Review Reports

- **JMeter Reports**: Analyze the `.jtl` results files or use JMeter’s reporting tools to generate detailed performance reports.
- **Pytest Reports**: Review the output from `pytest` to assess the performance of your application under load and stress conditions.

## Directory Structure

- **`jmeter/`**: Contains JMeter scripts and configurations for load and stress testing scenarios.
  - `load_test_script.jmx`: JMeter script for load testing.
  - `stress_test_script.jmx`: JMeter script for stress testing.

- **`python/`**: Contains Python scripts for load and stress testing.
  - `load_test.py`: Python script for custom load testing using `pytest`.
  - `stress_test.py`: Python script for custom stress testing using `pytest`.

- **`results/`**: Directory where JMeter test results are saved.
  - `load_test_results.jtl`: Results file for load tests.
  - `stress_test_results.jtl`: Results file for stress tests.

- **`requirements.txt`**: Lists Python dependencies required for custom scripts.
- **`page_objects.py`**: Defines Page Object Model classes used in tests (if applicable).

## License

This project is licensed under the MIT License. However, you must contact me before using or redistributing this software.

## Contributing

Contributions are welcome! If you’d like to contribute, please fork the repository and submit a pull request (PR). Ensure that your contributions adhere to the project's coding standards and include appropriate tests. Open issues or PRs to discuss and review any changes.

## Contact

For any questions, feedback, or collaboration inquiries, please reach out to Adeniyi John.

Thank you for using **Load-Stress-Test-Automation**. We hope this tool helps you achieve optimal performance for your applications!
