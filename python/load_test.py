import pytest
import time
from page_objects import ApiPage

# Configuration
BASE_URL = 'https://example.com/api'  # Replace with your API base URL
ENDPOINT = ''  # Replace with the specific endpoint if needed
NUM_REQUESTS = 100  # Number of requests to simulate

# Initialize the ApiPage object
api_page = ApiPage(BASE_URL)

def test_load():
    """Run a load test."""
    start_time = time.time()
    responses = []

    # Simulate load with multiple requests
    for _ in range(NUM_REQUESTS):
        response = api_page.get(ENDPOINT)
        responses.append(response)
    
    end_time = time.time()

    # Check responses and performance
    for response in responses:
        assert response.status_code == 200, f"Request failed with status code {response.status_code}"

    duration = end_time - start_time
    print(f"Load test completed. Total time: {duration:.2f} seconds.")

if __name__ == "__main__":
    pytest.main()
