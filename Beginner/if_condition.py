city_country = {
    "Mumbai": "India",
    "Chennai": "India",
    "Delhi": "India",
    "Bangalore": "India",
    "Sydney": "Australia",
    "Melbourne": "Australia",
    "Dubai": "UAE",
    "Abu Dhabi": "UAE",
    "New York": "USA",
    "Los Angeles": "USA"
}
city1 = input("Enter the first city: ").strip().title()
city2 = input("Enter the second city: ").strip().title()
if city1 in city_country and city2 in city_country:
    if city_country[city1] == city_country[city2]:
        print(f"Both cities are in {city_country[city1]}")
    else:
        print("They don't belong to the same country")
else:
    print("One or both cities are not in the database")
