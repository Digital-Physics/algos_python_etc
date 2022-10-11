def search_matrix(matrix: list[list[int]], target: int) -> bool:
    """Efficiently finds whether a number exists in a sorted matrix.
    First we'll binary search to determine the row to look in.
    Then we'll binary search the column."""
    print(matrix)
    if len(matrix) == 1:
        # determine column
        if len(matrix[0]) == 1:
            return False if matrix[0][0] != target else True

        col_length = len(matrix[0])
        j = col_length//2

        if matrix[0][j] == target:
            return True
        elif matrix[0][j] > target:
            return search_matrix([matrix[0][:j]], target)
        else:
            return search_matrix([matrix[0][j:]], target)

    row_length = len(matrix)
    i = row_length//2  # if it's odd, we round down on the length and land at the middle index

    # determine row
    if matrix[i][0] == target:
        return True
    elif matrix[i][0] > target:
        return search_matrix(matrix[:i], target)
    else:
        return search_matrix(matrix[i:], target)


test_matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
test_target = 3

test_matrix2 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
test_target2 = 13

print(search_matrix(test_matrix, test_target))
print(search_matrix(test_matrix2, test_target2))

