# Algorithm: Sliding Window

The **Sliding Window** technique is a specific sub-type of the **Two Pointers** pattern. While the previous "Opposite Ends" pattern shrinks the search space from the outside in, the Sliding Window maintains a "window" of elements that typically expands or shifts in a single direction (usually left to right).

It is the primary tool for reducing $O(n^2)$ or $O(n^3)$ problems involving **subarrays** or **substrings** down to $O(n)$.

## 1. The Core Concept
Think of a sliding window like a camera lens or a magnifying glass moving across an array. 
* **Fixed Window:** The width of the window stays the same (e.g., "Find the max sum of any 3 consecutive numbers").
* **Dynamic Window:** The window grows until a condition is met, then shrinks to find the smallest valid range (e.g., "Find the shortest subarray with a sum $\ge k$").

## 2. Use Case: Maximum Sum Subarray (Fixed)
**Problem:** Given an array, find the maximum sum of any contiguous subarray of size `k`.

Instead of recalculating the sum from scratch for every position (_O(n . k)_), you "slide" the window:
1.  Calculate the sum of the first `k` elements.
2.  Slide the window one step right: **Add** the new element and **Subtract** the element that just left the window.

```python
def max_sum_fixed(nums, k):
    if len(nums) < k: return 0
    
    # Initial window sum
    window_sum = sum(nums[:k])
    max_val = window_sum
    
    for i in range(len(nums) - k):
        # Slide: Subtract element at i, Add element at i + k
        window_sum = window_sum - nums[i] + nums[i + k]
        max_val = max(max_val, window_sum)
        
    return max_val
```

## 3. Use Case: Smallest Subarray Sum (Dynamic)
**Problem:** Find the length of the smallest subarray whose sum is $\ge$ `target`.

This uses a "Fast/Slow" pointer approach:
1.  Expand the `right` pointer to include elements until the sum $\ge$ target.
2.  Once the condition is met, shrink the `left` pointer to find the smallest possible window that still satisfies the condition.

```python
def min_subarray_len(target, nums):
    l = 0
    total = 0
    res = float('inf')
    
    for r in range(len(nums)):
        total += nums[r]
        
        # Shrink the window as much as possible while sum >= target
        while total >= target:
            res = min(res, r - l + 1)
            total -= nums[l]
            l += 1
            
    return res if res != float('inf') else 0
```

## 4. When to use Sliding Window vs. Opposite Ends
| Scenario | Pattern |
| :--- | :--- |
| Find a pair in a **sorted** array | **Opposite Ends** (L at 0, R at end) |
| Check if a string is a **palindrome** | **Opposite Ends** (L at 0, R at end) |
| Find a **subarray** or **substring** | **Sliding Window** (L and R move right) |
| "Longest/Shortest" string constraints | **Sliding Window** (Dynamic) |


### Key Takeaway
The "Window" represents the **current state** you are tracking. By moving the pointers, you update that state in $O(1)$ time rather than re-scanning the whole window, leading to an overall $O(n)$ complexity.
