import requests
import json
from config import settings

def astrologer_post(endpoint: str, payload: dict) -> dict:
    """
    Sends a POST request to a specified astrologer API endpoint.

    Args:
        endpoint (str): Endpoint path (e.g., 'birth-data').
        payload (dict): JSON-serializable request body.

    Returns:
        dict: JSON response from the API.
    """
    api_key = settings.ASTROLOGER_API_KEY
    base_url = settings.ASTROLOGER_BASE_URL

    if not api_key or not base_url:
        raise ValueError("API key or base URL not found. Please check your configuration.")
    if not base_url.startswith("http"):
        raise ValueError("Base URL must start with 'http' or 'https'.")

    url = f"{base_url.rstrip('/')}/{endpoint.lstrip('/')}"
    api_host = base_url.replace("https://", "").replace("http://", "").split("/")[0]

    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": api_host,
        "X_RapidAPI-Host": api_host,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    print(f"[DEBUG] POST: {url} - Status: {response.status_code}")

    if not response.ok:
        raise ValueError(f"API request failed with status {response.status_code}: {response.text}")

    try:
        return response.json()
    except json.decoder.JSONDecodeError as e:
        raise ValueError(f"Response is not valid JSON: {response.text}") from e
    
def get_birth_data(birth_data: dict) -> dict:
    """
    Calls the 'birth-data' endpoint with the given subject info.
    """
    payload = {"subject": birth_data}  # Wrap the data here
    return astrologer_post("birth-data", payload)

def get_relationship_score(subject_1: dict, subject_2: dict) -> dict:
    """
    Calls the 'relationship-score' endpoint with the given subjects.
    """
    payload = {
        "first_subject": subject_1,
        "second_subject": subject_2
    }
    return astrologer_post("relationship-score", payload)

def get_birth_chart(birth_data: dict) -> dict:
    """
    Calls the 'birth-chart' endpoint with the given subject info.
    """
    payload = {"subject": birth_data}  # Wrap the data here
    return astrologer_post("birth-chart", payload)