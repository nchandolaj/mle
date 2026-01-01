# Algortihm: Two Pointers

*Focus: Reducing $O(n^2)$ to $O(n)$ by processing from both ends.*

## Overview
The **Two Pointers** technique is one of the most effective ways to optimize algorithms from a "brute force" approach to a linear one. 
By utilizing the _inherent structure of the data (like **sorting** or **symmetry**)_, you can avoid redundant checks.

## 1. The Core Concept
In a typical $O(n^2)$ approach, you might use nested loops to compare every possible pair of elements. With Two Pointers, you use **two indices** (usually `L` and `R`) and move them toward each other.

### Why it works:
Instead of checking every combination, you use a **condition** to discard entire sets of possibilities. 
* If the current sum is too small, moving the `L` pointer to the right *guarantees* a larger sum.
* If the current sum is too large, moving the `R` pointer to the left *guarantees* a smaller sum.

## 2. Use Case: The Two-Sum (Sorted)
Imagine you have a **sorted array** and need to find two numbers that add up to a target.

**The $O(n)$ Logic:**
1.  Place `L` at index `0` and `R` at the last index.
2.  Calculate `current_sum = arr[L] + arr[R]`.
3.  If `current_sum == target`: Success!
4.  If `current_sum < target`: We need more value. Increment `L` (`L += 1`).
5.  If `current_sum > target`: We need less value. Decrement `R` (`R -= 1`).

```python
def two_sum_sorted(nums, target):
    l, r = 0, len(nums) - 1
    
    while l < r:
        curr = nums[l] + nums[r]
        if curr == target:
            return [l, r]
        elif curr < target:
            l += 1
        else:
            r -= 1
    return []
```

## 3. Use Case: Valid Palindrome (Processing Strings)
This pattern is perfect for palindromes because they are **inherently symmetrical**.

**Handling Non-Alphanumeric Characters:**
A common interview constraint is to "ignore case and non-alphanumeric characters." Instead of creating a new filtered string (which uses $O(n)$ space), you can skip the characters "on the fly" using your pointers.

```python
def is_palindrome(s):
    l, r = 0, len(s) - 1
    
    while l < r:
        # Skip non-alphanumeric from the left
        while l < r and not s[l].isalnum():
            l += 1
        # Skip non-alphanumeric from the right
        while l < r and not s[r].isalnum():
            r -= 1
            
        if s[l].lower() != s[r].lower():
            return False
            
        l += 1
        r -= 1
        
    return True
```

## 4. Key Takeaways for Your Review
| Feature | Description |
| :--- | :--- |
| **Pointers** | Usually `l = 0` and `r = len(arr) - 1`. |
| **Loop Condition** | `while l < r` (stops when they meet or cross). |
| **Optimization** | Reduces nested loops ($O(n^2)$) to a single pass ($O(n)$). |
| **Space** | Usually $O(1)$ because you are only storing two integer indices. |


### Comparison: Brute Force vs. Two Pointers

> **Note:** This specific "Opposite Ends" pattern requires the data to be **sorted** (for sums) or **symmetrical** (for palindromes). If the array isn't sorted, you often have to sort it first ($O(n \log n)$) or use a Hash Map.

