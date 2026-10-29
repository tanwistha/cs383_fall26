# Programming Assignment (PA) 4 — Friend Groups

**Graph Fundamentals: BFS, DFS, and Connected Components**

|                  |                                                  |
| ---------------- | ------------------------------------------------ |
| **Points**       | 100                                              |
| **Starter file** | `friend_groups.py` (provided template)           |
| **Bonus**        | Connected components, in the same file (+25 pts, optional) |

---

## Overview

Social networks are graphs. Every person is a node, and every friendship is an edge connecting two
people. Questions like "how are these two people connected?" or "how many separate communities are
in this network?" are graph questions, and they are answered with the two most basic graph
algorithms: **breadth-first search (BFS)** and **depth-first search (DFS)**.

In this assignment you will explore a small friend network. You will start with simple questions
about individual people, implement BFS and DFS yourself, and then use them to decide whether two
people belong to the same friend group. For bonus credit, you can split the whole network into its
**friend groups**, also known as its **connected components**.

## Learning objectives

- Represent an undirected graph as an adjacency list (a Python dictionary).
- Implement BFS with a queue and DFS with recursion, using a `visited` set to avoid repeating work.
- Explain why BFS and DFS visit the same nodes in a different order.
- Use a traversal to decide whether two nodes are connected.
- (Bonus) Find the connected components of a graph by running BFS/DFS repeatedly.

## Background: the friend network

The network is stored as an **adjacency list**: a dictionary that maps each person to a list of
their friends. Friendship goes both ways, so the graph is **undirected**. If `"Bob"` is in
`friends["Alice"]`, then `"Alice"` is in `friends["Bob"]`.

```python
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
```

Picture:

```
    Alice --- Bob
      |        |
    Carol --- Dave --- Eve

    Frank --- Grace          Heidi
```

> **Ordering rule.** Whenever you loop over a person's friends, visit them **in the order they
> appear in the list**. The expected outputs below depend on this. If your BFS or DFS order doesn't
> match, check this rule first.

---

## Part 1 — Warm-up: degree and direct friendship (25 pts)

```python
def degree(graph, person):
    """Return how many friends `person` has."""

def are_friends(graph, a, b):
    """Return True if a and b are DIRECT friends, otherwise False."""
```

| call                                  | expected |
| ------------------------------------- | -------- |
| `degree(friends, "Dave")`             | `3`      |
| `degree(friends, "Heidi")`            | `0`      |
| `are_friends(friends, "Alice", "Bob")` | `True`   |
| `are_friends(friends, "Alice", "Eve")` | `False`  |

---

## Part 2 — Breadth-First Search (25 pts)

```python
def bfs(graph, start):
    """Return a list of people in the order BFS visits them."""
```

Use a queue (`collections.deque`) and a `visited` set. **Mark a person as visited when you add
them to the queue**, not when you remove them. Otherwise the same person can be added twice (Dave
is a friend of both Bob and Carol).

| call                     | expected                                     |
| ------------------------ | -------------------------------------------- |
| `bfs(friends, "Alice")`  | `["Alice", "Bob", "Carol", "Dave", "Eve"]`   |
| `bfs(friends, "Eve")`    | `["Eve", "Dave", "Bob", "Carol", "Alice"]`   |
| `bfs(friends, "Heidi")`  | `["Heidi"]`                                  |

---

## Part 3 — Depth-First Search (25 pts)

```python
def dfs(graph, start):
    """Return a list of people in the order DFS visits them. Use RECURSION."""
```

Your DFS **must be recursive**. A small helper function defined inside `dfs` is fine.

| call                     | expected                                     |
| ------------------------ | -------------------------------------------- |
| `dfs(friends, "Alice")`  | `["Alice", "Bob", "Dave", "Carol", "Eve"]`   |
| `dfs(friends, "Eve")`    | `["Eve", "Dave", "Bob", "Alice", "Carol"]`   |
| `dfs(friends, "Heidi")`  | `["Heidi"]`                                  |

**Written question.** In 3–5 sentences, placed in the module docstring at the top of
`friend_groups.py`, explain **why `bfs` and `dfs` visit the same people but in a different order**.
Connect your answer to the data structure each one uses and to a specific example from the network
above.

---

## Part 4 — Same friend group? (25 pts)

```python
def same_group(graph, a, b):
    """Return True if b can be reached from a through a chain of friends."""
```

Reuse your `bfs` or `dfs`. Don't write a new traversal from scratch.

| call                                      | expected |
| ----------------------------------------- | -------- |
| `same_group(friends, "Alice", "Eve")`     | `True`   |
| `same_group(friends, "Alice", "Frank")`   | `False`  |
| `same_group(friends, "Heidi", "Heidi")`   | `True`   |

---

## Bonus — Connected components (+25 pts, optional)

```python
def friend_groups(graph):
    """Return a list of sets, one set per friend group."""

def count_groups(graph):
    """Return the number of friend groups."""

def largest_group_size(graph):
    """Return the size of the biggest friend group (0 for an empty graph)."""
```

**Idea:** loop over every person in the graph. If they haven't been visited yet, run BFS or DFS from
them. Everyone that traversal reaches forms one group. Add them all to `visited` and continue.

| call                            | expected                                                                 |
| ------------------------------- | ------------------------------------------------------------------------ |
| `friend_groups(friends)`        | `[{"Alice", "Bob", "Carol", "Dave", "Eve"}, {"Frank", "Grace"}, {"Heidi"}]` |
| `count_groups(friends)`         | `3`                                                                      |
| `largest_group_size(friends)`   | `5`                                                                      |

The order of the groups in the list does not matter.

---

## Grading

| Part      | Topic                                                 | Points  |
| --------- | ----------------------------------------------------- | ------- |
| 1         | `degree`, `are_friends`                               | 25      |
| 2         | `bfs`                                                 | 25      |
| 3         | `dfs` (recursive) + written question                  | 25      |
| 4         | `same_group`                                          | 25      |
| **Total** |                                                       | **100** |
| Bonus     | `friend_groups`, `count_groups`, `largest_group_size` | +25     |

Your code will be run on the sample network **and on additional hidden test graphs**. Hard-coding
the expected answers will receive no credit.

**Self-check:** the provided `friend_groups.py` template runs all of the examples above in its
`if __name__ == "__main__":` block and prints `PASS` / `FAIL` for each part. If a part fails, fix it
before moving on. Later parts build on earlier ones.

---

## Constraints & edge cases

- Every person appears as a key in the dictionary, even if they have no friends (empty list).
- The graph is undirected: every friendship is listed in both people's lists.
- The graph may contain cycles (for example, Alice–Bob–Dave–Carol–Alice). Your `visited` set must
  prevent visiting anyone twice or looping forever.
- A person is always in their own friend group (`same_group(g, x, x)` is `True`).
- (Bonus) An empty graph `{}` has `0` groups and a largest group size of `0`.
- Do **not** import any graph library (e.g., `networkx`). `collections.deque` is allowed.
- Do not modify the self-check code at the bottom of the template.

## Submission instructions

- Submit a single file: **`friend_groups.py`**, containing all required functions.
- Put your Part 3 written answer in the docstring at the very top of the file.
- Include your name and roughly how long the assignment took you in the header of the file.
- Your file must run standalone with: `python friend_groups.py`

**Due:** November 9 · **Submit via:** Google classroom

---

*Looking for extra challenge? Complete the Bonus (connected components) for up to +25 points.*
