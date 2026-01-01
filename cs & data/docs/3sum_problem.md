# 3Sum Problem

The **3Sum** problem is a classic algorithmic challenge that builds upon the foundational **Two Sum** logic. It is frequently used in technical interviews to test your ability to optimize nested loops and handle edge cases like duplicate results.

## 1. The Problem Statement
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that:
1.  $i \neq j$, $i \neq k$, and $j \neq k$ (no using the same index twice).
2.  $nums[i] + nums[j] + nums[k] == 0$.
3.  The solution set must **not contain duplicate triplets**.

### **The Brute Force Approach**
A naive solution involves three nested loops to check every possible combination:

```python
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if nums[i] + nums[j] + nums[k] == 0:
                # Add to set to handle duplicates
```
**Complexity:** $O(n^3)$ — This is far too slow for large datasets.

## 2. The Optimized Strategy: Sort + Two Pointers
By sorting the array first (**O(n log n)**), we can reduce the complexity to **O(n^2)**. We fix one number and then use the **Opposite Ends** pattern to find the other two.

### **The Step-by-Step**
1.  **Sort** the array.
2.  Iterate through the array with a pointer `i`. This is your "fixed" element.
3.  Set `left` to `i + 1` and `right` to the end of the array.
4.  Calculate the sum:
    * If **Sum == 0**: Success! Save the triplet.
    * If **Sum < 0**: We need a larger value, so move `left` forward.
    * If **Sum > 0**: We need a smaller value, so move `right` backward.

## 3. The "Hurdle": Handling Duplicates
The most difficult part of 3Sum is avoiding duplicate triplets in the output without using a heavy `set()` data structure, which can increase space complexity.

### **Hurdle A: The Fixed Pointer Duplicate**
If your current `nums[i]` is the same as the previous `nums[i-1]`, the algorithm will find the exact same pairs it just found.

```python
if i > 0 and nums[i] == nums[i-1]:
    continue # Skip to the next unique number
```

### **Hurdle B: The Inner Pointer Duplicates**
Once you find a valid triplet (`sum == 0`), your `left` and `right` pointers might still be sitting on the same values they just used. You must manually skip them.

```python
while left < right and nums[left] == nums[left + 1]:
    left += 1 # Skip identical left values
while left < right and nums[right] == nums[right - 1]:
    right -= 1 # Skip identical right values
```

## 4. Visualizing the Logic
Imagine `nums = [-2, -2, 0, 0, 2, 2]` sorted.

1.  **i = 0 (value -2):**
    * Pointers find `(-2, 0, 2)`.
    * The `while` loops skip the next `0` and the next `2`.
2.  **i = 1 (value -2):**
    * The `if i > 0 and nums[i] == nums[i-1]` check triggers.
    * **Skip!** We already found all triplets starting with `-2`.

## Summary of Complexity
* **Time Complexity:** $O(n^2)$ because we have an outer loop ($n$) and a two-pointer scan ($n$) inside it.
* **Space Complexity:** $O(1)$ or $O(n)$ depending on the implementation of the sorting algorithm and whether the output list is counted.

---

## The 3Sum Solution: Handling Duplicates with Two Pointers

```python
def threeSum(nums):
    # Step 1: Sorting is essential for handling duplicates and two-pointer logic
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        # HURDLE A: Skip the same fixed element to avoid duplicate triplets
        if i > 0 and nums[i] == nums[i-1]:
            continue
            
        # Optimization: If the smallest possible sum is > 0, stop the loop
        if nums[i] + nums[i+1] + nums[i+2] > 0:
            break
            
        # Standard Two-Pointer (Opposite Ends) initialization
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # HURDLE B: Skip duplicates for 'left' and 'right' pointers
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                # Move pointers inward after finding a valid triplet
                left += 1
                right -= 1
                
            elif current_sum < 0:
                # Sum too small; move left pointer to increase sum
                left += 1
            else:
                # Sum too large; move right pointer to decrease sum
                right -= 1
                
    return result

# Example Usage:
example_nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(example_nums)) 
# Output: [[-1, -1, 2], [-1, 0, 1]]
```

### Why this code works

1.  **Efficiency:** Instead of $O(n^3)$, this runs in $O(n^2)$. The sorting takes $O(n \log n)$, and the nested loops (an outer loop and a two-pointer scan) take $O(n^2)$.
2.  **No Extra Space:** Unlike using a `set()` to store results (which can consume a lot of memory), this skips duplicates "on the fly," keeping the extra space complexity to $O(1)$ (ignoring the space used by the output list).

