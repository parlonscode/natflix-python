import datetime

import utils

# TODO: Replace with real existing email addresses
existing_email_addresses = {"honore@gmail.com", "pierre@gmail.com"}


def register():
    name = None
    while name is None:
        name = input("Veuillez entrer votre nom: ")

        if name.strip() == "":
            print("Le nom ne peut pas être vide.")
            name = None

    email = None
    while email is None:
        email = input("Veuillez entrer votre email: ").lower()

        if not utils.is_a_valid_email_address(email):
            print("L'adresse email entrée est invalide!")
            email = None

        if email in existing_email_addresses:
            print("Désolé, adresse email déjà utilisée.")
            email = None

    birth_year = None
    while birth_year is None:
        birth_year = input("Veuillez entrer votre année de naissance: ")

        if not birth_year.isdigit():
            print("L'âge doit être un entier positif.")
            birth_year = None

    # TODO: Validate that user's age is between a given interval
    age = datetime.datetime.now().year - int(birth_year)

    # TODO: Validate country
    # https://stackoverflow.com/questions/41245330/check-if-a-country-entered-is-one-of-the-countries-of-the-world
    country = None
    while country is None:
        country = input("Veuillez entrer votre pays: ")

        if country.strip() == "":
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

    user = {
        "name": name,
        "email": email,
        "age": age,
        "country": country,
        "subscription_type": int(subscription_type),
        "password": password,
    }

    with open('users.txt', 'a') as f:
        f.write(f'{name},{email},{age},{country},{subscription_type},{password}\n')

    return user


def authenticate():
    # TODO: Authenticate user
    print("Processus d'authentification")
