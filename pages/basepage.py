# page/api_endpoints.py

import requests
import logging
import os

# Configuration
BASE_URL = 'https://automationexercise.com/api'
LOG_FOLDER = 'logs'  # Log folder path
LOG_FILE = os.path.join(LOG_FOLDER, 'api_tests.log')  # Full path to log file

# Ensure log folder exists
os.makedirs(LOG_FOLDER, exist_ok=True)

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Create file handler for logging
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setLevel(logging.INFO)

# Create console handler for logging
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a formatter and set it for the handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

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

def log_info(test_name, response):
    """Log informational details."""
    logger.info(f"Test '{test_name}' passed with status code: {response.status_code}")
    logger.info(f"Response body: {response.text}")

def log_error(test_name, response, exception=None):
    """Log error details."""
    logger.error(f"Error in {test_name}: {exception}")
    logger.error(f"Response status code: {response.status_code}")
    logger.error(f"Response body: {response.text}")
