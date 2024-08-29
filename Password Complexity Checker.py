import re
def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    criteria_met = [length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_criteria]
    strength = sum(criteria_met)

    feedback = {
        0: "Very Weak",
        1: "Very Weak",
        2: "Weak",
        3: "Moderate",
        4: "Strong",
        5: "Very Strong"
    }

    print(f"Password Strength: {feedback[strength]}")

    if not length_criteria:
        print(" - Password should be at least 8 characters long.")
    if not uppercase_criteria:
        print(" - Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        print(" - Password should include at least one lowercase letter.")
    if not number_criteria:
        print(" - Password should include at least one number.")
    if not special_criteria:
        print(" - Password should include at least one special character.")

def main():
    password = input("Enter a password to check its strength: ")
    check_password_strength(password)

if __name__ == "__main__":
    main()
