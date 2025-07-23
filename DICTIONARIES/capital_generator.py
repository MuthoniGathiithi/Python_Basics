country_capitals = {
    "kenya": "Nairobi",
    "uganda": "Kampala",
    "tanzania": "Dodoma",
    "rwanda": "Kigali",
    "burundi": "Gitega",
    "south Sudan": "Juba",
    "ethiopia": "Addis Ababa",
    "nigeria": "Abuja",
    "ghana": "Accra",
    "south Africa": "Pretoria",
    "egypt": "Cairo",
    "morocco": "Rabat",
    "algeria": "Algiers",
    "zimbabwe": "Harare",
    "Zambia": "Lusaka",
    "botswana": "Gaborone",
    "namibia": "Windhoek",
    "malawi": "Lilongwe",
    "cameroon": "Yaoundé",
    "senegal": "Dakar",
    "dr congo": "Kinshasa",
    "tunisia": "Tunis",
    "sudan": "Khartoum",
    "somalia": "Mogadishu",
    "libya": "Tripoli",
    "ivory Coast": "Yamoussoukro",
    "mali": "Bamako",
    "niger": "Niamey",
    "chad": "N'Djamena",
    "mauritania": "Nouakchott"
}

country = input("Enter a country name: ").lower()

capital = country_capitals.get(country)

if capital:
    print(f"The capital of {country} is {capital}.")
else:
    print("Sorry, country not found in the list.")
