# Python Collections 

Moving from Python’s built-in collections to custom data structures is the key to writing efficient code. 

## 1. Built-in Collections (The Fundamentals)

Python provides **four main "container" types**. The choice depends on whether you need **order**, **uniqueness**, or **mutability**.

### A. List `[]`: The Ordered Sequence
*Lists are your go-to for collections of items where order matters and you may need to change the content.*

* **Nature:** Ordered and mutable (changeable).
* **Best for:** Storing sequences where the position matters.
* **Performance:** Fast at adding/removing from the *end*, but slow $O(n)$ at the *beginning* because every other element has to shift.

```python
# Creation
fruits = ["apple", "banana", "cherry"]

# Access by index
print(fruits[0])  # Output: apple

# Mutability: changing an item
fruits[1] = "blueberry"

# Adding items
fruits.append("date")

# Removing by value
fruits.remove("cherry")

print(fruits) # Output: ['apple', 'blueberry', 'date']
```

### B. Tuple `()`: The Fixed Record
*Tuples are best for data that belongs together as a single "record" and should not be accidentally altered.*

* **Nature:** Ordered but **immutable** (cannot be changed after creation).
* **Best for:** Data that shouldn't change (like coordinates `(x, y)` or database records).
* **Performance:** Slightly faster and more memory-efficient than lists.

```python
# Creation (parentheses are optional but standard)
coordinates = (10, 20)
user_profile = ("jdoe", "John Doe", 30)

# Access by index
print(coordinates[0]) # Output: 10

# Immutability: The following would raise a TypeError
# coordinates[0] = 15 

# Unpacking: a very common Python pattern
x, y = coordinates
print(f"X: {x}, Y: {y}")
```

### C. Set `{}`: The Unique Collection
*Sets are used when you need to ensure no duplicates exist and when you want to perform mathematical operations like intersections.*

* **Nature:** Unordered and contains **unique** elements only.
* **Best for:** Removing duplicates and membership testing (checking if "x" is in the set).
* **Performance:** Extremely fast $O(1)$ for lookups.

```python
# Creation
ids = {101, 102, 103, 101} # Note: 101 is repeated

# Duplicates are automatically removed
print(ids) # Output: {101, 102, 103}

# Membership testing (Highly optimized O(1))
if 102 in ids:
    print("ID found!")

# Set math
other_ids = {103, 104, 105}
print(ids.intersection(other_ids)) # Output: {103}
print(ids.union(other_ids))        # Output: {101, 102, 103, 104, 105}
```

### D. Dictionary `{"key": "value"}`: The Key-Value Map
*Dictionaries (or "dicts") are used for fast lookups by a label (key) rather than a numeric position.*

* **Nature:** Key-Value pairs. Keys must be unique and immutable.
* **Best for:** Mapping data for quick retrieval.

```python
# Creation
stock_prices = {
    "AAPL": 150.25,
    "GOOG": 2800.10,
    "TSLA": 700.00
}

# Accessing by key
print(stock_prices["AAPL"]) # Output: 150.25

# Adding/Updating
stock_prices["MSFT"] = 300.50
stock_prices["AAPL"] = 155.00 # Updates existing value

# Safe access with .get() (avoids error if key is missing)
price = stock_prices.get("AMZN", "Not Found")
print(price) # Output: Not Found
```

## 2. Advanced Linear Structures

Once you outgrow lists, you encounter structures that optimize for specific types of access.

### Linked List
Unlike a list (which uses a contiguous block of memory), a Linked List consists of **Nodes**. Each node contains data and a "pointer" to the next node.
* **Singly Linked:** Each node points to the next.
* **Doubly Linked:** Each node points to both the next and the previous.
* **Pros:** Very fast $O(1)$ insertions/deletions at the beginning or middle (if you already have the reference).
* **Cons:** No "random access." To find the 10th element, you must start at the 1st and follow the chain.

### Stack & Queue
* **Stack (LIFO):** Last-In, First-Out. Like a stack of plates. You use `.append()` and `.pop()`.
* **Queue (FIFO):** First-In, First-Out. Like a line at a store. In Python, use `collections.deque` for efficient $O(1)$ pops from the front.


## 3. Specialized Non-Linear Structures

### Heaps (Priority Queues)
A Heap is a specialized tree-based structure. In a **Min-Heap** (Python's default), the smallest element is always at the root.
* **Use Case:** When you constantly need to access the "minimum" or "maximum" value while adding new data.
* **Python Library:** `heapq`
* **Logic:** Even as you add elements, it stays "partially sorted," so getting the top element is always $O(1)$, and re-sorting is $O(\log n)$.

### Trees & Binary Search Trees (BST)
* **Tree:** A hierarchy starting with a "Root" node, which has "Children" nodes.
* **BST:** A tree where the left child is smaller than the parent, and the right child is larger. This allows for incredibly fast searching, similar to binary search in an array.

## Comparison Summary

| Structure | Access Speed | Insert/Delete | Best Use Case |
| :--- | :--- | :--- | :--- |
| **List** | $O(1)$ | $O(n)$ (at start) | General purpose sequences |
| **Set/Dict** | $O(1)$ | $O(1)$ | Unique items / Quick lookup |
| **Linked List** | $O(n)$ | $O(1)$ | Frequent start/middle inserts |
| **Heap** | $O(1)$ (min/max) | $O(\log n)$ | Priority tasks / Top K elements |
