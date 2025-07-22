from datetime import datetime

def calculate_date_difference():
    date_format = "%Y-%m-%d"
    
    date1_str = input("Enter the first date (YYYY-MM-DD): ")
    date2_str = input("Enter the second date (YYYY-MM-DD): ")

    try:
        date1 = datetime.strptime(date1_str, date_format)
        date2 = datetime.strptime(date2_str, date_format)

        difference = abs((date2 - date1).days)
        print(f"The difference is {difference} days.")
    
    except ValueError:
        print("Please enter the date in correct format (YYYY-MM-DD).")

if __name__ == "__main__":
    calculate_date_difference()
