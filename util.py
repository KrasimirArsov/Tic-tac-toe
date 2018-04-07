import pygame


def get_wins_text(player):
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 80)
    wins_text = font.render("{0} : {1}".format(player.get_identifier(), player.wins), False, (0, 0, 0))
    return wins_text


def get_ready_status(text):
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 30)
    status_text = font.render(text, False, (0, 0, 0))
    return status_text


def generate_matrix(size):
    matrix = []
    for i in range(size):
        matrix.append([None] * size)
    return matrix


def print_matrix(matrix):
    side_char = "|"
    top_bot_char = "- "
    print(top_bot_char * (len(matrix) + 2))
    for item in matrix:
        print(side_char, end="")
        for under_item in item:
            print(under_item, end=" ")
        print(side_char)
    print(top_bot_char * (len(matrix) + 2))