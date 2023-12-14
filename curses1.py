import curses
import time


def affichage_titre(titre):
    for ligne in titre:
        print(ligne)
    time.sleep(2)



def affichage_aire_de_jeu(hauteur, largeur, titre):
    # Création d'une nouvelle fenètre en 0, 0
    win = curses.____
    # Les séquences d'échapement sont générés par certaines touches, les autres n'ont aucun effet
    win.keypad(__)
    # L'écho des caractères saisis est désactivé
    curses.noecho()
    # Pas de curseur visible
    curses.curs_set(__)
    # La saisie de caractère est non bloquante
    win.nodelay(1)
    # La fenètre a une bordure standard
    win.____
    # Définition d'une couleur pour le titre : texte en rouge sur fond blanc
    # Voir dans la documentation la table "lists the predefined colors"
    curses.init_pair(1, curses.____, curses.____)
    # Affichage du titre
    win.addstr(0, 27, titre, curses.color_pair(1))
    # Raffraichissement de la fenêtre
    win.____
    # Emission d'un beep
    curses.____
    # retourner la fenêtre
    return ____




titre =['  _______     _________ _    _  ____  _   _    _____ _   _          _  ________ ',
        ' |  __ \ \   / |__   __| |  | |/ __ \| \ | |  / ____| \ | |   /\   | |/ |  ____|',
        ' | |__) \ \_/ /   | |  | |__| | |  | |  \| | | (___ |  \| |  /  \  |   /| |__   ',
        ' |  ___/ \   /    | |  |  __  | |  | | . ` |  \___ \| . ` | / /\ \ |  < |  __|  ',
        ' | |      | |     | |  | |  | | |__| | |\  |  ____) | |\  |/ ____ \| . \| |____ ',
        ' |_|      |_|     |_|  |_|  |_|\____/|_| \_| |_____/|_| \_/_/    \_|_|\_|______|']


# Affichge du titre pendant 2s avant l'ouverture de la fenêtre de jeu
affichage_titre(titre)
# Initialisation du terminal
curses._____
# Démarrage du mode couleur
curses.start_color()
# Affichage de l'aire de jeu
affichage_aire_de_jeu(20,60, 'SNAKE')
# Tempo 10s
curses.napms(____)
# fin de l'affichage de la fenêtre
curses.endwin()
