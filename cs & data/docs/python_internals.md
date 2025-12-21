# Python Internals

*Focus: Understanding Python's built-in data structures and how they manage memory and handle operations under the hood.*

## Scope
* List vs. Tuple vs. Set (Lookup times).
* dict implementation (Hash map).
* List slicing arr[start:stop:step] (Note: Slicing creates a copy, costing O(k) memory).
  
## Python Data Structures: Implementation and Complexity

Python’s built-in data structures are highly optimized, but choosing the right one requires understanding how they manage memory and handle operations under the hood.

## 1. Sequence Types: List and Tuple

### **List (Mutable)**
A Python list is a **dynamic array**. When it runs out of space, Python allocates a larger chunk of memory (usually doubling the size) and copies the elements over.

* **Lookup:** $O(1)$ by index; $O(n)$ by value.
* **Insert/Delete:** $O(n)$ because elements must be shifted. Appending is **Amortized $O(1)$**.
* **Space:** Higher than tuples due to **over-allocation (padding)** to accommodate future growth.

### **Tuple (Immutable)**
Tuples are fixed-size. Once created, they cannot be changed.

* **Lookup:** $O(1)$ by index.
* **Space:** More memory-efficient than lists. Because they are immutable, Python can allocate the exact amount of memory needed **without extra padding**.
* **Use Case:** Ideal for "records" or constant data. They can be used as dictionary keys if they contain only hashable objects.

### **List Slicing**
Slicing (`my_list[start:stop:step]`) creates a **shallow copy** of the specified range. *A **shallow copy** means that a new collection object is created, but the elements inside that new collection are still references to the same objects found in the original. 
In contrast, a **deep copy** creates a completely independent copy where even nested objects are duplicated.*
* **Time Complexity:** $O(k)$ where $k$ is the length of the slice.
* **Space Complexity:** $O(k)$ to store the new list.
* **Note:** In large data processing, frequent slicing in loops can lead to significant memory overhead.

## 2. Hashed Collections: Set and Dictionary

Both types rely on **Hash Tables**, which provide near-instantaneous access by converting a key into an index via a hash function. *A **hash function** is a deterministic algorithm that takes an input (like a string, integer, or tuple) and returns a fixed-size integer, known as a **hash value**.*

### **Dictionary (dict)**
Dictionaries store key-value pairs. As of Python 3.7+, they maintain insertion order as an implementation detail, but their **primary strength is speed**.

* **Lookup/Insert/Delete:** $O(1)$ average case.
* **Space:** Significant overhead. They require space for the hash table itself and to minimize "collisions" (when two keys hash to the same index).
* **Implementation:** Python uses **open addressing** to resolve collisions.

### **Set**
A set is essentially a dictionary where there are only keys and no values.
* **Lookup:** $O(1)$ average. This makes sets perfect for **membership testing** (checking if `x in collection`).
* **Operations:** Mathematical operations like Union ($O(n+m)$) or Intersection ($O(\min(n, m))$) are highly optimized.


## 3. Complexity & Performance Summary

| Data Structure | Access (Index) | Search (Value) | Insertion | Space Complexity |
| :--- | :--- | :--- | :--- | :--- |
| **List** | $O(1)$ | $O(n)$ | $O(n)$ (at start/middle) | $O(n)$ |
| **Tuple** | $O(1)$ | $O(n)$ | N/A | $O(n)$ (compact) |
| **Set** | N/A | $O(1)$ | $O(1)$ | $O(n)$ (heavy) |
| **Dict** | $O(1)$ (by key) | $O(n)$ (by value) | $O(1)$ | $O(n)$ (heavy) |


## 4. Practical Implications

1.  **Search Speed:** If you need to check if an item exists repeatedly, convert your `list` to a `set`. A list search takes $O(n)$ (linear time), while a set search takes $O(1)$ (constant time).
2.  **Memory Constraints:** If you are storing millions of coordinates that won't change, use a `tuple` instead of a `list` to save several megabytes of RAM.
3.  **Slicing vs. Iteration:** If you only need to read data, consider using `itertools.islice` or a generator. This avoids the $O(k)$ space cost of creating a new sliced list.

> **Note:** For high-performance numerical data, Python's standard structures can be slow because they store pointers to objects. In those cases, **`NumPy` arrays** are preferred as they store data in **contiguous memory blocks**.

# References
* 

> **Note** Python Internals is a sub-topic of [**The Pythonic Standard**](https://github.com/nchandolaj/mle/blob/main/cs%20%26%20data/docs/the_pythonic_standard.md) discussion.
