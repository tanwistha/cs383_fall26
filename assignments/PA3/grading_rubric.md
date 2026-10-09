# Grading Rubric — Assignment 2: Real-Time ER Triage System


---

## Point breakdown

| Component | Points |
|---|---|
| Part 1 — `ERQueue` correctness (all methods, incl. `is_empty` / `__len__`) | 30 |
| Part 2 — Simulation correctness & wait-time report | 30 |
| Tie-breaking handled correctly (Parts 1 & 2) | 10 |
| Part 3 — Complexity write-up | 15 |
| Code quality — naming, structure, comments | 15 |
| **Total** | **100** |
| Part 4 — Bonus (separate file) | +20 |

---

## Part 4 (bonus) — graded separately

Part 4 is optional and distributed as its own file, `er_queue_bonus.py`. It's worth up to **+20**
points added on top of the 100 above (a submission can exceed 100 only via this bonus). 

| Component | Points |
|---|---|
| `HeapERQueue` correctness (same interface/behavior as `ERQueue`) | 5 |
| Benchmark runs, timings reported, and reasonably matches theoretical prediction (heap noticeably faster at n=20,000, especially on `next_patient`) | 5 |
