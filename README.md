# astrology-calculator

A Streamlit-based web application and Python API client for calculating astrological birth data and relationship compatibility scores using the Astrologer API.

## Current Features

- **Birth Data Viewer:** Enter birth details to view astrological information, lunar phases, planetary positions, and houses.
- **Relationship Score Calculator:** Compare two people's birth data to calculate their astrological compatibility and view detailed aspects.
- **API Client:** Python utilities for interacting with the Astrologer API, including endpoints for birth data and relationship scores.

## Project Structure

```
main.py                      # Example CLI for relationship score
test.py                      # Example API test script
app/
  birth_data.py              # Streamlit app for birth data
  relationship_score.py      # Streamlit app for relationship score
  astrologer_api/
    utils.py                 # API client utilities
  config/
    settings.py              # Loads API keys and base URL from .env
```

## Setup

1. **Clone the repository**

2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
   Or, if using `pyproject.toml`:
   ```sh
   pip install .
   ```

3. **Configure environment variables**

   Create an `.env` file in `app` with:
   ```
   ASTROLOGER_API_KEY=your_rapidapi_key
   ASTROLOGER_BASE_URL=https://astrologer.p.rapidapi.com/api/v4
   ```

## Usage

### Streamlit Apps

- **Birth Data Viewer**
  ```sh
  streamlit run app/birth_data.py
  ```
- **Relationship Score Calculator**
  ```sh
  streamlit run app/relationship_score.py
  ```

### Command Line

- Run the example CLI:
  ```sh
  python main.py
  ```

### API Test

- Test direct API call:
  ```sh
  python test.py
  ```

## API Utilities

- `app/astrologer_api/utils.py` provides:
  - `get_birth_data`
  - `get_relationship_score`
  - `get_birth_chart`

## License

This project is licensed under the GNU Affero General Public License v3.0.