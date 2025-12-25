# Arrays, Hashing, and Time-Space Trade-offs

## 1. Arrays vs. Hashing: The Core Difference
In Python, a **List** is a dynamic array. To find an element without knowing its index, you must perform a **Linear Search**, checking every element one by one ($O(n)$ time).

A **Hash Map** (Python `dict`) solves this by using a **Hash Function** to map a "key" to a specific memory address. This allows for **Constant Time** ($O(1)$) access, regardless of how many millions of items are in the collection.

## 2. Trading Space for Time
The fundamental principle of Hashing is **trading space for time**. 

* **The Cost (Space):** A dictionary consumes significantly more RAM than a list. It needs to stay "sparse" (mostly empty) to avoid collisions and stores extra metadata (hashes and keys) to manage the data.
* **The Benefit (Time):** You gain the ability to jump directly to data. If you have 1,000,000 items, a list might take 1,000,000 steps to find the last item; a dictionary takes **one**.

## 3. Collisions and Load Factor

### **Collisions**
A collision occurs when two distinct keys produce the same hash value or map to the same array index. Since the number of possible keys (infinite) is larger than the number of available memory slots (finite), collisions are inevitable.

### **Load Factor ($\alpha$)**
The **Load Factor** is the measure of how full the hash table is: </br>

$$\alpha = \frac{\text{Number of Elements (n)}}{\text{Number of Slots (k)}}$$

* **Low Load Factor:** Lots of empty space, very few collisions, very fast performance.
* **High Load Factor:** Table is nearly full, many collisions, performance degrades toward $O(n)$.
* **Python's Threshold:** Python's `dict` typically triggers a **resize** (doubling the table size) when the load factor exceeds **2/3 (approx 0.66)**. This ensures lookups stay $O(1)$.

## 4. The "Pre-computation" Pattern (Seen Elements)
One of the most powerful patterns in technical interviews and data processing is using a hash map/set to store "seen" elements. This allows you to check for existence in $O(1)$ instead of re-scanning the original array.

### **The Logic**
Instead of asking, "Is this element in the list?" (which is $O(n)$), you pre-process the list into a set:
1.  **Iterate** through the array once.
2.  **Store** each item in a Hash Set.
3.  **Check** for any future items against that set in constant time.

### **Python Example: The Two-Sum Problem**
*Goal: Find two numbers in a list that add up to a specific target.*

**Naive Approach** ( $O(n^2)$ ): Nested loops comparing every pair.

**Optimized Approach** ( $O(n)$ ): Using a dictionary to store "seen" values.

**The Logic: One-Pass Hash Map**
Instead of using nested loops ( $O(n^2)$ ), we iterate through the list once. For every number `x`, we calculate the `complement` ($target - x$). 

If the `complement` exists in our dictionary, we have found the solution. If not, we store the current number in the dictionary and move to the next.

```python
def two_sum(nums, target):
    """
    Finds two indices such that nums[index1] + nums[index2] == target.
    Uses a dictionary to achieve O(n) time complexity.
    """
    # Map to store: {value: index}
    seen_elements = {}

    for current_index, current_value in enumerate(nums):
        complement = target - current_value
        
        # O(1) Search: Check if the required partner has already been seen
        if complement in seen_elements:
            # Return the index of the complement and the current index
            return [seen_elements[complement], current_index]
        
        # O(1) Insertion: Record the current value and its index
        seen_elements[current_value] = current_index
        
    return None # Return None if no solution exists

# Example Usage:
numbers = [2, 7, 11, 15]
target_val = 9
print(f"Indices: {two_sum(numbers, target_val)}") # Output: [0, 1]


## Complexity Comparison

| Approach | Time Complexity | Space Complexity |
|:-|:-|:-|
| Nested Loops | $O(n^2)$ | $O(1)$ |
| Hash Map (Seen) | $O(n)$ | $O(n)$ |



