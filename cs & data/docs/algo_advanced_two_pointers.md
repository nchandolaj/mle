# Algorithm: Advanced Two Pointers

Moving into **3Sum** and **Greedy logic** is where you transition from basic syntax to true algorithmic thinking. These concepts are all about efficiency—reducing $O(n^3)$ brute force to $O(n^2)$ or $O(n)$.

Here is the breakdown of these "hurdles."

## 1. The 3Sum Hurdle: Handling Duplicates
The challenge with 3Sum ($a + b + c = 0$) isn't just finding the numbers; it’s ensuring you don't return the same triplet twice.

### **The Strategy**
1.  **Sort the array:** This is non-negotiable. Sorting allows you to skip duplicate values easily.
2.  **The "Skip" Logic:** If the current element is the same as the previous one, `continue`.
3.  **Two-Pointer Narrowing:** Use "Opposite Ends" pointers for the remaining two numbers.

```python
nums.sort()

for i in range(len(nums)):
    # Skip the same 'a' to avoid duplicate triplets
    if i > 0 and nums[i] == nums[i-1]:
        continue
    
    # Now perform standard Two Pointers (Opposite Ends)
    l, r = i + 1, len(nums) - 1
    # ... logic continues
```

## 2. Greedy Logic: The Water Container
In the **Container With Most Water** problem, you use a "Greedy" approach. You start with the *widest possible container* (*pointers at the very ends*) and make a choice to improve it.

### **The Rule**
Always move the pointer pointing to the **shorter line**.

* **Why?** The area is limited by the height of the shorter side. Moving the taller side can only decrease the width without ever increasing the height of the "bottleneck." Moving the shorter side is the only gamble that could result in a taller container.

## 3. Lambda Functions for Sorting
Data is rarely a simple list of integers. You’ll often deal with "Lists of Lists" or "Lists of Tuples."

### **The Syntax**
A lambda is an anonymous, one-line function: `lambda arguments: expression`.

```python
# Example: Sort intervals by their end times
intervals = [[1, 4], [2, 3], [3, 6]]

# x represents each element (the sub-list)
# x[1] tells Python to sort by the second value (the 'end' of the interval)
intervals.sort(key=lambda x: x[1])

print(intervals) # Output: [[2, 3], [1, 4], [3, 6]]
```

### **Common Use Cases**
* **Sorting by absolute value:** `sorted(nums, key=lambda x: abs(x))`
* **Sorting a dictionary by values:** `sorted(d.items(), key=lambda x: x[1])`

## Challenge Summary Table

| Problem | Key Technique | Why? |
| :--- | :--- | :--- |
| **3Sum** | `if i > 0 and nums[i] == nums[i-1]` | To avoid duplicate sets in the result. |
| **Water Container** | `if height[l] < height[r]: l += 1` | Greedy choice to find a potentially taller wall. |
| **Intervals** | `sort(key=lambda x: x[0])` | To process overlapping data in linear order. |

---

**Would you like to try coding the "3Sum" solution now? I can provide a template with the duplicate-skipping logic left blank for you to fill in.**
