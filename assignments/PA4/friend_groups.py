"""
PA4 -- Friend Groups: Graph Fundamentals

Name (Include your and your team member's names if applicable):
Approximate time spent on this assignment:

Part 3 written answer (replace this with your 3-5 sentence explanation):
    Why do bfs() and dfs() visit the same people but in a different order?

"""

from collections import deque


# ----------------------------------------------------------------------
# Sample network used by the self-checks. Do NOT modify it.
#
#     Alice --- Bob
#       |        |
#     Carol --- Dave --- Eve
#
#     Frank --- Grace          Heidi
# ----------------------------------------------------------------------
friends = {
    "Alice": ["Bob", "Carol"],
    "Bob":   ["Alice", "Dave"],
    "Carol": ["Alice", "Dave"],
    "Dave":  ["Bob", "Carol", "Eve"],
    "Eve":   ["Dave"],
    "Frank": ["Grace"],
    "Grace": ["Frank"],
    "Heidi": [],
}


# ----------------------------------------------------------------------
# Part 1 -- Warm-up (25 pts)
# ----------------------------------------------------------------------
def degree(graph, person):
    """Return how many friends `person` has."""
    # TODO
    raise NotImplementedError


def are_friends(graph, a, b):
    """Return True if a and b are DIRECT friends, otherwise False."""
    # TODO
    raise NotImplementedError


# ----------------------------------------------------------------------
# Part 2 -- Breadth-First Search (25 pts)
# ----------------------------------------------------------------------
def bfs(graph, start):
    """Return a list of people in the order BFS visits them.

    - Use a queue (collections.deque) and a `visited` set.
    - Mark a person as visited when you ADD them to the queue.
    - Visit neighbors in the order they appear in the list.
    """
    # TODO
    raise NotImplementedError


# ----------------------------------------------------------------------
# Part 3 -- Depth-First Search (25 pts)
# ----------------------------------------------------------------------
def dfs(graph, start):
    """Return a list of people in the order DFS visits them.

    - Must use RECURSION (a helper function inside dfs is fine).
    - Visit neighbors in the order they appear in the list.
    """
    # TODO
    raise NotImplementedError


# ----------------------------------------------------------------------
# Part 4 -- Same friend group? (25 pts)
# ----------------------------------------------------------------------
def same_group(graph, a, b):
    """Return True if b can be reached from a through a chain of friends.

    Hint: reuse your bfs() or dfs().
    """
    # TODO
    raise NotImplementedError


# ----------------------------------------------------------------------
# BONUS -- Connected components (+25 pts, optional)
# ----------------------------------------------------------------------
def friend_groups(graph):
    """Return a list of sets, one set per friend group.

    Idea: loop over every person. If they haven't been visited yet, run
    BFS/DFS from them; everyone it reaches forms one group.
    """
    # TODO (optional)
    raise NotImplementedError


def count_groups(graph):
    """Return the number of friend groups."""
    # TODO (optional)
    raise NotImplementedError


def largest_group_size(graph):
    """Return the size of the biggest friend group (0 for an empty graph)."""
    # TODO (optional)
    raise NotImplementedError


# ----------------------------------------------------------------------
# Self-checks -- do NOT modify below this line.
# Run with:  python friend_groups.py
# Passing these checks is necessary but not sufficient: your code will
# also be graded on additional hidden test graphs.
# ----------------------------------------------------------------------
def _run_checks():
    def as_set_of_frozensets(groups):
        return {frozenset(g) for g in groups}

    checks = {
        "Part 1": lambda: (
            degree(friends, "Dave") == 3
            and degree(friends, "Heidi") == 0
            and are_friends(friends, "Alice", "Bob") is True
            and are_friends(friends, "Alice", "Eve") is False
        ),
        "Part 2": lambda: (
            bfs(friends, "Alice") == ["Alice", "Bob", "Carol", "Dave", "Eve"]
            and bfs(friends, "Eve") == ["Eve", "Dave", "Bob", "Carol", "Alice"]
            and bfs(friends, "Heidi") == ["Heidi"]
        ),
        "Part 3": lambda: (
            dfs(friends, "Alice") == ["Alice", "Bob", "Dave", "Carol", "Eve"]
            and dfs(friends, "Eve") == ["Eve", "Dave", "Bob", "Alice", "Carol"]
            and dfs(friends, "Heidi") == ["Heidi"]
        ),
        "Part 4": lambda: (
            same_group(friends, "Alice", "Eve") is True
            and same_group(friends, "Alice", "Frank") is False
            and same_group(friends, "Heidi", "Heidi") is True
        ),
        "Bonus": lambda: (
            as_set_of_frozensets(friend_groups(friends)) == {
                frozenset({"Alice", "Bob", "Carol", "Dave", "Eve"}),
                frozenset({"Frank", "Grace"}),
                frozenset({"Heidi"}),
            }
            and len(friend_groups(friends)) == 3
            and count_groups(friends) == 3
            and largest_group_size(friends) == 5
        ),
    }

    for name, check in checks.items():
        try:
            result = "PASS" if check() else "FAIL"
        except NotImplementedError:
            result = "not implemented yet"
        except Exception as e:  # show the error but keep checking other parts
            result = f"ERROR ({type(e).__name__}: {e})"
        print(f"{name:7s} {result}")


if __name__ == "__main__":
    _run_checks()
