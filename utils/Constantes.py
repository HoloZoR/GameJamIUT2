import pygame as __pygame

TAILLE = LARGEUR, HAUTEUR = 1024, 768
FOND = 255, 255, 255

MAX_IPS = 60
COUCHE_HUD = 2

CHEMIN_SPRITE = 'res/img/entites/'
CHEMIN_MAP = 'res/map/'
TAILLE_PERSO = [120, 120]
COULEURS = ['rouge', 'jaune', 'vert', 'bleu']

TOUCHES = [
    {'aller_gauche': __pygame.K_q, 'aller_droite': __pygame.K_d, 'sauter': __pygame.K_z, 'competence': __pygame.K_LSHIFT},
    {'aller_gauche': __pygame.K_LEFT, 'aller_droite': __pygame.K_RIGHT, 'sauter': __pygame.K_UP, 'competence': __pygame.K_RSHIFT}
]
