import hashlib
import re


def is_a_valid_email_address(email):
    if re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email) is None:
        return False
    else:
        return True


def hash_password(plain_password):
    return hashlib.sha512(plain_password.encode()).hexdigest()


def verify_password(password_digest, plain_password):
    return password_digest == hash_password(plain_password)
