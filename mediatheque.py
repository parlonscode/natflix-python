import csv


MIN_AGE_PER_RATING = {
    # Pour regarder un film ou série d'une catégorie, votre âge doit être supérieur à la limite.
    "TV-Y": 0,  # Le programme est évalué comme étant approprié aux enfants.
    "TV-Y7": 7,  # Le programme est destiné aux enfants âgés de 7 ans et plus.
    "TV-Y7-FV": 7,  # Le programme est destiné aux enfants âgés de 7 ans et plus.
    "TV-G": 10,  # La plupart des parents peuvent considérer ce programme comme approprié pour les enfants.
    "TV-PG": 14,  # Contient des éléments que les parents peuvent considérer inappropriés pour les enfants
    "TV-14": 14,  # Contient des éléments pouvant être inappropriés pour les enfants de moins de 14 ans
    "TV-MA": 17,  # Uniquement réservé aux adultes et inapproprié pour la jeune audience de moins de 17 ans.
    "G": 0,  # Tous les âges sont admis. Rien qui offenserait les parents pour le visionnage par les enfants.
    "PG": 7,  # Certains matériaux peuvent ne pas convenir aux jeunes enfants
    "PG-13": 13,  # Certains contenus peuvent ne pas convenir aux enfants de moins de 13 ans.
    "R": 17,  # Les moins de 17 ans doivent être accompagnés d'un parent ou d'un tuteur adulte.
    "NC-17": 18,  # Personne de 17 ans et moins admis. Clairement adulte. Les enfants ne sont pas admis.
    "NR": 13,  # Non-rated donc par défaut, il doit être considéré comme PG-13
    "UR": 13,  # Unrated donc par défaut, il doit être considéré comme PG-13
    "": 13,  # Si la valeur est manquante, donc par défaut, il doit être considéré comme PG-13
}


def load_shows(media_file):
    with open(media_file, "r") as f:
        reader = csv.DictReader(f, delimiter="|")

        shows = []

        for show in reader:
            show["pays"] = (
                [] if show["pays"].strip() == "" else show["pays"].split(", ")
            )
            show["acteurs"] = (
                [] if show["acteurs"].strip() == "" else show["acteurs"].split(", ")
            )
            show["directeurs"] = (
                []
                if show["directeurs"].strip() == ""
                else show["directeurs"].split(", ")
            )
            show["categories"] = (
                []
                if show["categories"].strip() == ""
                else show["categories"].split(", ")
            )

            shows.append(show)

        return shows


def filter_shows_by_age(shows, user_age):
    return [
        show for show in shows if user_age >= MIN_AGE_PER_RATING[show["classement"]]
    ]


def filter_shows_by_country(shows, user_country):
    return [show for show in shows if user_country.lower() == show["pays"].lower()]


def filter_shows_by_title_or_description(shows, expression):
    return [
        show
        for show in shows
        if expression.lower() in show["titre"].lower()
        or expression.lower() in show["description"].lower()
    ]
