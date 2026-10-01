"""
Programming Assignment 2 (PA2) - Merge Sort vs. Quicksort
=========================================================

Assignment Overview
--------------------
You will implement two classic divide-and-conquer sorting algorithms
and compare them empirically:

    1. MERGE SORT      -- split the array in half, sort each half
                           recursively, then merge the two sorted
                           halves back together.
    2. QUICKSORT        -- pick a PIVOT element, partition the array
                           into "less than pivot" and "greater than
                           pivot", sort each side recursively.

Both are divide-and-conquer: break the problem into smaller
subproblems, solve them recursively, combine the results. The
interesting difference is WHERE the work happens: merge sort does its
work when COMBINING (the merge step); quicksort does its work when
DIVIDING (the partition step). That difference has real consequences,
which you'll measure in Part 3.

For quicksort, HOW you pick the pivot matters a great deal. You'll
implement two different pivot strategies and compare them.

Required functions
--------------------
    1. merge_sort(arr)                    -- Part 1
    2. quicksort_first_pivot(arr)         -- Part 2a
    3. quicksort_random_pivot(arr)        -- Part 2b
    4. describe_complexity()              -- Part 3 (written analysis,
                                              returned as a dict)

A benchmark script (benchmark.py) is provided separately for Part 3
(the runtime experiments) -- you don't need to write that part, just
run it once your four functions above are implemented.

Instructions
------------
Implement each function below. Do not change the function signatures.
None of these should sort in place -- each should return a NEW sorted
list, leaving the input list unmodified. This makes it easy to compare
methods on the exact same input in the benchmark script.

Do not use Python's built-in sorted() or list.sort() anywhere in your
implementations -- the whole point is to build these yourself.
"""

import random


# ---------------------------------------------------------------------------
# Part 1: Merge sort
# ---------------------------------------------------------------------------

def merge_sort(arr):
    """
    Sort a list using merge sort.

    Args:
        arr: a list of comparable values (e.g. ints or floats).

    Returns:
        A NEW list containing the same elements as `arr`, in ascending
        order. Does not modify `arr`.

    Notes:
        - Base case: a list of length 0 or 1 is already sorted.
        - Recursive case: split `arr` into two halves, sort each half
          with a recursive call to merge_sort, then MERGE the two
          sorted halves back into one sorted list. You'll need a
          helper function for the merge step -- write one.
        - The merge step should be a single linear pass through both
          halves, comparing their front elements and taking the
          smaller one each time.
    """
    # TODO: implement (you may add a helper merge() function)
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Part 2a: Quicksort with a FIRST-ELEMENT pivot
# ---------------------------------------------------------------------------

def quicksort_first_pivot(arr):
    """
    Sort a list using quicksort, always choosing the FIRST element of
    the current sublist as the pivot.

    Args:
        arr: a list of comparable values.

    Returns:
        A NEW sorted list. Does not modify `arr`.

    Notes:
        - Base case: a list of length 0 or 1 is already sorted.
        - Recursive case: pick arr[0] as the pivot. Partition the rest
          of the list into elements less than the pivot and elements
          greater than or equal to the pivot. Recursively sort each
          partition, then combine: sorted(less) + [pivot] + sorted(geq).
        - Think about what kind of input makes this pivot choice a bad
          idea. You'll investigate this directly in Part 3.
    """
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Part 2b: Quicksort with a RANDOM pivot
# ---------------------------------------------------------------------------

def quicksort_random_pivot(arr):
    """
    Sort a list using quicksort, choosing a RANDOM element of the
    current sublist as the pivot each time.

    Args:
        arr: a list of comparable values.

    Returns:
        A NEW sorted list. Does not modify `arr`.

    Notes:
        - Same structure as quicksort_first_pivot, except the pivot is
          chosen with random.choice(arr) instead of always arr[0].
        - Handle duplicate values properly: elements equal to the
          pivot should end up in neither the "less than" nor "greater
          than" partition being recursed on again (otherwise a list of
          many equal values could recurse forever, or at least very
          inefficiently). Put pivot-equal elements in their own group.
    """
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Part 3: Explain the Big-O
# ---------------------------------------------------------------------------

def describe_complexity():
    """
    Return a dict describing the time and space complexity of the
    algorithms you implemented above, in your own words but using
    correct Big-O notation.

    Returns:
        A dict with these keys, each mapping to a short string:
            - "merge_sort_time_best"     e.g. "O(n log n)"
            - "merge_sort_time_worst"    e.g. "O(n log n)"
            - "merge_sort_space"         e.g. "O(n)"
            - "quicksort_time_best"      e.g. "O(n log n)"
            - "quicksort_time_worst"     e.g. "O(n^2)"
            - "quicksort_space"          e.g. "O(log n)" or "O(n)"
            - "why_pivot_matters"        a 2-3 sentence explanation, in
                                          your own words, of why the
                                          pivot strategy affects
                                          quicksort's worst case but
                                          does NOT affect merge sort at
                                          all.

    Notes:
        Merge sort's time complexity does not depend on the input's
        original order -- it's the same in the best, average, and
        worst case. Quicksort's does. Your answer for
        "why_pivot_matters" should explain WHY that asymmetry exists,
        referring to what each algorithm actually does with its pivot
        (or lack thereof) at each step.
    """
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Provided test harness -- do not remove these checks.
# ---------------------------------------------------------------------------

def _is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


if __name__ == "__main__":
    import copy

    test_cases = [
        [],
        [1],
        [2, 1],
        [5, 3, 8, 1, 9, 2, 7],
        [1, 1, 1, 1],
        [4, 2, 4, 1, 4, 3],          # duplicates
        list(range(50, 0, -1)),      # already reverse-sorted
        list(range(50)),             # already sorted
    ]

    for arr in test_cases:
        original = copy.deepcopy(arr)

        result_m = merge_sort(arr)
        assert _is_sorted(result_m), f"merge_sort failed on {original}"
        assert sorted(result_m) == sorted(original), f"merge_sort lost/changed elements on {original}"
        assert arr == original, "merge_sort must not modify its input"

        result_f = quicksort_first_pivot(arr)
        assert _is_sorted(result_f), f"quicksort_first_pivot failed on {original}"
        assert sorted(result_f) == sorted(original), f"quicksort_first_pivot lost/changed elements on {original}"
        assert arr == original, "quicksort_first_pivot must not modify its input"

        result_r = quicksort_random_pivot(arr)
        assert _is_sorted(result_r), f"quicksort_random_pivot failed on {original}"
        assert sorted(result_r) == sorted(original), f"quicksort_random_pivot lost/changed elements on {original}"
        assert arr == original, "quicksort_random_pivot must not modify its input"

    print("All correctness tests passed!")

    info = describe_complexity()
    required_keys = {
        "merge_sort_time_best", "merge_sort_time_worst", "merge_sort_space",
        "quicksort_time_best", "quicksort_time_worst", "quicksort_space",
        "why_pivot_matters",
    }
    assert required_keys.issubset(info.keys()), f"missing keys: {required_keys - info.keys()}"
    assert all(isinstance(v, str) and len(v) > 0 for v in info.values())

    print("\nYour complexity analysis:")
    for key in ["merge_sort_time_best", "merge_sort_time_worst", "merge_sort_space",
                "quicksort_time_best", "quicksort_time_worst", "quicksort_space"]:
        print(f"  {key}: {info[key]}")
    print(f"  why_pivot_matters: {info['why_pivot_matters']}")

    # TODO (optional): add your own additional test cases below --
    # e.g. a list of all-equal elements, a very small list, or a list
    # with negative numbers.
