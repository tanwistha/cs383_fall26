# CS 383 — Bonus Assignment: Build a Hash Table (100 points)

**Released:** Wednesday, Oct 21

**Due:** Wednesday, Oct 28, 11:59 PM (No late submissions)

**Worth:** Bonus - will be counted towards assignments category

## Overview

This is an optional bonus assignment covering the hashing material from
Oct 21st. It's meant to reinforce hash table mechanics before we move
into graphs. It should take a fraction of the time of a regular PA — plan
for roughly the effort of one problem set.

## Part 1 — Implement a Hash Table (80%)

Implement a hash table from scratch supporting the following operations:

- `insert(key, value)` — insert a new key/value pair, or update the value
  if the key already exists
- `search(key)` — return the value associated with `key`, or `None` /
  `null` if the key is not present
- `delete(key)` — remove `key` from the table if it exists

**Collision resolution:** choose **one** of the two strategies we covered
in lecture:

- **Separate chaining**, or
- **Open addressing with linear probing**

State which one you chose in a comment at the top of your file (one
sentence is enough — you don't need to justify it here, that's Part 2).

**Requirements:**

- Use a fixed table size (no need to implement dynamic resizing).
- Any reasonable hash function is fine (e.g., built-in `hash()` in
  Python, or your own) — the point of this assignment is the collision-handling logic, not hash function design.
- Include a small `main` / driver section (or a few lines at the bottom
  of your file) that demonstrates insert, search, and delete working
  correctly on a handful of keys, including at least one deliberate
  collision.

**Submit:** a single source file (`.py`).

## Part 2 — Short Reflection (20%)

Answer the following in a few sentences each. Submit as a short text file
or PDF alongside your code.

1. Why does your chosen collision strategy work, and what's one weakness
   it has compared to the other approach (chaining vs. open addressing)?
2. What happens to your hash table's performance as the load factor
   approaches 1, and why?
3. Give one real-world example where a hash table is a natural fit, and
   one where it's a poor fit.

## Submission

Submit both files (code + reflection) through the usual course submission
system by the deadline above. **Late submissions will not be accepted**, since
this assignment is designed to wrap up before PA4 is released on October 28th, and you will have your project released on October 30th. 

## Grading rubrics Part 1 (80 points)

Suggested breakdown:

| Component | Points | 
|---|---|
| `insert` works correctly, including update-on-duplicate-key | 20 | 
| `search` works correctly, including collision cases | 20 | 
| `delete` works correctly | 20 | 
| Driver / demonstration code shows a deliberate collision handled correctly | 10 | 
| Code clarity / stated collision strategy | 10 | 

## Grading rubrics Part 2 (20 points)

3 questions - writeup. 6-7 points per question. 