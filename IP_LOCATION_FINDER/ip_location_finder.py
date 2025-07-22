import requests

def get_ip_info(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"IP Address: {data.get('ip', 'N/A')}")
        print(f"Location: {data.get('city', 'N/A')}, {data.get('region', 'N/A')}, {data.get('country', 'N/A')}")
        print(f"ISP: {data.get('org', 'N/A')}")
        print(f"Timezone: {data.get('timezone', 'N/A')}")
    else:
        print("Failed to retrieve data. Check the IP address or your connection.")

if __name__ == "__main__":
    ip_input = input("Enter an IP address to lookup: ")
    get_ip_info(ip_input)
