
# region Import
import numpy as np
from scipy.optimize import fsolve
# endregion

# region Functions
def func(x):
    """
        defines Function #1  -- x-3cos(x)=0
    :param x: x value to be evaluated
    :return: Function 1 evaluated at x
    """
    f = x - 3*np.cos(x)
    return f


def func2(x):
    """
    defines Function #2  - cos(2x) * x^3=0
    :param x: x value to be evaluated
    :return: Function 2 evaluated at x
    """
    f2 = np.cos(2*x)*x**3
    return f2


def findIntersection(x0):
    """
    Uses fsolve to find the intersection point
    :param x0: initial guess, can put np array into it
    :return: root closest to the initial guess
    """
    return fsolve(lambda x : func(x) - func2(x),x0)  # find when func1 - func2 = 0, or func1 = func2


def solver(arr, fcn):
    """
    Solves for the roots of the function, 
    :param arr: the x values to be tested
    :param fcn: the function to be called to return the equation
    :return: roots of the equation in an array
    """

    roots = fsolve(fcn, arr)  # get roots using the arr passing into this function
    newroots = np.unique(np.round(roots, 3))  # round and strip the duplicates of the roots

    return newroots
# endregion

# region Main

def main():
    """
    Hw4 question b
    "Find the roots of the following equations using fsolve from scipy.optimize. Do these functions
    intersect? If so, where?"
    Main function, finds roots and intersects of 2 equations
    :return: prints results to the CLI
    """

    min = -4  # min for guesses
    max = 4  # max for guesses
    arr = np.array([range(min, max)])  # create arr containing the guesses at each integer x value
    print(f"Between x = {min} and x = {max}")  # print the bounds of our guesses

    roots1=solver(arr, func)  # use solver to get roots of func1
    print(f"Roots of Func1: ")
    for i in range(roots1.size):  # prints the roots nicely
        print(f"x={roots1[i]}")
    print()

    roots2=solver(arr, func2)  # use solver to get roots of func2
    print(f"Roots of Func2:")
    for i in range(roots2.size):  # prints the roots nicely
        print(f"x={roots2[i]}")
    print()

    newresult = np.unique(np.round(findIntersection(arr), 3))  # get intersects, round and strip duplicates
    print(f"Intersects between the 2 functions:")
    for i in range(newresult.size):  # prints the intersects nicely
        print(f"x={newresult[i]}")
    pass
# endregion

if __name__ == '__main__':
    main()