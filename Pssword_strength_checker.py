import re
import random
import string

# Common weak passwords
weak_passwords = {"password", "123456", "qwerty", "letmein", "admin", "welcome"}


def check_password_strength(password, level="strong"):
    # Basic rule: Minimum 8 characters
    if len(password) < 8:
        return "Weak: Password too short! (At least 8 characters required)"

    # Check for common weak passwords
    if password.lower() in weak_passwords:
        return "Weak: Your password is too common!"

    # Medium security: Require at least one number
    if level in ["strong", "very strong"] and not re.search(r"\d", password):
        return "Weak: Add at least one number."

    # Strong security: Require uppercase letter
    if level == "very strong" and not re.search(r"[A-Z]", password):
        return "Weak: Add at least one uppercase letter."

    # Very strong security: Require special characters
    if level == "very strong" and not re.search(r"[!@#$%^&*]", password):
        return "Weak: Add at least one special character."

    # No spaces allowed in any level
    if " " in password:
        return "Weak: Password should not contain spaces."

    return "Strong password!"


def generate_strong_password():
    length = 12  # Length of generated password
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))


# Get user input
level = input("Choose security level (basic/strong/very strong): ").strip().lower()
password = input("Enter your password: ").strip()

# Check password strength
result = check_password_strength(password, level)
print(result)

# Suggest a strong password if weak
if "Weak" in result:
    print("Suggested strong password:", generate_strong_password())
