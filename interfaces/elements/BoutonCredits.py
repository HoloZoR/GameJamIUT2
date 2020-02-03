import pygame

from gestionnaires.Evenement import Evenement
from interfaces.elements.Bouton import Bouton


class BoutonCredits(Bouton):
    def __init__(self, coord, image, menu):
        super().__init__(coord, image, menu)
        Evenement().enregistrer(pygame.MOUSEBUTTONUP, self)

    def evenement(self, evenement):
        if (self.coord[0] <= pygame.mouse.get_pos()[0] <= self.coord[0] + 100) \
                and (self.coord[1] <= pygame.mouse.get_pos()[1] <= self.coord[1] + 30):
            print("Credits")
            self.afficherCredits()

    def afficherCredits(self):
        self.menu.credits = True
