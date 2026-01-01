# Container With Most Water

The **Container With Most Water** problem is the quintessential example of **Greedy Logic** applied to the Two-Pointer pattern. It challenges you to make the "locally optimal" choice at each step to reach the global maximum.

## 1. The Problem Statement
You are given an array `height` where each value represents the height of a vertical line. You need to find two lines that, together with the x-axis, form a container that holds the most water.

* **The Formula:** $\text{Area} = \text{width} \times \min(\text{height}_1, \text{height}_2)$
* **The Constraint:** The width is the distance between the two indices. The height is limited by the **shorter** of the two lines (the "bottleneck").

## 2. The Greedy Strategy
A brute-force solution ($O(n^2)$) would check every possible pair. The Greedy Two-Pointer approach ($O(n)$) starts with the maximum possible width and narrows it down.

1.  **Start at the ends:** Place `left` at index 0 and `right` at the last index.
2.  **Calculate Area:** Find the area and update your `max_area`.
3.  **The Greedy Move:** Compare `height[left]` and `height[right]`. **Move the pointer pointing to the shorter line.**

## 3. The "Hurdle": Proving the Greedy Choice
The biggest hurdle is understanding **why** we move the shorter side. It feels counter-intuitive to give up width, but here is the mathematical proof:

### **The Bottleneck Logic**
* The area is determined by the shorter side.
* If we move the **taller** side inward, the width decreases. Even if we find an even taller line, the area cannot increase because it is still limited by the original shorter side (the bottleneck).
* Therefore, the only way to potentially find a larger area is to move the **shorter** side in hopes of finding a significantly taller line that compensates for the loss in width.

## 4. Implementation in Python

```python
def maxArea(height):
    max_val = 0
    left = 0
    right = len(height) - 1
    
    while left < right:
        # Calculate current area
        width = right - left
        h = min(height[left], height[right])
        max_val = max(max_val, width * h)
        
        # The Greedy Move: 
        # Always move the pointer that is currently the bottleneck.
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    return max_val
```

## 5. Comparison: 3Sum vs. Water Container

| Feature | 3Sum (Opposite Ends) | Water Container (Greedy) |
| :--- | :--- | :--- |
| **Goal** | Find specific sums | Maximize a calculation (Area) |
| **Movement** | Based on `sum` vs `target` | Based on `height[l]` vs `height[r]` |
| **Sorting** | Required ($O(n \log n)$) | **Not** required ($O(n)$) |
| **Duplicates** | Must be manually skipped | Not an issue (simply move past) |
