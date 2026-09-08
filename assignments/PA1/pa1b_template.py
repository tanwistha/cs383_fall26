"""
PA1b - Recursion, Logarithms & Complexity
S 383 - Algorithm Analysis and Design 

=====================================================================
WRITTEN ANSWER — Problem 2, Part B (required)
=====================================================================
Q: What is the Big-O running time of count_halvings(n) in terms of n?
   Justify your answer by relating the recursion depth to the halving
   pattern from the Sep 9 lecture.

A: <YOUR ANSWER HERE — 2 to 4 sentences>

=====================================================================
"""


def sum_array(arr):
    """
    PROBLEM 1

    Return the sum of all elements in arr, computed recursively.

    Rules:
      - No loops (for/while).
      - No built-in sum().
      - Must have a base case and a recursive case.

    Parameters
    ----------
    arr : list[int | float]
        May be empty.

    Returns
    -------
    int | float
        sum_array([]) should return 0.

    Examples
    --------
    >>> sum_array([])
    0
    >>> sum_array([1, 2, 3, 4])
    10
    """
    # TODO: base case
    # if ...:
    #     return ...

    # TODO: recursive case
    # return ... + sum_array(...)

    raise NotImplementedError("Implement sum_array")


def count_halvings(n):
    """
    PROBLEM 2, PART A

    Return the number of times n can be divided by 2 (integer division)
    until it reaches 1.

    Rules:
      - n is always a positive integer (n >= 1).
      - No loops (for/while).
      - No math.log / math.log2 / any built-in logarithm function.
      - Must have a base case and a recursive case.

    Parameters
    ----------
    n : int
        n >= 1.

    Returns
    -------
    int

    Examples
    --------
    >>> count_halvings(1)
    0
    >>> count_halvings(16)
    4
    >>> count_halvings(1000000)
    19
    """
    # TODO: base case
    # if ...:
    #     return ...

    # TODO: recursive case (integer division: n // 2)
    # return ... + count_halvings(...)

    raise NotImplementedError("Implement count_halvings")


if __name__ == "__main__":
    # Quick manual sanity checks.
    print(sum_array([1, 2, 3, 4]))     # expect 10
    print(count_halvings(16))          # expect 4
