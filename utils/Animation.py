import pygame


class Animation:
    def __init__(self, x, y, largeur, hauteur, nb_images, temps_anim, loop=True, temps_premiere_img=-1):
        self.__x = x
        self.__y = y
        self.__largeur = largeur
        self.__hauteur = hauteur
        self.__nb_images = nb_images
        self.__temps_animation = temps_anim
        self.__temps_premiere_img = temps_premiere_img
        self.__temps = 0
        self.__image = 0
        self.__loop = loop
        self.__fin = False

    """
    :return pygame.rect Un rectangle permettant de découper l'image selon la partie de l'animation demandée
    """
    def recuperer_image(self):
        return False if self.__fin else pygame.Rect((self.__x * self.__largeur) + (self.__image * self.__largeur),
                                                    self.__y, self.__largeur, self.__hauteur)

    def ajouter_temps(self, delta):
        temps_anim = self.__temps_animation
        if self.__image == 0 and self.__temps_premiere_img > 0:
            temps_anim = self.__temps_premiere_img

        self.__temps += delta
        if self.__temps >= temps_anim:
            self.__temps -= temps_anim
            self.__image = (self.__image + 1) % self.__nb_images
            if self.__image == 0 and not self.__loop:
                self.__fin = True

    def recuperer_sous_sprite(self, sprite, x, y):
        sous_sprite = sprite.subsurface(self.recuperer_image())
        sous_sprite_rect = sous_sprite.get_rect()
        sous_sprite_rect.x, sous_sprite_rect.y = x, y
        return sous_sprite, sous_sprite_rect

    def reinitialiser(self, img=0):
        self.__image = img
        self.__temps = 0
        self.__fin = False

    def est_finie(self):
        return self.__fin
