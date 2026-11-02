# Team Project: Campus Delivery Route Planner

**Teams of 3**

| | |
|---|---|
| Project announced | Mon Nov 2 |
| Proposal due | Fri Nov 20 |
| Code + report due | Wed Dec 9 (online) |
| Presentations (15 mins) | Wed Dec 16 1-4 PM (in class) |

Graded components: **Proposal 15% · Code + Report 60% · Presentation 25%**

---

## The problem

A delivery agent starts at a campus mail center, needs to carry out a
list of delivery requests (each with a pickup building and a dropoff
building), and returns to the start. The agent can carry more than one
item at once, up to a weight limit.

**Your job: decide the order to do everything in, so total travel
distance is as small as possible.**

You're given three small CSV files (`buildings.csv`, `pathways.csv`,
`deliveries.csv`) — see `DATASET_GUIDE.txt` for exact columns and the
fixed constants (where the agent starts, the weight limit). Every team
gets the same data, so your results are directly comparable to every
other team's.

---

## What we are not telling you

We are not telling you which data structures or algorithms to use.

This semester you've built linear and binary search, sorting, heaps
and priority queues, BSTs, hash tables, graph traversal, Dijkstra,
minimum spanning trees, dynamic programming, and greedy algorithms.
Deciding which of those belong here — and how to combine them — is the
project.

There is no single intended solution. As examples only (not
requirements): one team might combine a hash table, a priority queue,
and Dijkstra. Another might use Dijkstra plus dynamic programming on a
small piece of the problem. Another might do something not on this
list. All are legitimate starting points. Your report should explain
and defend whatever your team actually chose.

A natural first idea is a greedy one — always go to the nearest useful
stop next. That's a fine place to start. Whether it's a fine place to
*stop* is exactly the kind of question your empirical results should
answer.

### How this gets evaluated

Every part of this project — proposal, report, presentation — is
graded through the same four questions. Keep them in mind from day
one:

1. **Modeling** — did you represent the problem correctly? (The graph,
   the requests, the capacity constraint — in a form your solver can
   actually use.)
2. **Justification** — did you choose your approach for real, stated
   reasons, not just because it was the first idea?
3. **Implementation** — does it actually work?
4. **Evaluation** — did you measure it honestly, and do you understand
   what the numbers mean?

See `project_rubric.md` for exactly how these are weighted at each
stage. A team that's strong on all four scores far better than a team
with clever code but no real justification or evaluation for it.

---

## What you must produce

**A solver** matching the format in `delivery_scaffold.py`, plus
`check_solution()` — an independent checker included in that file that
tells you whether your plan is legal and what it costs. Run it
constantly.

### Required results

1. **A working, valid plan** for the MEDIUM and FULL delivery sets
   (see `DATASET_GUIDE.txt` for what those mean).
2. **A comparison of at least two approaches** — for example a fast
   heuristic against something more careful, or two different rules
   for deciding what to do next. Report the cost and running time of
   each.
3. **A small scaling check**: run your solver on SMALL, MEDIUM, and
   FULL, and report how running time and total cost change as the
   number of deliveries grows.
4. **One result comparing against the SMALL brute-force baseline**
   described in `DATASET_GUIDE.txt`.

Result 4 usually produces the most interesting sentence in a team's
report — don't skip it.

---

## Scope — please read

Not required, and not rewarded:

- No web app, database, or graphical interface. Clean text output is fine.
- No multiple delivery agents. One agent.
- No requests arriving mid-shift. The full list is known up front.

If you find yourselves building infrastructure instead of working on
the routing problem, stop and talk to me. A map or chart is a fine
*optional* extra once your solver works — not before.

---

## Deliverables

**Proposal — due Fri Nov 20 (15%).** One page: your planned approach,
the structures you expect to use, who owns what, and what you expect
to be hardest.

**Code + report — due Thu Dec 10, online (60%).** Your code, plus a
few pages of report covering your approach, why you chose it, and your
four required results.

**Presentation — Wed Dec 16 (25%).** ~15 minutes plus questions. Live
demo. All members present and able to speak to any part of the code.

---

## A suggested first step

Get *any* legal plan working, however bad — greedy nearest-neighbor is
fine. A poor plan that passes `check_solution()` in week one is worth
far more than an elegant one that doesn't exist until week four.
Everything after that is improvement.
