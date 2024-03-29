import csv
import datetime

import utils
import settings


def get_existing_users():
    current_year = datetime.datetime.now().year
    existing_users = []
    with open("users.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            existing_users.append(
                {
                    "name": row[0],
                    "email": row[1],
                    "age": current_year - int(row[2]),
                    "country": row[3],
                    "subscription_type": int(row[4]),
                    "password": row[5],
                }
            )
    return existing_users


def get_existing_email_addresses():
    return [user["email"] for user in get_existing_users()]


def register():
    current_year = datetime.datetime.now().year

    name = None
    while name is None:
        name = input("Veuillez entrer votre nom: ").strip()

        if name == "":
            print("Le nom ne peut pas être vide.")
            name = None

    email = None
    while email is None:
        email = input("Veuillez entrer votre email: ").lower()

        if not utils.is_a_valid_email_address(email):
            print("L'adresse email entrée est invalide!")
            email = None
            continue

        if email in get_existing_email_addresses():
            print("Désolé, adresse email déjà utilisée.")
            email = None

    birth_year = None
    while birth_year is None:
        birth_year = input("Veuillez entrer votre année de naissance: ")

        if not birth_year.isdigit():
            print("L'année doit être un entier positif.")
            birth_year = None

        if not (
            current_year - settings.MAX_AGE
            <= int(birth_year)
            <= current_year - settings.MIN_AGE
        ):
            print(
                f"L'année doit être comprise entre {current_year - settings.MAX_AGE} et {current_year - settings.MIN_AGE}"
            )
            birth_year = None

    # TODO: Validate country
    # https://stackoverflow.com/questions/41245330/check-if-a-country-entered-is-one-of-the-countries-of-the-world
    country = None
    while country is None:
        country = input("Veuillez entrer votre pays: ").strip()

        if country == "":
            print("Le pays entré est invalide.")
            country = None

    subscription_type = None
    while subscription_type is None:
        subscription_type = input(
            "Veuillez entrer votre type d'abonnement - 1 [Régional] ou 2 [International]: "
        )

        if subscription_type not in ("1", "2"):
            print(
                "Le type d'abonnement doit être 1 pour régional ou 2 pour international."
            )
            subscription_type = None

    password = None
    while password is None:
        password = input("Veuillez entrer votre mot de passe (min 6 caractères): ")

        if len(password) < 6 or password.isspace():
            print(
                "Le mot de passe doit faire au minimum 6 caractères et ne doit pas contenir que des espaces."
            )
            password = None

    password_digest = utils.hash_password(password)

    user = {
        "name": name,
        "email": email,
        "age": current_year - int(birth_year),
        "country": country,
        "subscription_type": int(subscription_type),
        "password": password_digest,
    }

    with open("users.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow(
            [name, email, birth_year, country, subscription_type, password_digest]
        )

    return user


def authenticate():
    email = None
    while email is None:
        email = input("Veuillez entrer votre email: ").lower()

        if not utils.is_a_valid_email_address(email):
            print("L'adresse email entrée est invalide!")
            email = None
            continue

        if email not in get_existing_email_addresses():
            print(
                "Nous n'avons trouvé aucun utilisateur avec cette adresse email au niveau de notre système."
            )
            email = None

    user_found = None
    for u in get_existing_users():
        if u["email"] == email:
            user_found = u
            break

    password = None
    while password is None:
        password = input("Veuillez entrer votre mot de passe: ")

        if not utils.verify_password(user_found["password"], password):
            print("Mot de passe invalide!")
            password = None

    return user_found
