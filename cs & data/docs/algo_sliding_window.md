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
| **MLE:** Rolling 7-day average | **Sliding Window** (Fixed Window K. L and R move right) |
| **MLE:** Find the shortest burst of error logs | **Sliding Window** (Dynamic) |

### Key Takeaway
The "Window" represents the **current state** you are tracking. By moving the pointers, you update that state in $O(1)$ time rather than re-scanning the whole window, leading to an overall $O(n)$ complexity.

---

# MLE Relevance: Data Streams & Time-Series
In Machine Learning Engineering (MLE), the sliding window mimics how we handle **streaming data:**

* **Feature Engineering:** Calculating a "rolling average" of stock prices over the last 24 hours.
* **Stride in CNNs:** Convolutional Neural Networks use a sliding window (kernel) to extract features from images.
* **Anomaly Detection:** Monitoring a data stream for spikes within a specific time window.

## Time-Series Data Stream 
In the context of software engineering and Machine Learning (MLE), **time-series data streams** represent a continuous flow of data points indexed in chronological order. Unlike a static database, a stream is "infinite"—you process data as it arrives.

The **Sliding Window** pattern is the primary tool used to make sense of this infinite flow.

## 1. What makes it a "Stream"?
A stream has three distinct characteristics that require specific algorithmic approaches:
1.  **Temporal Dependency:** The value at $T_n$ is often related to the value at $T_{n-1}$.
2.  **Volatility:** Data arrives at high velocity; you cannot afford $O(n^2)$ operations because the "window" of time to process each point is tiny.
3.  **Unboundedness:** You cannot see the "end" of the data, so algorithms must be able to summarize the past without storing everything.

## 2. Sliding Windows in Streams
When dealing with streams, we use sliding windows to transform raw data into **features** for ML models.

### **A. Rolling Aggregates (Fixed Window)**
This is used for "smoothing" noise or calculating trends.
* **Example:** A 5-minute rolling average of CPU usage.
* **Implementation:** As a new packet arrives (Right pointer expands), the packet from 5 minutes ago is dropped (Left pointer shrinks).

### **B. Sessionization (Variable Window)**
This is used to group related events that occur close together.
* **Example:** A user’s "session" on a website.
* **Logic:** The window stays open as long as the user clicks something every 30 seconds. If they stop for more than 30 seconds (constraint violated), the window "shrinks" (closes) and a new session begins.

## 3. The "State" Hurdle in MLE
In standard LeetCode problems, your "window" is usually just an array in memory. In a real-time stream (like Kafka or Flink), the **State** is the biggest hurdle.

| Challenge | Description | Sliding Window Solution |
| :--- | :--- | :--- |
| **Out-of-Order Data** | Data arrives late due to network lag. | **Watermarking:** Keeping the window "open" slightly longer to catch late data. |
| **Memory Management** | Storing millions of events is impossible. | **Aggregating on the fly:** Instead of storing all numbers, only store the `sum` and `count`. |
| **Concept Drift** | The patterns in the data change over time. | **Weighted Windows:** Giving more importance (weight) to newer data in the window. |

## 4. Practical Python Example: Simple Data Stream
This simulates a stream where we calculate a rolling average using $O(1)$ per new data point.

```python
class StreamProcessor:
    def __init__(self, window_size):
        self.k = window_size
        self.window = []
        self.current_sum = 0

    def next(self, val):
        # 1. Expand (Include new data)
        self.window.append(val)
        self.current_sum += val
        
        # 2. Shrink (Remove old data once window > k)
        if len(self.window) > self.k:
            outgoing = self.window.pop(0)
            self.current_sum -= outgoing
            
        # 3. Output (Average)
        return self.current_sum / len(self.window)

# Simulated Stream
stream = [10, 20, 30, 40, 50]
proc = StreamProcessor(window_size=3)
for val in stream:
    print(f"New data: {val}, Rolling Avg: {proc.next(val)}")
```

## 5. Summary Table: Streaming Patterns

| Pattern | Goal | MLE Use Case |
| :--- | :--- | :--- |
| **Tumbling Window** | Non-overlapping fixed chunks | Hourly reporting / billing |
| **Sliding Window** | Overlapping fixed chunks | Real-time monitoring / Trend detection |
| **Session Window** | Data-driven variable chunks | User behavior analysis |


