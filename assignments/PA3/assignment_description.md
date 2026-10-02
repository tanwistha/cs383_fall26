# Programming Assignment (PA) 3 — Real-Time Emergency Room Triage System

**Priority Queues in Practice**

| | |
|---|---|
| **Points** | 100 |
| **Starter file** | `er_queue.py` (provided template) |
| **Bonus** | See separate file `er_queue_bonus.py` (+20 pts, optional) |

---

## Overview

Hospitals don't treat patients in the order they walk in — they treat them in the order of medical
urgency. The person having a heart attack is seen before the person with a sprained ankle, even if
the ankle arrived first. This is a priority queue, running live, on real people.

In this assignment you will build exactly that system: a priority-queue engine that processes a
real-time stream of patient arrivals and "doctor becomes available" events, in chronological order,
and reports what actually happened — who was treated, in what order, and how long each patient
waited.

## Learning objectives

- Implement a priority queue ADT from scratch, backed by a plain Python list.
- Correctly reason about and report the time complexity of each operation you write.
- Integrate a priority queue into a larger event-driven system — not just call its methods in
  isolation.

## Background: the Emergency Severity Index

Real emergency rooms score every incoming patient on the **Emergency Severity Index (ESI)**, a scale
from **1** (most critical — immediate life threat) to **5** (least urgent — minor issue). Lower
number = higher priority. Your system models this directly: it is a **MIN-priority queue**. The next
patient treated is always the one with the smallest ESI level currently waiting.

> **Tie-breaking rule.** Two patients can share the same ESI level. When they do, whoever arrived
> first is treated first — exactly like a real waiting room. Your implementation must break ties by
> `arrival_time`, not by insertion order into your data structure (the two are not always the same
> once you get to Part 2).

---

## Part 1 — Warm-up: the `ERQueue` class


Implement a class `ERQueue` backed by a plain Python list (no `heapq`, no sorting library — the point
of this part is to practice the elementary implementation ideas from lecture). Your class must
support:

```python
class ERQueue:
    def __init__(self):
        ...

    def add_patient(self, patient_id, esi_level, arrival_time):
        """Add a patient. esi_level is an int 1-5 (1 = most critical)."""
        ...

    def next_patient(self):
        """Remove and return the (patient_id, esi_level, arrival_time)
        of the highest-priority waiting patient. Raise IndexError if
        the queue is empty."""
        ...

    def peek_next(self):
        """Same answer as next_patient(), without removing it."""
        ...

    def is_empty(self):
        ...

    def __len__(self):
        ...
```

You may implement `add_patient` and `next_patient` using either the "unordered list" or "sorted
list" approach from lecture — your choice. Part 3 asks you to state which you picked and why.

---

## Part 2 — The real-time simulation

A real ER doesn't process requests one at a time in a vacuum — patients keep arriving while others
are being treated. You'll simulate this with an **event log**: a list of timestamped events, already
sorted by time, that your code plays back in order.

```python
# Each event is a tuple: (timestamp, event_type, payload)
#
#   (time, "ARRIVE", (patient_id, esi_level))   — a new patient walks in
#   (time, "TREAT",  None)                      — a doctor becomes free
#
# Example:
events = [
    (0,  "ARRIVE", ("P1", 3)),
    (2,  "ARRIVE", ("P2", 1)),
    (5,  "TREAT",  None),
    (6,  "ARRIVE", ("P3", 3)),
    (9,  "TREAT",  None),
    (9,  "ARRIVE", ("P4", 2)),
    (12, "TREAT",  None),
    (20, "TREAT",  None),
]
```

Write:

```python
def run_simulation(events, queue):
    """
    Play back `events` in order on `queue` (an ERQueue).
    On every TREAT event, call next_patient() and record:
        - the timestamp treatment started
        - the patient_id treated
        - their wait time = (treatment timestamp - arrival_time)
    A TREAT event with nobody waiting is simply skipped (the
    doctor waits idle) — do not raise an error.
    Return the list of treatment records, in the order they occurred.
    """
    ...
```

For the example event log above, using ties broken by arrival time, your simulation should produce:

| time | patient treated | esi | wait time |
|---|---|---|---|
| 5  | P2 | 1 | 3  |
| 9  | P1 | 3 | 9  |
| 12 | P4 | 2 | 3  |
| 20 | P3 | 3 | 14 |

At the end of the run, print the total number of patients treated, and their average wait time. (For
the example above: 4 patients, average wait = 7.25.)

**Self-check:** the provided `er_queue.py` template runs this exact example in its `if __name__ ==
"__main__":` block and asserts your output matches the table above. If the asserts fail, your queue
or your simulation has a bug — fix it before moving on.

---

## Part 3 — Complexity write-up


In a short paragraph (4–6 sentences), placed in the module docstring at the very top of
`er_queue.py`, state the Big-O of `add_patient` and `next_patient` for the implementation you chose
in Part 1, and explain why — in your own words, connecting your explanation to the specific line(s)
of your code responsible for that cost. This is the same style of reasoning from lecture: don't just
name the complexity, show where it comes from.

---

## Constraints & edge cases

- ESI levels are integers 1–5 inclusive (1 = most critical).
- `arrival_time` and event timestamps are non-negative integers; the event list is already sorted by
  timestamp.
- Multiple patients may share the exact same `arrival_time`.
- `next_patient()` / `peek_next()` on an empty queue must raise `IndexError` — do not return `None`
  silently.
- A `TREAT` event when the queue is empty means the doctor is idle; skip it without error (see Part
  2).

## Submission instructions

- Submit a single file: **`er_queue.py`**, containing `ERQueue` and `run_simulation`.
- Put your Part 3 write-up in the docstring at the very top of the file.
- Include a header comment with your name, and roughly how long the assignment
  took you.
- Your file must run standalone with: `python er_queue.py`

**Due:** Oct 12 · **Submit via:** Google classroom

---

*Looking for extra challenge? See the separate bonus assignment, `er_queue_bonus.py`, worth up to +20
points.*
