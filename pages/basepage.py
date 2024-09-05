# page/api_endpoints.py
import requests
import logging
import os

# Configuration
BASE_URL = 'https://automationexercise.com/api'
LOG_FOLDER = 'logs'  # Log folder path

# Ensure log folder exists
os.makedirs(LOG_FOLDER, exist_ok=True)

def setup_logger(test_file_name):
    """Set up a logger specific to each test file."""
    # Create a unique logger for each test file
    logger = logging.getLogger(test_file_name)
    logger.setLevel(logging.INFO)

    # Define the log file path using the test file name
    log_file_path = os.path.join(LOG_FOLDER, f'{test_file_name}.log')

    # Clear existing handlers if the logger already has some
    if logger.hasHandlers():
        logger.handlers.clear()

    # Create file handler for logging
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.INFO)

    # Create console handler for logging (optional)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Create a formatter and set it for the handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

class ApiPage:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, params=None):
        return requests.get(f"{self.base_url}/{endpoint}", params=params)

    def post(self, endpoint, json=None):
        return requests.post(f"{self.base_url}/{endpoint}", json=json)

    def put(self, endpoint, json=None):
        return requests.put(f"{self.base_url}/{endpoint}", json=json)

    def delete(self, endpoint, params=None):
        return requests.delete(f"{self.base_url}/{endpoint}", params=params)

def log_info(test_name, response, logger):
    """Log information about a successful test."""
    logger.info(f"Test {test_name} passed with status code: {response.status_code} and response: {response.json()}")

def log_error(test_name, response, exception, logger):
    """Log error details."""
    if exception:
        logger.error(f"Error in {test_name}: {exception} - Status Code: {response.status_code}, Response: {response.text}")
    else:
        logger.error(f"Error in {test_name}: Status Code: {response.status_code}, Response: {response.text}")
