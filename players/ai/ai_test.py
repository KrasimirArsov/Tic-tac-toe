from players.ai.ai import AI
from util import print_matrix, generate_matrix


def test_check_two_mine():
    ai = AI()

    test_matrix = generate_matrix(3)
    test_matrix[0][0] = "x"
    test_matrix[0][2] = "x"
    ai.update_inner_matrix(test_matrix)
    assert ai.check_two_mine() == (0, 1)

    test_matrix = generate_matrix(3)
    test_matrix[0][0] = "x"
    test_matrix[2][2] = "x"
    ai.update_inner_matrix(test_matrix)
    assert ai.check_two_mine() == (6, 1)

    test_matrix = generate_matrix(3)
    test_matrix[0][2] = "x"
    test_matrix[2][2] = "x"
    ai.update_inner_matrix(test_matrix)
    assert ai.check_two_mine() == (5, 1)
    print("check_two_mine() function passed!")


def test_check_two_his():
    ai = AI()

    test_matrix = generate_matrix(3)
    test_matrix[0][0] = "o"
    test_matrix[0][2] = "o"
    ai.update_inner_matrix(test_matrix)
    assert ai.check_two_his() == (0, 1)

    test_matrix = generate_matrix(3)
    test_matrix[0][0] = "o"
    test_matrix[2][2] = "o"
    ai.update_inner_matrix(test_matrix)
    assert ai.check_two_his() == (6, 1)

    test_matrix = generate_matrix(3)
    test_matrix[0][2] = "o"
    test_matrix[2][2] = "o"
    ai.update_inner_matrix(test_matrix)
    assert ai.check_two_his() == (5, 1)
    print("check_two_his() function passed!")


def test_check_if_corner():
    ai = AI()

    test_matrix = generate_matrix(3)
    coll_of_bools = []
    test_matrix[0][0] = "o"
    test_matrix[0][2] = "o"
    test_matrix[2][0] = "o"
    test_matrix[2][2] = "o"
    ai.update_inner_matrix(test_matrix)
    for i in range(len(test_matrix)):
        for j in range(len(test_matrix[i])):
            coll_of_bools.append(ai.check_if_corner((i, j)))
    print("test_check_if_corner() passed!")
    assert coll_of_bools == [True, False, True, False, False, False, True, False, True]


def test_translate():
    ai = AI()

    assert ai.translate((0, 1)) == (0, 1)
    assert ai.translate((4, 1)) == (1, 1)
    assert ai.translate((5, 2)) == (2, 2)
    assert ai.translate((6, 0)) == (0, 0)
    assert ai.translate((6, 2)) == (2, 2)
    assert ai.translate((7, 0)) == (0, 2)
    assert ai.translate((7, 1)) == (1, 1)
    print("test_translate() passed!")







test_check_two_mine()
test_check_two_his()
test_check_if_corner()
test_translate()
