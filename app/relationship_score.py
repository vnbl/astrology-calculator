import streamlit as st
import pandas as pd
from astrologer_api.utils import get_relationship_score

# Function to display the input form for birth details
def get_input_fields():
    # First person's details

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("First Person's Details")
        first_name = st.text_input("Name", "Fer")
        first_year = st.number_input("Year of Birth", min_value=1900, max_value=2100, value=1992)
        first_month = st.number_input("Month of Birth", min_value=1, max_value=12, value=1)
        first_day = st.number_input("Day of Birth", min_value=1, max_value=31, value=11)
        first_hour = st.number_input("Hour of Birth", min_value=0, max_value=23, value=7)
        first_minute = st.number_input("Minute of Birth", min_value=0, max_value=59, value=23)
    with col2:  
    # Second person's details
        st.subheader("Second Person's Details")
        second_name = st.text_input("Name2", "Paz")
        second_year = st.number_input("Year of Birth2", min_value=1900, max_value=2100, value=1996)
        second_month = st.number_input("Month of Birth2", min_value=1, max_value=12, value=2)
        second_day = st.number_input("Day of Birth2", min_value=1, max_value=31, value=26)
        second_hour = st.number_input("Hour of Birth2", min_value=0, max_value=23, value=12)
        second_minute = st.number_input("Minute of Birth2", min_value=0, max_value=59, value=0)

    return (first_name, first_year, first_month, first_day, first_hour, first_minute, 
            second_name, second_year, second_month, second_day, second_hour, second_minute)

# Function to create the subject data from input
def create_subject_data(name, year, month, day, hour, minute):
    return {
        'name': name,
        'year': year,
        'month': month,
        'day': day,
        'hour': hour,
        'minute': minute,
        "longitude": -57.63591,
        "latitude": -25.30066,
        "city": "Asuncion",
        "nation": "PY",
        "timezone": "America/Asuncion",
        "zodiac_type": "Tropic",
        "perspective_type": "Apparent Geocentric",
        "houses_system_identifier": "P"
    }

# Function to display the relationship score and details
def display_relationship_score(result):
    if result['status'] == 'OK':
        st.subheader("Relationship Score")
        st.write(f"Score: {result['score']} - {result['score_description']}")
        st.write(f"Is Destiny Sign: {'Yes' if result['is_destiny_sign'] else 'No'}")

        # Display Aspects
        st.subheader("Aspects")
        for aspect in result['aspects']:
            st.write(f"{aspect['p1_name']} - {aspect['p2_name']} : {aspect['aspect']} ({aspect['orbit']})")

        # Create two columns for side-by-side display
        col1, col2 = st.columns(2)
        
        # Display Subject 1 Details in the first column
        with col1:
            st.subheader(f"Subject 1: {result['data']['first_subject']['name']}")
            display_subject_details(result['data']['first_subject'])

        # Display Subject 2 Details in the second column
        with col2:
            st.subheader(f"Subject 2: {result['data']['second_subject']['name']}")
            display_subject_details(result['data']['second_subject'])

        # Display JSON view
        st.title("Astrology compatibility JSON view")
        st.json(result)
    else:
        st.error("Failed to retrieve relationship score. Please try again later.")


# Function to display the detailed information for a subject (person 1 or person 2)
def display_subject_details(subject_data):
    st.subheader(f"Subject: {subject_data['name']}")
    st.write(f"Birth Date: {subject_data['day']}/{subject_data['month']}/{subject_data['year']}")
    st.write(f"City: {subject_data['city']}, {subject_data['nation']}")

    # Display Lunar Phase
    st.header("Lunar Phase")
    st.write(f"Moon Phase: {subject_data['lunar_phase']['moon_phase_name']} {subject_data['lunar_phase']['moon_emoji']}")
    st.write(f"Sun Phase: {subject_data['lunar_phase']['sun_phase']}")

    # Display Planetary Positions
    st.header("Planetary Positions")
    planet_data = []
    planets = subject_data['planets_names_list']
    for planet_name in planets:
        planet_info = subject_data[planet_name.lower()]
        planet_data.append({
            "Planet": f"{planet_name} {planet_info['emoji']}",
            "Sign": planet_info['sign'],
            "House": planet_info['house'],
            "Position (°)": f"{planet_info['position']:.2f}",
            "Retrograde": "Yes" if planet_info['retrograde'] else "No"
        })
    planet_df = pd.DataFrame(planet_data)
    st.dataframe(planet_df)

    # Display Astrological Houses
    st.header("Astrological Houses")
    house_data = []
    houses = subject_data['houses_names_list']
    for house_name in houses:
        house_info = subject_data[house_name.lower()]
        house_data.append({
            "House": f"{house_name} {house_info['emoji']}",
            "Sign": house_info['sign'],
            "Position (°)": f"{house_info['position']:.2f}"
        })
    house_df = pd.DataFrame(house_data)
    st.dataframe(house_df)

# Main Streamlit App
def main():
    st.title('Astrology Relationship Score')
    st.write("Enter the birth details of two people to calculate their relationship score.")
    
    # Get the input fields from the user
    first_name, first_year, first_month, first_day, first_hour, first_minute, \
    second_name, second_year, second_month, second_day, second_hour, second_minute = get_input_fields()
    
    # Create subject data for both individuals
    first_subject = create_subject_data(first_name, first_year, first_month, first_day, first_hour, first_minute)
    second_subject = create_subject_data(second_name, second_year, second_month, second_day, second_hour, second_minute)

    # Button to calculate relationship score
    if st.button("Calculate Relationship Score"):
        # Get relationship score from API
        result = get_relationship_score(first_subject, second_subject)
        
        # Display relationship score and details
        display_relationship_score(result)

if __name__ == "__main__":
    main()
