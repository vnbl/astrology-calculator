from astrologer_api.utils import get_relationship_score 

def main():
    subject_1 = {
        "year": 1992,
        "month": 1,
        "day": 11,
        "hour": 7,
        "minute": 23,
        "longitude": -57.63591,
        "latitude": -25.30066,
        "city": "Asuncion",
        "nation": "PY",
        "timezone": "UTC",  # simplified
        "name": "Jane Doe",
        "zodiac_type": "Tropic",
        "perspective_type": "Apparent Geocentric",
        "houses_system_identifier": "P"
        # removed sidereal_mode
    }
    subject_2 = {
        "year": 1992,
        "month": 1,
        "day": 11,
        "hour": 7,
        "minute": 23,
        "longitude": -57.63591,
        "latitude": -25.30066,
        "city": "Asuncion",
        "nation": "PY",
        "timezone": "UTC",  # simplified
        "name": "Jane Doe",
        "zodiac_type": "Tropic",
        "perspective_type": "Apparent Geocentric",
        "houses_system_identifier": "P"
        # removed sidereal_mode
    }
    response = get_relationship_score(subject_1=subject_1, subject_2=subject_2) # No wrapping of "subject" here
    print(response)


if __name__ == "__main__":
    main()
