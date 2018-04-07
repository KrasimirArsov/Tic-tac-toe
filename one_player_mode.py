from time import sleep
import pygame
from game_map import GameMap
from checker import check_win
from checker import check_tie
from players.x_player import PlayerX
from players.human_player import PlayerHuman
from players.ai.ai import AI
from util import *


def one_player_game():
    curr_game = GameMap(3)
    pygame.init()

    display_width = 640
    display_height = 740

    white = (255,255,255)

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption("TicTacToe - vs A.I.")
    grid_image = pygame.image.load("assets/grid_single.png")
    clock = pygame.time.Clock()
    player_x = AI()
    player_o = PlayerHuman()


    def display_status(text):
        gameDisplay.blit(text, (200, 30))


    def display_score(player_x, player_o):
        gameDisplay.blit(get_wins_text(player_x), (0, -8))
        gameDisplay.blit(get_wins_text(player_o), (470, -8))


    def display_grid():
        gameDisplay.blit(grid_image, (0, 0))


    def win_event(player):
        player.add_a_win()
        curr_game.set_status("   {} won a game".format(player.get_identifier().upper()))
        curr_game.clear_matrix()
        sleep(0.4)


    def tie_event():
        curr_game.clear_matrix()
        curr_game.set_status("          Tie")
        sleep(0.4)


    def display_matrix(matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] is not None:
                    if matrix[i][j] == "x":
                        gameDisplay.blit(player_x.get_prop(), (j * 220, i * 220 + 100))
                    elif matrix[i][j] == "o":
                        gameDisplay.blit(player_o.get_prop(), (j * 220, i * 220 + 100))


    def display_highlight_position(pos):
        if curr_game.get_turn() % 2 == 0:
            gameDisplay.blit(player_x.get_hilight(), (pos[1] * 220, pos[0] * 220 + 100))
        elif curr_game.get_turn() % 2 == 1:
            gameDisplay.blit(player_o.get_hilight(), (pos[1] * 220, pos[0] * 220 + 100))


    def game_loop():

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        curr_game.move_left()
                    if event.key == pygame.K_RIGHT:
                        curr_game.move_right()
                    if event.key == pygame.K_UP:
                        curr_game.move_up()
                    if event.key == pygame.K_DOWN:
                        curr_game.move_down()
                    if event.key == pygame.K_RETURN:
                        is_placed = curr_game.place_symbol()
                        if is_placed is not True:
                            curr_game.set_status(" Already occupied")
                        else:
                            curr_game.set_status(" ")
                    if curr_game.turn % 2 == 1:
                        curr_game.set_position(player_x.take_turn(curr_game.get_matrix()))
                        is_placed = curr_game.place_symbol()
                        if is_placed is not True:
                            curr_game.set_status(" Already occupied")
                        else:
                            curr_game.set_status(" ")


            gameDisplay.fill(white)
            display_grid()
            display_highlight_position(curr_game.get_position())
            display_matrix(curr_game.get_matrix())
            display_score(player_x, player_o)
            display_status(get_ready_status(curr_game.get_status()))
            pygame.display.update()

            win = check_win(curr_game.get_matrix())
            tie = check_tie(curr_game.get_matrix())
            if win != " ":
                if win == "x":
                    win_event(player_x)
                    win = " "
                elif win == "o":
                    win_event(player_o)
                    win = " "
            if tie is True:
                tie_event()

            clock.tick(30)


    game_loop()
    pygame.quit()
