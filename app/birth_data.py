import streamlit as st
import pandas as pd
from astrologer_api.utils import get_birth_data

# Function to make the API request

# Streamlit UI for input
st.title("Astrology Data Viewer")
name = st.text_input("Name", "Jane Doe")
year = st.number_input("Year", min_value=1900, max_value=2100, value=1992)
month = st.number_input("Month", min_value=1, max_value=12, value=1)
day = st.number_input("Day", min_value=1, max_value=31, value=11)
hour = st.number_input("Hour", min_value=0, max_value=23, value=7)
minute = st.number_input("Minute", min_value=0, max_value=59, value=23)
city = st.text_input("City", "Asuncion")
nation = st.text_input("Nation", "PY")

# Construct the subject dictionary
subject = {
    "name": name,
    "year": year,
    "month": month,
    "day": day,
    "hour": hour,
    "minute": minute,
    "city": city,
    "nation": nation,
    "longitude": -57.63591,
    "latitude": -25.30066,
    "timezone": "America/Asuncion",
    "zodiac_type": "Tropic",
    "perspective_type": "Apparent Geocentric",
    "houses_system_identifier": "P"
}


# Fetch astrology data when the button is pressed
if st.button("Get Astrology Data"):
    data = get_birth_data(subject)
    if data:
    # Personal Info Section
        st.header("Personal Information")
        st.write(f"**Name**: {data['data']['name']}")
        st.write(f"**Birth Date**: {data['data']['day']}/{data['data']['month']}/{data['data']['year']}")
        st.write(f"**City**: {data['data']['city']}, {data['data']['nation']}")
        st.write(f"**Timezone**: {data['data']['tz_str']}")

        # Lunar Phase Section
        st.header("Lunar Phase")
        st.write(f"**Moon Phase**: {data['data']['lunar_phase']['moon_phase_name']} {data['data']['lunar_phase']['moon_emoji']}")
        st.write(f"**Sun Phase**: {data['data']['lunar_phase']['sun_phase']}")

        # Planets Section in Tabular Format
        st.header("Planetary Positions")
        planet_data = []
        planets = data['data']['planets_names_list']
        for planet_name in planets:
            planet_info = data['data'][planet_name.lower()]
            planet_data.append({
                "Planet": f"{planet_name} {planet_info['emoji']}",
                "Sign": planet_info['sign'],
                "House": planet_info['house'],
                "Position (°)": f"{planet_info['position']:.2f}",
                "Retrograde": "Yes" if planet_info['retrograde'] else "No"
            })

        planet_df = pd.DataFrame(planet_data)
        st.dataframe(planet_df)

        # Houses Section in Tabular Format
        st.header("Astrological Houses")
        house_data = []
        houses = data['data']['houses_names_list']
        for house_name in houses:
            house_info = data['data'][house_name.lower()]
            house_data.append({
                "House": f"{house_name} {house_info['emoji']}",
                "Sign": house_info['sign'],
                "Quality": house_info['quality'],
                "Element": house_info['element']
            })

        house_df = pd.DataFrame(house_data)
        st.dataframe(house_df)