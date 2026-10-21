"""
CS 383 — Bonus Hashing Assignment: Starter Template

Name:
Collision strategy chosen (chaining / open addressing):

Instructions:
- Implement insert, search, and delete below.
- Choose ONE collision resolution strategy: separate chaining OR open
  addressing with linear probing. Delete the method bodies you don't need
  and fill in the ones you do -- you do not need to implement both.
- Do not implement dynamic resizing; a fixed table size is fine.
- At the bottom, in the __main__ block, add a short demonstration of your
  table working correctly, including at least one deliberate collision
  (i.e., two keys you know will hash to the same slot).
"""


class HashTable:
    def __init__(self, size=11):
        self.size = size
        # TODO: initialize your underlying storage here.
        # For chaining: a list of buckets (e.g., a list of lists).
        # For open addressing: a flat list of slots, all initially None.
        self.table = None

    def _index(self, key):
        """Map a key to a starting slot/bucket index."""
        # TODO: any reasonable hash function is fine, e.g. Python's
        # built-in hash(key) % self.size.
        pass

    def insert(self, key, value):
        """
        Insert a new key/value pair. If the key already exists, update
        its value instead of creating a duplicate entry.
        """
        # TODO
        pass

    def search(self, key):
        """
        Return the value associated with key, or None if key is not
        present in the table.
        """
        # TODO
        pass

    def delete(self, key):
        """
        Remove key from the table if present.

        Reminder if you're using open addressing: think carefully about
        what happens to search() for OTHER keys after a delete. Setting
        a slot back to None on delete can break the probe sequence for
        keys that were inserted after a collision.
        """
        # TODO
        pass


if __name__ == "__main__":
    ht = HashTable(size=11)

    # TODO: demonstrate insert, search, and delete working correctly.
    # Make sure to include at least one deliberate collision -- i.e.,
    # two keys that you've confirmed hash to the same slot -- and show
    # that both are still handled correctly (inserted, found, and, if
    # one is deleted, the other is still searchable).

    pass
