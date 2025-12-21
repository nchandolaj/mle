# The "Two-Sum" Problem - Space-Time Trade-off Explained

*Problem: Given an array 'nums' and a 'target', find two numbers that add up to 'target'.*

**Assumptions**
* **Input:** An array of integers `nums` and an integer `target`.
* **Output:** The **indices** of the two numbers such that they add up to `target`.
* **Constraint:** Assuming that each input would have exactly one solution, and you may not use the same element twice.

*Example:*
`nums = [2, 7, 11, 15]`, `target = 9`
* `nums[0] + nums[1] = 2 + 7 = 9`
* **Output:** `[0, 1]`


## Approach 1: Brute Force (Low Space, High Time)
**The Logic:**
We check every possible pair of numbers. We use a nested loop: "For every number $i$, check every other number $j$ to see if they add up to the target."

**Python Code:**
```python
def twoSum_brute(nums, target):
    n = len(nums)

    # Outer loop iterates from the first element to the second-to-last
    for i in range(n):

        # Inner loop iterates from i+1 to the end
        for j in range(i + 1, n):

            if nums[i] + nums[j] == target:
                return [i, j]

    return []
```

**Trade-off Analysis:**
* **Time Complexity:** $O(n^2)$ This is Quadratic Time. If your input has 10,000 items, the CPU has to perform roughly 50,000,000 checks. This is usually too slow for production systems.
* **Space Complexity:** $O(1)$ Constant Space. We are not creating any new data structures; we are just reading the existing array. This is very memory efficient.


## Approach 2: The Hash Map (High Space, Low Time)
**The Logic:**
This is the standard "Space-Time Trade-off." Instead of scanning the array repeatedly to find a match (target - current_number), we store the numbers we've seen so far in a Hash Map (Dictionary) for instant ($O(1)$) lookup. 

As we iterate through the array once:
1. Calculate the diff needed (target - current_value).
2. Check if diff is already in our dictionary.
   - Yes? We found the pair! Return the current index and the index stored in the dict.
   - No? Store the current number and its index in the dictionary (val: index).

**Python Code:**
```python
def twoSum_optimal(nums, target):
    # Create a dictionary to store {value: index}
    # This is where we "spend" our memory space
    prev_map = {} 
    
    for i, n in enumerate(nums):
        diff = target - n
        
        # Check if the difference exists in the map
        if diff in prev_map:
            return [prev_map[diff], i]
        
        # If not, store the current number and its index
        prev_map[n] = i
        
    return []
```

**Trade-off Analysis:**
* **Time Complexity:** $O(n)$ Linear Time. We only loop through the list once. Lookup in a dictionary is $O(1)$ on average. This is significantly faster than brute force.
* **Space Complexity:** $O(n)$ Linear Space. In the worst case (no match found until the very end), we store every single item in the dictionary. If the array is massive (e.g., 1 billion items), this might crash your RAM.


## Approach 3: Sorting + Two Pointers (The Middle Ground)
**The Logic:**
If the array were sorted, we could put one pointer at the start (Left) and one at the end (Right).
* If Left + Right > target: The sum is too big. Move Right pointer down.
* If Left + Right < target: The sum is too small. Move Left pointer up.
$Note$: Since the original problem asks for **indices**, and sorting messes up indices, this approach requires us to store the original indices before sorting (e.g., [(2,0), (7,1), ...]), which takes $O(n)$ space anyway. However, if the input is already sorted (LeetCode 167), this is the superior approach.

**Python Code (Assuming Sorted Input):**
```python
def twoSum_sorted(nums, target):
    l, r = 0, len(nums) - 1
    
    while l < r:
        currentSum = nums[l] + nums[r]
        
        if currentSum > target:
            r -= 1
        elif currentSum < target:
            l += 1
        else:
            return [l, r]
            
    return []
```

**Trade-off Analysis:**
* **Time Complexity:** $O(n \log n)$ due to sorting (or $O(n)$ if already sorted).
* **Space Complexity:** $O(1)$ (if already sorted).

## Summary of Trade-offs

| Approach | Time Complexity | Space Complexity | When to use? |
| :--- | :--- | :--- | :--- |
| **Brute Force** | $O(n^2)$ (Slow) | $O(1)$ (Minimal) | Never in an interview (unless $N < 50$). |
| **Hash Map** | **$O(n)$ (Fast)** | **$O(n)$ (Heavy)** | **Standard Interview Answer.** Best for unsorted arrays. |
| **Two Pointers** | $O(n)$ | $O(1)$ | Best if the array is **already sorted**. |


# References
* [**The Big O Notation**](https://github.com/nchandolaj/mle/blob/main/cs%20&%20data/docs/big_o_notation.md): Discuss Time vs. Space complexity. Understand why $O(1) < O(\log n) < O(n) < O(n \log n) < O(n^2) < O(n!)$.

**Note:** Two-Sum Problem example is a sub-topic of the following discussions:
* [**The Pythonic Standard**](https://github.com/nchandolaj/mle/blob/main/cs%20%26%20data/docs/the_pythonic_standard.md)
* [**Space-Time Trade-off**](https://github.com/nchandolaj/mle/blob/main/cs%20&%20data/docs/space_time_trade_off.md)
