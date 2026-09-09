# PA1a — Environment Check + Stack & Queue Basics - 10 points

**Released:** Sep 9 (day of the Stacks & Queues lecture)
**Due:** Sep 18
**Files to submit on Google classroom:** `pa1a_template.py` and `pa1b_template.py` (renamed to your own filename is fine, but keep the class/function names unchanged), plus your short written answer at the bottom of the 2nd file.

This is a short, low-stakes first assignment. Its two goals are: (1) make sure your Python environment and submission process both work, and (2) get comfortable with stack and queue behavior using tools you already know (Python's built-in `list`) — no pointers, no custom node classes, nothing new to build from scratch yet. That comes later in the course.

---

## Part 0 — Environment Check (not graded on content, only on completion)

At the top of [`pa1a_template.py`](https://github.com/tanwistha/cs383_fall26/blob/main/assignments/PA1/pa1a_template.py), replace `YOUR_NAME_HERE` with your name, then run the file. It should print a short greeting with your name and the Python version you're running.

This part exists purely to confirm:
- Python is installed and runs correctly on your machine.
- You can edit, run, and submit a `.py` file through Google classroom.

If this part doesn't run, **ask for help before the due date** — this is exactly the kind of thing TA lab hours are for.

---

## Part 1 — `Stack` (4 methods)

Implement a `Stack` class backed by a Python `list`. A stack is Last-In-First-Out (LIFO) — think of a stack of plates.

| Method | Behavior |
|---|---|
| `push(item)` | Add `item` to the top of the stack. |
| `pop()` | Remove and return the item at the top of the stack. Raise `IndexError` if the stack is empty. |
| `peek()` | Return (without removing) the item at the top of the stack. Raise `IndexError` if the stack is empty. |
| `is_empty()` | Return `True` if the stack has no items, else `False`. |
| `size()` | Return the number of items currently in the stack. |

---

## Part 2 — `Queue` (5 methods)

Implement a `Queue` class backed by a Python `list`. A queue is First-In-First-Out (FIFO) — think of a line at a coffee shop.

| Method | Behavior |
|---|---|
| `enqueue(item)` | Add `item` to the back of the queue. |
| `dequeue()` | Remove and return the item at the front of the queue. Raise `IndexError` if the queue is empty. |
| `peek()` | Return (without removing) the item at the front of the queue. Raise `IndexError` if the queue is empty. |
| `is_empty()` | Return `True` if the queue has no items, else `False`. |
| `size()` | Return the number of items currently in the queue. |

---

# PA1b - Recursion fundamentals and Big-O - 10 points

## Part 1 — implement sum_array and count_halvings functions

Check file [`pa1b_template.py`](https://github.com/tanwistha/cs383_fall26/blob/main/assignments/PA1/pa1a_template.py) and implement the functions per the specifications. 

## Part 2 - Big-O runtime for a recursive function

At the bottom of `pa1b_template.py`, answer the following in a comment:

Q: What is the Big-O running time of `count_halvings(n)` in terms of n?
   Justify your answer by relating the recursion depth to the halving
   pattern from the Sep 9 lecture.

A: <YOUR ANSWER HERE — 2 to 4 sentences>


---

