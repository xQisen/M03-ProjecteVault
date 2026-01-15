import re

def check_password(pwd):
    if len(pwd) < 8:
        return False
    if not re.search(r"\d", pwd):
        return False
    if not re.search(r"[A-Z]", pwd):
        return False
    if "admin" in pwd.lower():
        return False
    return True

