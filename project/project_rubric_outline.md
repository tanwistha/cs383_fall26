# Grading Rubric: Campus Delivery Route Planner

**100 points: Proposal 15 · Code + Report 60 · Presentation 25**

Every part of this rubric is built around the same four questions.
Tell students this up front — it's the lens the whole project is
graded through, at every stage:

1. **Modeling** — did they represent the problem correctly?
2. **Justification** — did they choose their approach for good reasons?
3. **Implementation** — does it actually work?
4. **Evaluation** — did they measure it honestly and understand the results?

Since teams choose their own data structures and algorithms, nothing
below rewards a *specific* choice. It rewards doing each of the four
things well, whatever the choice was.

---

## Proposal — 15 pts

The proposal previews questions 1 and 2, since students haven't
implemented anything yet.

| Lens | What we're looking for | Pts |
|---|---|---|
| **Modeling** | Correctly describes the problem: what the graph represents, what a request is, what the capacity constraint means in practice | 5 |
| **Justification** | Names a planned approach and gives real reasons for it, not just a label | 5 |
| — | Realistic division of labor across the team | 3 |
| — | Names something they expect to be hard | 2 |

The point is to get teams thinking early, not
to hold them to a contract.

---

## Code + Report — 60 pts (15 per lens)

### 1. Modeling — 15 pts

Did they represent the problem correctly, in a way that actually
supports what they needed to compute?

| Criterion | Pts |
|---|---|
| Buildings and pathways are represented in a way that supports efficient lookups (not, e.g., re-scanning a flat list for every distance query) | 5 |
| Delivery requests, priority, and capacity are represented in a way that the solver can actually use — not just stored, but structured for the decisions the solver needs to make | 5 |
| The representation matches the problem's real constraints (e.g., capacity is checked against what's carried *at once*, not total demand) | 5 |

A team that chose a simple representation because the problem didn't
need anything fancier, and says so, should score well here. This isn't
about complexity for its own sake.

### 2. Justification — 15 pts

Did they choose their algorithm(s) for good, stated reasons — and do
those reasons hold up?

| Criterion | Pts |
|---|---|
| Explains *why* each algorithm/structure was chosen for its role, not just names it | 6 |
| Complexity analysis of the main components, and it's consistent with what they actually measured | 5 |
| Shows awareness of at least one alternative they didn't choose, and why | 4 |

"We used a hash table for request lookup because we needed O(1) access
by request ID, and here's where that mattered" is a strong answer. "We
used a hash table" with no reasoning is not, even if the code works.

### 3. Implementation — 15 pts

Does it actually work?

| Criterion | Pts |
|---|---|
| Valid plans on MEDIUM and FULL, verified with `check_solution()` | 8 |
| Runs from a clean download without manual fixing | 3 |
| Code is readable and reasonably organized — a grader (or teammate) can follow it | 4 |

This is the one lens that's mostly binary: it works or it doesn't. A
plan that fails `check_solution()` caps this section hard, regardless
of how sophisticated the underlying idea was.


### 4. Evaluation — 15 pts



| Criterion | Pts |
|---|---|
| Compared at least two approaches, with real cost and runtime numbers for both | 6 |
| Scaling result across SMALL/MEDIUM/FULL, with runtime and cost reported and discussed | 5 |
| Brute-force comparison on SMALL, with honest interpretation (including if their solver beat the sequential baseline — see DATASET_GUIDE.txt) | 4 |


---

## Presentation — 25 pts

~15 minutes + questions. Same four lenses, now under live questioning.

