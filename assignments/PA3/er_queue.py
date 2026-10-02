"""
Programming Assignment 3 -- Real-Time Emergency Room Triage System
Parts 1-3

Time spent:

--------------------------------------------------------------------------
PART 3 -- COMPLEXITY WRITE-UP  (fill this in, 4-6 sentences)
--------------------------------------------------------------------------
State the Big-O of add_patient and next_patient for the implementation you
chose below, and explain why -- connect your explanation to the specific
line(s) of your code responsible for that cost.

    add_patient:  O(???)
    next_patient: O(???)

    (your explanation here)

--------------------------------------------------------------------------
"""


class ERQueue:
    """A MIN-priority queue of ER patients, ordered by ESI level (1 = most
    critical). Ties are broken by arrival_time: whoever arrived first is
    treated first.

    Implement this using a PLAIN PYTHON LIST -- no heapq, no sorting
    library. You may use either the "unordered list" approach (fast
    add_patient, slow next_patient) or the "sorted list" approach (the
    reverse) from lecture. Either is acceptable; Part 3 asks which you
    picked and why.
    """

    def __init__(self):
        # TODO: pick your internal representation, e.g. self.a = []
        ...

    def add_patient(self, patient_id, esi_level, arrival_time):
        """Add a patient.

        patient_id:  any hashable identifier for the patient (e.g. a string)
        esi_level:   int, 1-5 (1 = most critical)
        arrival_time: non-negative int, the simulated time they arrived
        """
        # TODO
        ...

    def next_patient(self):
        """Remove and return the (patient_id, esi_level, arrival_time) of
        the highest-priority waiting patient (lowest esi_level; ties broken
        by earliest arrival_time).

        Raise IndexError if the queue is empty.
        """
        # TODO
        ...

    def peek_next(self):
        """Same answer as next_patient(), without removing it.

        Raise IndexError if the queue is empty.
        """
        # TODO
        ...

    def is_empty(self):
        """Return True if there are no patients waiting."""
        # TODO
        ...

    def __len__(self):
        """Return the number of patients currently waiting."""
        # TODO
        ...


def run_simulation(events, queue):
    """Play back `events` in order on `queue` (an ERQueue).

    events: a list of (timestamp, event_type, payload) tuples, already
            sorted by timestamp, where event_type is one of:

                "ARRIVE"  payload = (patient_id, esi_level)
                "TREAT"   payload = None

    On every TREAT event, call queue.next_patient() and record a tuple:

        (timestamp, patient_id, esi_level, wait_time)

    where wait_time = timestamp - arrival_time for that patient.

    A TREAT event with nobody waiting is simply skipped (the doctor waits
    idle) -- do not raise an error.

    Return the list of treatment records, in the order they occurred.
    """
    # TODO
    ...


# ---------------------------------------------------------------------
# Self-check -- do not need to edit below this line.
#
# Run this file directly (`python er_queue.py`) to check your Part 1/2
# work against a known example. All asserts should pass once ERQueue and
# run_simulation are correctly implemented.
# ---------------------------------------------------------------------
if __name__ == "__main__":
    example_events = [
        (0,  "ARRIVE", ("P1", 3)),
        (2,  "ARRIVE", ("P2", 1)),
        (5,  "TREAT",  None),
        (6,  "ARRIVE", ("P3", 3)),
        (9,  "TREAT",  None),
        (9,  "ARRIVE", ("P4", 2)),
        (12, "TREAT",  None),
        (20, "TREAT",  None),
    ]

    expected = [
        (5,  "P2", 1, 3),
        (9,  "P1", 3, 9),
        (12, "P4", 2, 3),
        (20, "P3", 3, 14),
    ]

    q = ERQueue()
    records = run_simulation(example_events, q)

    print("time | patient | esi | wait")
    print("-----+---------+-----+-----")
    for t, pid, esi, wait in records:
        print(f"{t:>4} | {pid:>7} | {esi:>3} | {wait:>4}")

    assert records == expected, (
        f"\nMismatch!\n  expected: {expected}\n  got:      {records}\n"
        "Check your priority ordering and tie-breaking rule."
    )

    total = len(records)
    avg_wait = sum(r[3] for r in records) / total
    print(f"\nPatients treated: {total}")
    print(f"Average wait time: {avg_wait:.2f}")

    assert total == 4
    assert abs(avg_wait - 7.25) < 1e-9

    print("\nAll self-checks passed.")
