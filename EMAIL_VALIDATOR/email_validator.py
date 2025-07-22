import re

def is_valid_email(email):
    # Regular expression pattern for validating email
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    if re.match(pattern, email):
        return True
    else:
        return False

if __name__ == "__main__":
    email_input = input("Enter an email address to validate: ")
    if is_valid_email(email_input):
        print("✅ This is a valid email address.")
    else:
        print("❌ Invalid email format.")
