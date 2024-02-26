import numpy as np

# region Archived
# def solver(a, b):
#     """
#     Solves the system of equations given by a and b in the form of matrices
#     :param a: matrix of coefficients
#     :param b: matrix of answers for the system
#     :return: the solutions of the system in an array
#     """
#     results = np.linalg.solve(a, b)  # using numpy function to solve system
#     return results
#
#
# def main():
#     """
#     Solves the system of equations, has options for 2x2-5x5 matrices
#     :return: Prints the solutions to the CLI
#     """
#
#     # 2x2 Matrices, True to use, False to not use.
#     two = False
#     if two is True:
#         a2 = np.array([[4, 2], [5, 2]])  # defining matrix a
#         b2 = np.array([14, 16])  # defining matrix b
#         xtwo = np.round(solver(a2, b2), 3)  # solving for x1,x2,...
#         num_rows, num_cols = a2.shape  # getting measurements
#         for i in range(num_rows):  # for each row print the first equation from this system
#             print(f"({a2[i][0]})•x1 + ({a2[i][1]})•x2 = {b2[i]}")
#         for i in range(xtwo.size):  # prints the x values nicely
#             print(f"x{i + 1}={xtwo[i]}")
#         print()  # space for prettiness
#
#     # 3x3 Matrices, True to use, False to not use.
#     thr = True
#     if thr is True:
#         a3 = np.array([[3, 1, -1], [1, 4, 1], [2, 1, 2]])  # defining matrix a
#         b3 = np.array([2, 12, 10])  # defining matrix b
#         xthr = np.round(solver(a3, b3), 3)  # solving for x1,x2,...
#         num_rows, num_cols = a3.shape  # getting measurements
#         for i in range(num_rows):  # for each row print the first equation from this system
#             print(f"({a3[i][0]})•x1 + ({a3[i][1]})•x2 + ({a3[i][2]})•x3 = {b3[i]}")
#         for i in range(xthr.size):  # prints the x values nicely
#             print(f"x{i + 1}={xthr[i]}")
#         print()  # space for prettiness
#
#     # 4x4 Matrices, True to use, False to not use.
#     four = True
#     if four is True:
#         a4 = np.array([[1, -10, 2, 4], [3, 1, 4, 12], [9, 2, 3, 4], [-1, 2, 7, 3]])  # defining matrix a
#         b4 = np.array([2, 12, 21, 37])  # defining matrix b
#         xfour = np.round(solver(a4, b4), 3)  # solving for x1,x2,...
#         num_rows, num_cols = a4.shape  # getting measurements
#         for i in range(num_rows):  # for each row print the first equation from this system
#             print(f"({a4[i][0]})•x1 + ({a4[i][1]})•x2 + ({a4[i][2]})•x3 + ({a4[i][3]})•x4 = {b4[i]}")
#         for i in range(xfour.size):  # prints the roots nicely
#             print(f"x{i + 1}={xfour[i]}")
#         print()  # space for prettiness
#
#     five = False
#     if five is True:
#         # defining matrix a
#         a5 = np.array([[1, -10, 2, 4, 3], [3, 1, 4, 12, 7], [9, 2, 3, 4, 1], [-1, 2, 7, 3, 3], [4, 2, 7, 4, 2]])
#         b5 = np.array([2, 12, 21, 37, 32])  # defining matrix b
#         xfive = np.round(solver(a5, b5), 3)  # solving for x1,x2,...
#         num_rows, num_cols = a5.shape  # getting measurements
#         for i in range(num_rows):  # for each row print the first equation from this system
#             print(f"({a5[i][0]})•x1 + ({a5[i][1]})•x2 + ({a5[i][2]})•x3 + ({a5[i][3]})•x4 + ({a5[i][4]})•x5 = {b5[i]}")
#         for i in range(xfive.size):  # prints the roots nicely
#             print(f"x{i + 1}={xfive[i]}")
#         print()  # space for prettiness
# endregion

# region Solver
def solver(a, b):
    """
    Solves the system of equations given by a and b in the form of matrices
    :param a: matrix of coefficients
    :param b: matrix of answers for the system
    :return: the solutions of the system in an array
    """
    results = np.linalg.solve(a, b)  # using numpy function to solve system
    return results

def print_system(a, b, x):
    """
    Prints the system of equations and their solutions dynamically for any size of matrices
    :param a: Coefficient matrix
    :param b: Answers matrix
    :param x: Solutions matrix
    """
    num_rows, num_cols = a.shape
    for i in range(num_rows):
        equation = " + ".join(f"({a[i][j]})•x{j+1}" for j in range(num_cols)) + f" = {b[i]}"
        print(equation)
    for i, xi in enumerate(x):
        print(f"x{i+1}={xi}")
    print()  # space for prettiness

# endregion

# region Main

def main():
    """
    Solves the system of equations, has options for 2x2-5x5 matrices
    :return: Prints the solutions to the CLI
    """
    # Example usage for a 3x3 matrix
    a3 = np.array([[3, 1, -1], [1, 4, 1], [2, 1, 2]])  # defining matrix a
    b3 = np.array([2, 12, 10])  # defining matrix b
    x3 = np.round(solver(a3, b3), 3)  # solving for x1,x2,...
    print_system(a3, b3, x3)

    a4 = np.array([[1, -10, 2, 4], [3, 1, 4, 12], [9, 2, 3, 4], [-1, 2, 7, 3]])  # Defining matrix a
    b4 = np.array([2, 12, 21, 37])  # Defining matrix b
    x4 = np.round(solver(a4, b4), 3)  # Solving for the solutions
    print_system(a4, b4, x4)

    # Add more matrices of different sizes here and use print_system to print them

# endregion

if __name__ == '__main__':
    main()


