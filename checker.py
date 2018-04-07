def is_valid(value):
    if isinstance(value, bool):
        return False
    if not isinstance(value, (str, int, float)):
        return False


def translate_input(inpt, size):
    row = inpt // size
    col = inpt % size - 1

    if col == -1:
        return [row - 1, size + col]
    else:
        return [row, col]


def all_equal(items):
    value = items[0]
    for item in items:
        if value != item:
            return False
    return True


def fill_matrix(m_size, fill_with):
    if is_valid(fill_with):
        raise TypeError("Invalid input!")
    output_matrix = []
    for i in range(m_size):
        output_matrix.append([])
        for j in range(m_size):
            output_matrix[i].append(fill_with)
    return output_matrix


def display_matrix(matrix):
    side_char = "|"
    top_bot_char = "- "
    print(top_bot_char * (len(matrix) + 2))
    for item in matrix:
        print(side_char, end="")
        for under_item in item:
            print(under_item, end=" ")
        print(side_char)
    print(top_bot_char * (len(matrix) + 2))


def update_matrix(coordinates, value, matrix):
    is_valid(value)
    matrix[coordinates[0]][coordinates[1]] = value
    return matrix


def check_valid_coord(coordinates, matrix):
    if matrix[coordinates[0]][coordinates[1]] == ".":
        return True
    else:
        return False


def check_item_win(item):
    value = item[0]

    if (value == "x" or value == "o") and all_equal(item):
        return value
    else:
        return " "


def check_horizontal_win(matrix):
    to_return = " "
    for item in matrix:
        outcome = check_item_win(item)
        if outcome != " ":
            to_return = outcome

    return to_return


def check_vertical_win(matrix):
    to_return = " "
    for j in range(len(matrix[0])):
        column = []
        for i in range(len(matrix)):
            column.append(matrix[i][j])

        outcome = check_item_win(column)
        if outcome != " ":
            to_return = outcome

    return to_return


def check_forward_diagonal(matrix):
    diagonal = []
    x = 0
    y = len(matrix) - 1
    for _ in matrix:
        diagonal.append(matrix[x][y])
        x += 1
        y -= 1

    to_return = " "
    outcome = check_item_win(diagonal)
    if outcome != " ":
            to_return = outcome

    return to_return


def check_backward_diagonal(matrix):
    diagonal = []
    for i in range(len(matrix)):
        diagonal.append(matrix[i][i])

    to_return = " "
    outcome = check_item_win(diagonal)
    if outcome != " ":
            to_return = outcome

    return to_return


def check_diagonal_win(matrix):
    forward = check_forward_diagonal(matrix)
    backward = check_backward_diagonal(matrix)
    if forward == "x" or forward == "o":
        return forward
    elif backward == "x" or backward == "o":
        return backward
    else:
        return " "


def check_win(matrix):
    horizontal = check_horizontal_win(matrix)
    vertical = check_vertical_win(matrix)
    diagonal = check_diagonal_win(matrix)

    if horizontal == "x" or horizontal == "o":
        return horizontal
    elif vertical == "x" or vertical == "o":
        return vertical
    elif diagonal == "x" or diagonal == "o":
        return diagonal
    else:
        return " "


def check_tie(matrix):
    no_win = False
    if check_win(matrix) == " ":
        no_win = True
    no_space = True
    for row in matrix:
        for item in row:
            if item is None:
                no_space = False

    if no_win and no_space:
        return True
    else:
        return False