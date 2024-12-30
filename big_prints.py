import shutil
def introduction_of_the_game():
    def center_text(text):
        terminal_width, _ = shutil.get_terminal_size()

        # Calcul de l'espacement nécessaire pour centrer le texte
        padding = (terminal_width - len(text)) // 2

        # Affichage du texte centré avec l'espacement calculé
        print(" " * padding + text)

    # Utilisation
    center_text("***fight club ***\n".upper())
    center_text("Bienvenue dans l'arene du FIGHT CLUB.")
    center_text("Ne paniquez pas. vous vous demandez surement ce que vous faites ici non ?")
    center_text("et bien vous etes ici pour divertir. OUI, Divertir. ")
    center_text(
        "ce soir, l'elite de notre pays s'est rassemblé pour vous voir leur offir du divertissement senglant et mortel")
    center_text(
        "avant vous etiez des hommes libres vivant librement. Mais aujourd'hui vous etes les prisoniers du FIGHT CLUB et le seul moyen de retrouver votre liberté est de...")
    center_text("TUER")
    center_text("TUER votre adversaire")
    center_text(
        "Vous avez bien compris. Un combat a mort dont le seul survivant pourra sortir d'ici couvert de richesses et le perdant finira juste six pieds sous terre.")
    center_text(
        "Ah oui j'avais oublié. Je suis impardonable. Je suis Gravik le seul et l'unique présentateur de cette soirée. ")
    center_text("Et vous mes chers combatabts qui etes vous ?")

def rules_of_the_game():
    print()
    print("Voici les regles du Fight club:")
    print("Dans chaque tour, vous pouvez choisir parmi les options 0, 1 et 2.")
    print(
        "En choisissant 0, vous restez passif, gagnant ainsi 1 point d'endurance, mais vous prenez le coup de l'ennemi en pleine face.")
    print(
        "En choisissant 1, vous optez pour la défense, vous permettant d'encaisser le coup sans perdre de points de vie, mais vous perdez 0,5 points d'endurance.")
    print(
        "En choisissant 2, vous choisissez l'attaque, infligeant des dégâts aléatoires entre la valeur minimale et maximale de la force de votre avatar.")
    print("Le premier joueur à atteindre 0 point de vie perd le combat.")
    print()