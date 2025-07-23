country_capitals = {
    "Kenya": "Nairobi",
    "Uganda": "Kampala",
    "Tanzania": "Dodoma",
    "Rwanda": "Kigali",
    "Burundi": "Gitega",
    "South Sudan": "Juba",
    "Ethiopia": "Addis Ababa",
    "Nigeria": "Abuja",
    "Ghana": "Accra",
    "South Africa": "Pretoria",
    "Egypt": "Cairo",
    "Morocco": "Rabat",
    "Algeria": "Algiers",
    "Zimbabwe": "Harare",
    "Zambia": "Lusaka",
    "Botswana": "Gaborone",
    "Namibia": "Windhoek",
    "Malawi": "Lilongwe",
    "Cameroon": "Yaoundé",
    "Senegal": "Dakar",
    "DR Congo": "Kinshasa",
    "Tunisia": "Tunis",
    "Sudan": "Khartoum",
    "Somalia": "Mogadishu",
    "Libya": "Tripoli",
    "Ivory Coast": "Yamoussoukro",
    "Mali": "Bamako",
    "Niger": "Niamey",
    "Chad": "N'Djamena",
    "Mauritania": "Nouakchott"
}

country = input("Enter a country name: ")

capital = country_capitals.get(country)

if capital:
    print(f"The capital of {country} is {capital}.")
else:
    print("Sorry, country not found in the list.")
