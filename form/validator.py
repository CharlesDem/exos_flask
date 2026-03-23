import re

USERNAME_REGEX = re.compile(r"^.{2,20}$")
EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
PASSWORD_REGEX = re.compile(r"^.{8,}$")
AGE_REGEX = re.compile(r"^\d{1,3}$")

def validate_user(data):
    errors = {}

    username = data.get("username", "")
    if not USERNAME_REGEX.match(username):
        errors["username"] = "must be 2 à 20 caracters"

    email = data.get("email", "")
    if not EMAIL_REGEX.match(email):
        errors["email"] = "invalid format"

    password = data.get("password", "")
    if not PASSWORD_REGEX.match(password):
        errors["password"] = "must be at least 8 caracteres"

    age = data.get("age")
    if age is None or not AGE_REGEX.match(str(age)):
        errors["age"] = "must be a number"
    else:
        age = int(age)
        if age < 18 or age > 100:
            errors["age"] = "must be between 18 and 100"

    return errors