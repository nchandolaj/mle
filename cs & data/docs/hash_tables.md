# Data Structure: Hash Tables

Hash tables are one of the most fundamental and powerful data structures in computer science. They are the engine behind everything from database indexing to the core mechanics of high-level languages like Python.

## 1. The Why, What, and How

### The "Why": Speed

Before hash tables, finding an item in a collection usually required searching through it ( $O(n)$ time) or keeping it sorted to use binary search ( $O(\log n)$ time). 

Hash tables were designed to achieve **$O(1)$ (constant time)** complexity for search, insertion, and deletion.

### The "What": A Key-Value Mapping

A hash table is a data structure that maps **keys** to **values**. It uses a mathematical formula, 'a hash function', to transform a key into an index in an array.

### The "How": The Hash Function

The "magic" happens via a **Hash Function**. This function takes an input (like a string "Apple") and outputs an integer. That integer is then mapped to a specific slot (bucket) in an underlying **array**.

* **Determinism:** The same input must always produce the same output.
* **Efficiency:** It must be fast to compute.
* **Uniformity:** It should distribute keys evenly across the table to avoid "clumping."

## 2. Implementation & The Collision Challenge

Even the best hash function will eventually map two different keys to the same array index. This is known as a **Collision**.

### Resolution 1: Chaining (Open Hashing)

Each slot in the **array** points to a **linked list** (or another data structure). If a collision occurs, the new item is simply appended to the linked list (or another data structure) at that index.

* **Pros:** Simple to implement; the table never truly "fills up."
* **Cons:** If lists get too long, performance degrades to $O(n)$.

### Resolution 2: Open Addressing (Closed Hashing)

If a collision occurs, the algorithm looks for another empty slot in the array according to a specific probe sequence:

* **Linear Probing:** Look at the next slot ($index + 1$), then the next, until an empty one is found.
* **Quadratic Probing:** Increase the interval between probes quadratically.
* **Double Hashing:** Use a second hash function to determine the step size.

## 3. Resizing: Maintaining Performance

As a hash table fills up, the probability of collisions increases. This is measured by the **Load Factor ($\alpha$):**

$$\alpha = \frac{\text{Total elements (n)}}{\text{Number of buckets (m)}}$$

### Automated Resizing (Rehashing)

Most modern implementations (like **Python’s `dict`** or **Java’s `HashMap`**) resize **automatically**. 

* **Threshold:** When $\alpha$ exceeds a certain limit (usually 0.75), the table grows.
* **Process:** A new, larger array is created (typically double the size). Every single existing item must be **re-hashed** into the new array because their index (calculated as $hash(key) \pmod m$) changes when $m$ changes.

### Manual Resizing

In low-level systems programming (like C), developers may manually define the initial size if they know exactly how much data to expect, avoiding the expensive overhead of automated rehashing during runtime.

## 4. Different Types of Hash Tables

1.  **Static Hash Table:** The size is fixed at creation. Best when the data set is known and unchanging.
2.  **Dynamic Hash Table:** Grows and shrinks based on the number of elements.
3.  **Distributed Hash Table (DHT):** Spread across multiple nodes in a network (used in BitTorrent and Blockchain).
4.  **Cuckoo Hashing:** Uses two hash functions and two tables. If a collision occurs, it "kicks out" the existing resident to a new home, ensuring $O(1)$ worst-case lookup.

## 5. Use Cases

* **Database Indexing:** To quickly locate records without scanning entire tables.
* **Caching:** Storing web page data or API responses for instant

