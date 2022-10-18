import user
import settings
import mediatheque


def display_main_title():
    print("#" * settings.TITLE_WIDTH)
    print(f'###{"Bienvenue dans Natflix":^{settings.TITLE_WIDTH - 6}}###')
    print("#" * settings.TITLE_WIDTH)


def display_home_menu_and_retrieve_user_choice():
    choice = None

    while choice is None:
        print("Menu d'accueil")
        print("1 - S'inscrire")
        print("2 - S'authentifier")
        print("3 - Quitter")

        choice = input("Veuillez entrer votre choix: ")

        if choice not in ("1", "2", "3"):
            print(
                "Votre choix n'est pas dans la liste des options. Veuillez réessayer."
            )
            choice = None

    return choice


def display_user_menu_and_retrieve_user_choice():
    choice = None

    while choice is None:
        print("Menu Utilisateur")
        print("1 - Rechercher des films ou séries avec une expression")
        print("2 - Rechercher des films ou séries selon le genre")
        print("3 - Rechercher des films ou séries selon les acteurs")
        print(
            "4 - Afficher la médiathèque par ordre des shows les plus récemment ajoutés"
        )
        print("5 - Afficher la médiathèque par ordre des shows les plus populaires")
        print("6 - Afficher la médiathèque par ordre des shows les mieux évalués")
        print("7 - Quitter l'application")

        choice = input("Veuillez entrer votre choix: ")

        if choice not in ("1", "2", "3", "4", "5", "6", "7"):
            print(
                "Votre choix n'est pas dans la liste des options. Veuillez réessayer."
            )
            choice = None

    return choice


def main():
    # shows = mediatheque.load_shows(settings.MEDIA_FILE)
    # print(len(shows))
    # shows = mediatheque.filtrer_shows_par_age(shows, 12)
    # print(len(shows))
    # # if authenticated_user['subscription_type'] == 1:
    # if True:
    #     print('filtrer par pays')
    # print(shows)
    display_main_title()
    user_choice = display_home_menu_and_retrieve_user_choice()

    match user_choice:
        case "1":
            authenticated_user = user.register()
        case "2":
            authenticated_user = user.authenticate()
        case "3":
            authenticated_user = None

    if authenticated_user is not None:
        shows = mediatheque.load_shows(settings.MEDIA_FILE)
        shows = mediatheque.filter_shows_by_age(shows, authenticated_user['age'])

        # Si l'utilisateur a un abonnement régional
        if authenticated_user['subscription_type'] == 1:
            shows = mediatheque.filter_shows_by_country(shows, authenticated_user['country'])

        print(
            f"Salut {authenticated_user['name']}! Tu as accès à {len(shows)} films et séries télés."
        )
        user_choice = display_user_menu_and_retrieve_user_choice()
        print(f"{user_choice=}")


if __name__ == "__main__":
    main()
