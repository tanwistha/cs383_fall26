"""
CS 383 Algorithms Analysis and Design
Coin Change: Greedy vs. Dynamic Programming
Points: Individual Effort Assignment (Bonus 2)
        Will be graded towards Assignment category, should you choose to submit it by November 25th.

PROBLEM
    Given a list of coin values and an amount, pay the amount using as
    few coins as possible. Each coin value can be used any number of times.

    Example: coins = [1, 3, 4], amount = 6
        best answer: 3 + 3  (2 coins)

YOUR TASKS
    Part 1. coin_change_greedy  - always take the largest coin that fits
    Part 2. coin_change_dp      - bottom-up dynamic programming table
    
    
    Fill in every place marked TODO. Do not change the function names
    or parameters. Run this file to check your work:

        python coin_change_template.py
"""

from functools import lru_cache


# ======================================================================
# Part 1: Greedy
# ======================================================================
def coin_change_greedy(coins, amount):
    """Pay `amount` by always taking the largest coin that still fits.

    Returns:
        A list of the coins used, e.g. [4, 1, 1].
        None if greedy gets stuck and cannot reach exactly `amount`.

    Hint: sort the coins from largest to smallest, then keep using a
          coin while it still fits in the remaining amount.
    """
    picks = []
    # TODO: implement the greedy rule
    raise NotImplementedError("Part 1: coin_change_greedy")


# ======================================================================
# Part 2: Dynamic programming (bottom-up table)
# ======================================================================
def coin_change_dp(coins, amount):
    """Pay `amount` with the fewest coins, using a DP table.

    Five-step recipe:
        1. Subproblem:  A[x] = fewest coins needed to pay exactly x
        2. Recurrence:  A[x] = 1 + min( A[x - c] )  over coins c <= x
        3. Base case:   A[0] = 0
        4. Order:       fill A[1], A[2], ..., A[amount] (small to large)
        5. Reconstruct: walk back from `amount` using last[x]

    Returns:
        A list of the coins used (any order), e.g. [3, 3].
        None if the amount cannot be paid at all.
    """
    INF = float("inf")
    A = [0] + [INF] * amount        # A[x] = fewest coins for amount x
    last = [None] * (amount + 1)    # last[x] = coin used last to reach x

    # TODO (step 4): fill the table.
    #   For each amount x from 1 to `amount`:
    #       for each coin c:
    #           if c fits (c <= x) and using it improves A[x],
    #           update A[x] and remember c in last[x].

    # TODO: if A[amount] is still INF, return None.

    # TODO (step 5): walk back from `amount` to build the list of coins.
    #   Hint: the last coin used for x is last[x]; what amount is left?

    raise NotImplementedError("Part 2: coin_change_dp")

# ======================================================================
# Self-check (do not modify)
# ======================================================================
def _check():
    tests = [
        # coins,           amount, fewest coins (None = impossible)
        ([1, 5, 10, 25],   63,     6),
        ([1, 3, 4],        6,      2),
        ([1, 10, 25],      30,     3),
        ([4, 5],           8,      2),
        ([5, 10],          3,      None),
        ([2],              0,      0),
    ]
    passed = 0
    for coins, amount, expected in tests:
        print(f"coins={coins}, amount={amount}  (best: {expected})")
        for name, fn in [("greedy", coin_change_greedy),
                         ("dp", coin_change_dp),
                         ("memo", min_coins_memo)]:
            try:
                out = fn(coins, amount)
            except NotImplementedError as e:
                print(f"  {name:6s} not done yet ({e})")
                continue
            if name == "greedy":
                if out is None:
                    note = "(greedy got stuck)"
                elif sum(out) == amount:
                    note = f"(coins add up, {len(out)} coins)"
                else:
                    note = "(WRONG: coins do not add up)"
                print(f"  {name:6s} {out}  {note}")
                continue
            count = out if name == "memo" else (None if out is None else len(out))
            valid = name == "memo" or out is None or sum(out) == amount
            ok = valid and count == expected
            passed += ok
            print(f"  {name:6s} {out}  {'PASS' if ok else 'FAIL'}")
    print(f"\nDP + memo tests passed: {passed} / {2 * len(tests)}")


if __name__ == "__main__":
    _check()
