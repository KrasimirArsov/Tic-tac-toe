from players.player import Player
import pygame

class PlayerX(Player):

    def __init__(self):
        super().__init__()
        self.identifier = "x"
        self.x_image = pygame.image.load("assets/x_sign.png")
        self.hilight_image = pygame.image.load("assets/x_hilight.png")

    def get_prop(self):
        return self.x_image

    def get_hilight(self):
        return self.hilight_image

    def get_identifier(self):
        return self.identifier