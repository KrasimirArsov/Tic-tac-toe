from players.player import Player
import pygame
from random import randint

class AI(Player):

    def __init__(self):
        super().__init__()
        self.matrix = []
        self.list_of_lines = []
        self.identifier = "x"
        self.x_image = pygame.image.load("assets/x_image_single.png")
        self.hilight_image = pygame.image.load("assets/AI_hilightor.png")

    """
    me = A.I.
    him = pesky human opponent
    line = any combination of 3 fields in a straight line
    x = always me
    o = human
    """

    @staticmethod
    def translate(coords):
        if coords[0] < 3:
            return coords
        elif coords[0] < 6:
            return coords[1], coords[0] - 3
        elif coords[0] < 7:
            return coords[1], coords[1]
        else:
            return coords[1], 2 - coords[1]
 
    def update_inner_matrix(self, matrix):

        self.matrix = matrix
        self.list_of_lines = self.create_list_of_lines()

    def get_prop(self):
        return self.x_image

    def get_hilight(self):
        return self.hilight_image

    def get_identifier(self):
        return self.identifier

    def take_turn(self, matrix):
        self.update_inner_matrix(matrix)

        turn_coords = self.decide_turn()
        return turn_coords

    def create_list_of_lines(self):

        lines = []

        #adding horizontal lines
        for hor_line in self.matrix:
            lines.append(hor_line)

        #adding vertical lines
        for i in range(len(self.matrix)):
            ver_line = []
            for j in range(len(self.matrix[i])):
                ver_line.append(self.matrix[j][i])
            lines.append(ver_line)

        #adding diagonal lines
        back_diag_line = []
        for i in range(len(self.matrix)):
            back_diag_line.append(self.matrix[i][i])
        lines.append(back_diag_line)

        forw_diag_line = []
        x = 0
        y = len(self.matrix) - 1
        for _ in self.matrix:
            forw_diag_line.append(self.matrix[x][y])
            x += 1
            y -= 1
        lines.append(forw_diag_line)

        return lines

    def decide_turn(self):

        desicion = None
        undecided_yet = (-1, -1)

        desicion = self.check_two_mine()
        if desicion == undecided_yet:
            desicion = self.check_two_his()

        if desicion == undecided_yet:
            desicion = self.check_mine_crossing_mine_and_his()

        if desicion == undecided_yet:
            desicion = self.check_mine_crossing_his()

        if desicion == undecided_yet:
            desicion = self.just_go_by_priority()

        return desicion

    def chech_two(self, line, symbol):

        if line == [symbol, symbol, None] or line == [symbol, None, symbol] or line == [None, symbol, symbol]:
            return True
        else:
            return False

    def check_if_corner(self, coords):
        i = coords[0]
        j = coords[1]
        if (i == 0 and j == 0):
            return True
        elif (i == 0 and j == 2):
            return True
        elif (i == 2 and j == 0):
            return True
        elif (i == 2 and j == 2):
            return True
        return False


    def check_two_mine(self):

        for curr_line_number in range(len(self.list_of_lines)):
            if self.chech_two(self.list_of_lines[curr_line_number], "x"):
                for curr_field_number in range(len(self.list_of_lines[curr_line_number])):
                    if self.list_of_lines[curr_line_number][curr_field_number] is None:
                        return curr_line_number, curr_field_number
        return -1, -1

    def check_two_his(self):

        for curr_line_number in range(len(self.list_of_lines)):
            if self.chech_two(self.list_of_lines[curr_line_number], "o"):
                for curr_field_number in range(len(self.list_of_lines[curr_line_number])):
                    if self.list_of_lines[curr_line_number][curr_field_number] is None:
                        return curr_line_number, curr_field_number
        return -1, -1

    def check_mine_crossing_his(self):
        return -1, -1

    def just_go_by_priority (self):
        x = randint(0, 2)
        y = randint(0, 2)
        return x, y

    def check_mine_crossing_mine_and_his(self):

        return -1, -1

