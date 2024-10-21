"""Module for reading from and writing to csv files, calculating reflexive, symmetric, transitive
closing of matrices."""

# from itertools import product
# import numpy as np


# 1
def read_matrix_from_csv(csv_file: str) -> list[list[int]]:
    """
    Reads a matrix from a text file and returns it as a two-dimensional array.

    :param csv_file: str, name of file
    :return: list[list[int]], two-dimensional list representing the read matrix.
    """
    file = open(csv_file)

    position_0_0 = file.tell()
    num_of_lines = len(file.readlines())
    file.seek(position_0_0)

    matrix: list[list[int]] = []
    for _ in range(num_of_lines):
        row = file.readline()
        matrix.append([int(j) for j in row if j.isdigit()])
    file.close()

    # matrix: list[list[int]] = []
    #
    # with open(csv_file, 'r') as file:
    #     for line in file:
    #         matrix.append([int(i) for i in line.split(',')])
    return matrix


def write_matrix_to_csv(csv_file: str, matrix: list[list[int]]) -> None:
    """
    Write given matrix to file
    :param csv_file: str, file to write
    :return: None
    """
    with open(csv_file, 'w') as write_file:
        for row in matrix:
            print(','.join([str(num) for num in row]), file=write_file)


# 2
def reflexive_closing(matrix: list[list[int]]) -> list[list[int]]:
    """
    Making reflexive closing of matrix.

    :param matrix: list[list[int]], given matrix
    :return: list[list[int]], reflexive closing of given matrix

    >>> reflexive_closing([[1, 0, 1], [0, 0, 0], [1, 0, 0]])
    [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
    >>> reflexive_closing([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    """
    n = len(matrix)
    for i in range(n):
        matrix[i][i] = 1
    return matrix


# 3
def symmetrical_closing(matrix: list[list[int]]) -> list[list[int]]:
    """
    Making symmetrical closing of matrix.

    :param matrix: list[list[int]], given matrix
    :return: list[list[int]], symmetrical closing of given matrix

    >>> symmetrical_closing([[1, 0, 1], [1, 1, 1], [1, 0, 0]])
    [[1, 1, 1], [1, 1, 1], [1, 1, 0]]
    """
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                matrix[j][i] = 1
    return matrix


# 4
def transitive_closing(matrix: list[list[int]]) -> list[list[int]]:
    """
    Return transitive closing of given matrix
    :param matrix: list[list[int]], matrix to process
    :return: list[list[int]], transitive closing of matrix

    >>> transitive_closing([[1, 1, 1], [1, 0, 1], [1, 0, 0]])
    [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    >>> transitive_closing([[1, 0, 0, 1], [0, 0, 0, 0], [1, 1, 1, 0], [0, 0, 1, 0]])
    [[1, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 1, 1]]
    """

    size: int = len(matrix)
    current_step: list[list[int]] = matrix.copy()
    next_step: list[list[int]] = []

    for iteration in range(size):
        column: list[int] = [current_step[col][iteration] for col in range(size)]
        row: list[int] = current_step[iteration]
        for i in range(size):
            next_step.append(current_step[i] if column[i] == 0
                             else [x | y for x, y in zip(current_step[i], row)])
        current_step = next_step.copy()
        next_step = []
    return current_step


# 5
def equivalence_classes(matrix: list[list[int]]) -> list[list[int]]:
    """
    Return equivalence classes of given matrix
    :param matrix: list[list[int]], matrix to process
    :return: list[list[int]], equivalence classes of matrix, list at some index is the class of
    that index

    >>> equivalence_classes([[1, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]])
    [[0], [1, 2], [1, 2], [3]]
    """

    size: int = len(matrix)
    return_list: list[list[int]] = []
    for i in range(size):
        eqv_class: list[int] = []
        for j in range(size):
            if matrix[i][j] == 1:
                eqv_class.append(j)
        return_list.append(eqv_class)

    return return_list


# TODO: remake without numpy and itertools
# def number_of_transitive_closure(n: int) -> int:
#     """
#     Given size of set, calculate the number of transitive closures of relations on given set .
#     :param n: int, size of set
#     :return: int, number of transitive closures of relations on given set
#
#     >>> number_of_transitive_closure(0)
#     1
#     >>> number_of_transitive_closure(1)
#     2
#     >>> number_of_transitive_closure(2)
#     13
#     >>> number_of_transitive_closure(3)
#     171
#     """
#
#     def is_matrix_trans(matrix) -> bool:
#         """
#         Determine if given matrix is transitive.
#         :param matrix: list[list[int]], matrix to process
#         :return: bool, True if matrix is transitive, False otherwise
#         """
#         result = [[int(any(a * b for a, b in zip(A_row, B_col)))
#                    for B_col in zip(*matrix)]
#                   for A_row in matrix]
#         result = [item for row in result for item in row]
#         matrix = [item for row in matrix for item in row]
#         for i, j in zip(result, matrix):
#             if i > j:
#                 return False
#         return True
#
#     count = 0
#     for vals in product([0, 1], repeat=n**2):
#         if vals.count(1) == 1:
#             count += 1
#             continue
#         arr = np.matrix(np.array(vals).reshape((n, n))).tolist()
#         if is_matrix_trans(arr):
#             count += 1
#     return count

# 1.1
file_name = 'Lab_work/matrix.csv'
print(f'Matrix read from "{file_name}" = {read_matrix_from_csv('Lab_work/matrix.csv')}')

# 1.2
M = [[0, 1, 1, 0],
     [0, 0, 0, 0],
     [1, 1, 1, 0],
     [0, 1, 0, 1]]
write_matrix_to_csv('Lab_work/matrix.csv', M)

# 2
M = [[0, 1, 1, 0],
     [0, 0, 0, 0],
     [1, 1, 1, 0],
     [0, 1, 0, 1]]
print(f'{'-'*20}\n{M = }\nReflexive closing of M = {reflexive_closing(M)}')

# 3
M = [[1, 0, 0],
     [1, 1, 1],
     [1, 0, 0]]
print(f'{'-'*20}\n{M = }\nSymmetrical closing of M = {symmetrical_closing(M)}')

# 4
M = [[1, 0, 0, 1],
     [0, 0, 0, 0],
     [1, 1, 1, 0],
     [0, 0, 1, 0]]
print(f'{'-'*20}\n{M = }\nTransitive closing of M = {transitive_closing(M)}')

# 5
M = [[1, 0, 0, 0],
     [0, 1, 1, 0],
     [0, 1, 1, 0],
     [0, 0, 0, 1]]
print(f'{'-'*20}\n{M = }\nEquivalence classes of M = {equivalence_classes(M)}')


if __name__ == "__main__":
    import doctest
    doctest.testmod()
