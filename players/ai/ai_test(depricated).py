def generate_matrix(size):
    matrix = []
    for i in range(size):
        matrix.append([None] * size)
    return matrix


def create_list_of_lines(matrix):
    lines = []
    #adding horizontal lines
    for hor_line in matrix:
        lines.append(hor_line)
    #adding vertical lines
    for i in range(len(matrix)):
        ver_line = []
        for j in range(len(matrix[i])):
            ver_line.append(matrix[j][i])
        lines.append(ver_line)
    #adding diagonal lines
    back_diag_line = []
    for i in range(len(matrix)):
        back_diag_line.append(matrix[i][i])
    lines.append(back_diag_line)
    forw_diag_line = []
    x = 0
    y = len(matrix) - 1
    for _ in matrix:
        forw_diag_line.append(matrix[x][y])
        x += 1
        y -= 1
    lines.append(forw_diag_line)
    return lines


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


test_matrix = generate_matrix(3)
test_matrix[0][0] = "x"
test_matrix[0][1] = "o"
test_matrix[1][1] = "o"
test_matrix[2][1] = "o"
test_matrix[2][2] = "o"
test_matrix[0][2] = "x"
display_matrix(test_matrix)
lines = create_list_of_lines(test_matrix)
for item in lines:
    print(item)



