# Data Structures in Computer Science

In computer science, a **data structure** is a specialized format for organizing, processing, retrieving, and storing data. It is the "physical" implementation of an Abstract Data Type (ADT). While an ADT defines *what* operations can be performed (like a "List"), the data structure defines *how* those operations are executed in memory (like an "Array" vs. a "Linked List").

[Image of data structures classification tree]


### 1. Classification of Data Structures
Data structures are generally categorized based on how the elements are arranged and how memory is allocated.

* **Linear Data Structures:** Elements are arranged in a sequence. Each element is connected to its previous and next adjacent elements.
    * *Examples:* Arrays, Stacks, Queues, Linked Lists.
* **Non-Linear Data Structures:** Elements are not arranged sequentially; they can be hierarchical or interconnected.
    * *Examples:* Trees, Graphs, Heaps.
* **Static vs. Dynamic:** Static structures (like fixed-size arrays) have a fixed memory size at compile time, while dynamic structures (like linked lists or dynamic arrays) can grow or shrink during execution.

---

### 2. Exhaustive List of Data Structures
In modern languages (Python, Java, C++, Rust, Go), data structures range from primitive types to highly specialized concurrent and probabilistic structures.

#### **A. Linear Data Structures**
* **Array:** A collection of elements identified by index, stored in contiguous memory.
    * *Variants:* Static Array, Dynamic Array (e.g., `std::vector` in C++, `ArrayList` in Java, `list` in Python).
* **Linked List:** Nodes containing data and pointers to other nodes.
    * *Variants:* Singly Linked, Doubly Linked, Circular Linked List, Skip List.
* **Stack:** Last-In-First-Out (LIFO) structure.
* **Queue:** First-In-First-Out (FIFO) structure.
    * *Variants:* Circular Queue, Priority Queue, Deque (Double-Ended Queue).

#### **B. Tree-Based Data Structures (Hierarchical)**
* **Binary Tree:** Each node has at most two children.
* **Binary Search Tree (BST):** A binary tree where the left child is smaller and the right child is larger than the parent.
* **Balanced Trees:** Automatically keep their height small to ensure $O(\log n)$ operations.
    * *Examples:* AVL Tree, Red-Black Tree (used in Java's `TreeMap`), B-Trees/B+ Trees (used in databases).
* **Heap:** A tree-based structure that satisfies the "heap property" (min-heap or max-heap).

* **Trie (Prefix Tree):** Used for efficient string searching and autocomplete.
* **Segment Tree / Fenwick Tree:** Used for range queries and updates.

#### **C. Hashing & Set Data Structures**
* **Hash Table / Hash Map:** Uses a hash function to map keys to values ($O(1)$ average time).
    * *Variants:* Distributed Hash Tables (DHT), Cuckoo Hashing.
* **HashSet:** Stores unique elements using hashing.
* **Bloom Filter:** A probabilistic data structure used to test if an element is a member of a set (allows false positives but no false negatives).

#### **D. Graph Data Structures**
* **Graph:** A set of vertices (nodes) and edges (connections).
    * *Representations:* Adjacency Matrix, Adjacency List.

    * *Types:* Directed/Undirected, Weighted/Unweighted, Directed Acyclic Graph (DAG).

#### **E. Advanced & Language-Specific Structures**
* **Disjoint Set Union (DSU):** Also called Union-Find; tracks elements partitioned into disjoint sets.
* **Suffix Tree / Suffix Array:** Advanced structures for complex string pattern matching.
* **Spatial Data Structures:** Used for geographical or 3D data.
    * *Examples:* Quadtree, Octree, R-Tree, K-D Tree.
* **Concurrent Data Structures:** Thread-safe versions used in systems programming.
    * *Examples:* ConcurrentHashMap (Java), Lock-free Queues.

---

### 3. Comparison Table: Core Complexity
| Data Structure | Access (Avg) | Search (Avg) | Insertion (Avg) | Deletion (Avg) |
| :--- | :--- | :--- | :--- | :--- |
| **Array** | $O(1)$ | $O(n)$ | $O(n)$ | $O(n)$ |
| **Stack/Queue** | $O(n)$ | $O(n)$ | $O(1)$ | $O(1)$ |
| **Linked List** | $O(n)$ | $O(n)$ | $O(1)$ | $O(1)$ |
| **Hash Table** | N/A | $O(1)$ | $O(1)$ | $O(1)$ |
| **BST (Balanced)** | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ |

Would you like me to explain how a specific data structure, such as a Hash Map or a Red-Black Tree, is implemented in a particular language like Python or C++?
