from two_player_mode import two_player_game
from one_player_mode import one_player_game
import pygame

class Menu:

    def __init__(self):
        self.option_selected = 0

    def move_selection_up(self):
        if self.option_selected == 0:
            self.option_selected = 2
        else:
            self.option_selected -= 1

    def move_selection_down(self):
        if self.option_selected == 2:
            self.option_selected = 0
        else:
            self.option_selected += 1

    def get_option_selected(self):
        return self.option_selected


pygame.init()
main_menu = Menu()
clock = pygame.time.Clock()

display_width = 640
display_height = 740

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("TicTacToe")
bg = pygame.image.load("assets/menu_bg.png")
hilighter = pygame.image.load("assets/menu_hilighter.png")
labels = pygame.image.load("assets/menu_labels.png")


white = (255, 255, 255)


def display_bg():
    gameDisplay.blit(bg, (0, 0))


def display_hilighter(position, hili_image):
    if position == 0:
        hili = pygame.transform.scale(hili_image, (370, 90))
        gameDisplay.blit(hili, (135, 335))
    elif position == 1:
        hili = pygame.transform.scale(hili_image, (370, 90))
        gameDisplay.blit(hili, (135, 435))
    elif position == 2:
        hili = pygame.transform.scale(hili_image, (160, 90))
        gameDisplay.blit(hili, (425, 615))


def display_labels():
    gameDisplay.blit(labels, (0, 0))


gameDisplay = pygame.display.set_mode((display_width, display_height))

def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    main_menu.move_selection_up()
                if event.key == pygame.K_DOWN:
                    main_menu.move_selection_down()
                if event.key == pygame.K_RETURN:
                    if main_menu.get_option_selected() == 0:
                        one_player_game()
                    elif main_menu.get_option_selected() == 1:
                        two_player_game()
                    elif main_menu.get_option_selected() == 2:
                        pygame.quit()

        display_bg()
        display_hilighter(main_menu.get_option_selected(), hilighter)
        display_labels()
        pygame.display.update()
        clock.tick(30)


game_loop()