import re

def is_valid_age(age):
    return age.isdigit() and 0 < int(age) < 120

def is_valid_mobile(mobile):
    return mobile.isdigit() and len(mobile) == 10

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def is_valid_name(name):
    name = name.strip()
    return 2 <= len(name) <= 50