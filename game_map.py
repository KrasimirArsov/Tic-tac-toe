

class GameMap:
    def __init__(self, size):
        self.__curr_position = (0, 0)
        self.turn = 0
        self.size = size
        self.__status = ""
        self.__game_matrix = self.generate_matrix()
        self.occupied_positions = set()

    def generate_matrix(self):
        matrix = []
        for i in range(self.size):
            matrix.append([None] * self.size)
        return matrix

    def clear_matrix(self):
        matrix = []
        for i in range(self.size):
            matrix.append([None] * self.size)

        self.__game_matrix = matrix
        self.occupied_positions = set()

    def display_matrix(self):
        side_char = "|"
        top_bot_char = "- "
        print(top_bot_char * (len(self.__game_matrix) + 2))
        for item in self.__game_matrix:
            print(side_char, end="")
            for under_item in item:
                print(under_item, end=" ")
            print(side_char)
        print(top_bot_char * (len(self.__game_matrix) + 2))

    def place_symbol(self):
        if self.__curr_position not in self.occupied_positions:
            if self.turn % 2 == 0:
                self.display_matrix()
                self.__game_matrix[self.__curr_position[0]][self.__curr_position[1]] = "x"
                self.occupied_positions.add(self.__curr_position)
            elif self.turn % 2 == 1:
                self.display_matrix()
                print((self.__curr_position[0], self.__curr_position[1]))
                self.__game_matrix[self.__curr_position[0]][self.__curr_position[1]] = "o"
                self.occupied_positions.add(self.__curr_position)
            self.turn += 1
            return True
        else:
            return False

    def set_position(self, coord):
        self.__curr_position = coord

    def set_status(self, status):
        self.__status = status

    def get_position(self):
        return self.__curr_position

    def get_matrix(self):
        return self.__game_matrix

    def get_turn(self):
        return self.turn

    def get_status(self):
        return self.__status

    def move_left(self):
        if self.__curr_position[1] > 0:
            self.set_position((self.get_position()[0], self.get_position()[1] - 1))
        else:
            self.set_status("   Can't go left")

    def move_right(self):
        if self.__curr_position[1] < self.size - 1:
            self.set_position((self.get_position()[0], self.get_position()[1] + 1))
        else:
            self.set_status("   Can't go right")

    def move_up(self):
        if self.__curr_position[0] > 0:
            self.set_position((self.get_position()[0] - 1, self.get_position()[1]))
        else:
            self.set_status("     Can't go up")

    def move_down(self):
        if self.__curr_position[0] < self.size - 1:
            self.set_position((self.get_position()[0] + 1, self.get_position()[1]))
        else:
            self.set_status("   Can't go down")
