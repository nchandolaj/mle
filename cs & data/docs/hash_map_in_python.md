# Hash Map in Python

In Python, a **Hash Map** is implemented via the built-in `dict` (dictionary) class. In Python, the `dict` is the concrete implementation of the **Hash Map** concept using a **highly refined, all-purpose Hash Table** that serves as one of the most optimized parts of the entire language.

* **"Hash Map"** is a general abstract data type (the concept of mapping keys to values).
* **"Hash Table"** is the data structure used to build that map.

## 1. How it Works Under the Hood
Python’s dictionary uses **Open Addressing** for collision resolution. This differs from many other languages (like Java) that use Chaining. 

When you insert a key-value pair:
1.  Python runs the key through a hash function: `hash(key)`.
2.  It uses the result to calculate an index in a sparse array.
3.  If that slot is empty, it stores the data.
4.  **Collision:** If the slot is already occupied, Python uses a "pseudo-random" probing sequence to find the next available slot.

## 2. Key Characteristics of Python Dictionaries

### Insertion Order (Python 3.7+)
Historically, dictionaries were unordered. However, since Python 3.7 (and as an implementation detail in 3.6), dictionaries are **guaranteed to maintain insertion order**. 
* This was achieved by moving to a "compact" layout where the hash table stores indices that point to a separate, dense array containing the actual key-value pairs.

### The "Hashable" Requirement
To use an object as a key in a Python dict, it must be **hashable**. This means:
* It must have a hash value that never changes during its lifetime (usually requires the object to be **immutable**).
* It must be comparable to other objects (implements `__eq__`).
* **Examples:** Strings, integers, and tuples are hashable. Lists and dictionaries are **not** hashable because they can be changed (mutable).

## 3. Performance
Because it is a hash table, the dictionary offers incredible performance for standard operations:

| Operation | Average Case | Worst Case |
| :--- | :--- | :--- |
| **Search** | $O(1)$ | $O(n)$ |
| **Insertion** | $O(1)$ | $O(n)$ |
| **Deletion** | $O(1)$ | $O(n)$ |

> **Note:** The worst case $O(n)$ only occurs during extreme hash collisions or during a resize/rehash event.

## 4. Practical Example
Here is how you interact with the Python implementation of a Hash Map:

```python
# Initialization
user_scores = {"Alice": 95, "Bob": 87}

# O(1) Insertion
user_scores["Charlie"] = 92 

# O(1) Lookup
print(user_scores.get("Alice")) 

# Handling missing keys gracefully
score = user_scores.get("Eve", 0) # Returns 0 instead of crashing
```

# DEEP DIVE: Does Python use a Hash Map or a Hash Table?

In technical terms, Python uses a **Hash Table** to implement its **`dict`** (Dictionary) type, but for all practical purposes, a Python `dict` **is** a Hash Map.

To understand why this distinction exists, we have to look at how Python is built and how it manages data.

## 1. The Short Answer
Python uses a **Hash Table** implementation. Specifically, it uses a variation called a **Sparse Hash Table** with **Open Addressing**. 

* **"Hash Map"** is a general *abstract data type* (the concept of mapping keys to values).
* **"Hash Table"** is the *data structure* used to build that map.

In Python, the `dict` is the concrete implementation of the Hash Map concept using a Hash Table structure.

## 2. Python’s Specific Implementation: Open Addressing
Unlike languages like Java, where a "HashMap" usually uses **Chaining** (linked lists in each bucket), Python's hash table uses **Open Addressing**.

When a collision occurs in Python:
1.  The algorithm calculates a new index based on a specific formula (a "probing" sequence).
2.  It looks at that new slot.
3.  If it's full, it repeats until it finds an empty space.

## 3. The "Compact" Dictionary (Python 3.6+)
Since version 3.6, Python changed how its hash table is structured to be more memory-efficient. It now uses two arrays instead of one:

1.  **The Hash Indices (Sparse Array):** A small array that only stores the "indices" of where the data lives.
2.  **The Entry Array (Dense Array):** A separate array that stores the actual `hash`, `key`, and `value` in the order they were inserted.

**This shift is why Python dictionaries now preserve insertion order.** Because the entries are stored in a dense list as they arrive, iterating through the dict simply means walking through that list.

## 4. Why Python chooses this over Chaining

* **Memory Efficiency:** Linked lists (used in Chaining) require extra pointers, which consume more memory. Python's compact array layout is much leaner.
* **Cache Locality:** Modern CPUs are faster when they access data stored close together in memory. Arrays (Open Addressing) are better for this than linked lists scattered across memory.

## 5. Summary Table

| Feature | Python `dict` |
| :--- | :--- |
| **Concept** | Hash Map |
| **Data Structure** | Hash Table |
| **Collision Resolution** | Open Addressing (Pseudo-random probing) |
| **Ordering** | Ordered (since 3.7+) |
| **Null Keys** | No (None is allowed, but it's an object, not a "null" slot) |

