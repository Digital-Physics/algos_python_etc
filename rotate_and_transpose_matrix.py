# when you zip lists together the nth elements of equally-length lists are put into tuples together
# if each of these lists that are zipped is a row of column elements in a matrix, then
# zip essentially turns the nth column/element into the nth row/list (i.e. this is a matrix transpose)
# a rotation of 90 degrees is essentially just a matrix transpose followed by a reflection/reversal over a vertical axis (cols) (func #2)
# or a horizontal axis (row) reflection/reversal followed by a transpose (func directly below)
def rotate_matrix_90_clockwise(matrix: list[list[int]]) -> None:
    """rotate a matrix 90 degrees clockwise"""
    matrix = [list(tup) for tup in zip(*reversed(matrix))]
    print(matrix)


def rotate_matrix_90_clockwise2(matrix: list[list[int]]) -> None:
    """rotate a matrix 90 degrees clockwise"""
    matrix = [list(tup)[::-1] for tup in zip(*matrix)]
    print(matrix)


def transpose(matrix: list[list[int]]) -> None:
    """transpose a matrix"""
    matrix = [list(tup) for tup in zip(*matrix)]
    print(matrix)


rotate_matrix_90_clockwise([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
rotate_matrix_90_clockwise2([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

rotate_matrix_90_clockwise([[1, 2, 3], [4, 5, 6]])
rotate_matrix_90_clockwise2([[1, 2, 3], [4, 5, 6]])
transpose([[1, 2, 3], [4, 5, 6]])