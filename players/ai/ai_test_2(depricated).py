

def check_for_corner(coord):
    i = coord[0]
    j = coord[1]

    if (i is 0 and (j is not 1)) and (i is 2 and (j is not 1)):
        print("{}, {} is corner".format(i, j))


test_matrix = generate_matrix(3)
test_matrix[0][0] = "x"
test_matrix[0][2] = "x"