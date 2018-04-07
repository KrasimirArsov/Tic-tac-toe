from players.player import Player
import pygame

class PlayerHuman(Player):

    def __init__(self):
        super().__init__()
        self.identifier = "o"
        self.o_image = pygame.image.load("assets/o_image_single.png")
        self.hilight_image = pygame.image.load("assets/human_hilightor.png")

    def get_prop(self):
        return self.o_image

    def get_hilight(self):
        return self.hilight_image

    def get_identifier(self):
        return self.identifier