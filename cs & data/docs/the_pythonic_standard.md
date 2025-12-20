# The Pythonic Standard

*Focus: Writing clean, idiomatic code and understanding complexity.*

## Whats Covered?
* **Big O Notation:** Review Time vs. Space complexity. Understand why $O(1) < O(\log n) < O(n) < O(n \log n) < O(n^2)$.
* **Python Internals:**
        * List vs. Tuple vs. Set (Lookup times).
        * `dict` implementation (Hash map).
        * List slicing `arr[start:stop:step]` (Note: Slicing creates a copy, costing $O(k)$ memory).

## Big O Notation

### What is it?

Think of **Big O Notation** not as a math equation, but as a "Stress Test for Reality." It measures how much a system "freaks out" as you give it more work to do. 

In programming, $n$ represents the number of items you’re dealing with. Big O describes the relationship between that $n$ and the resources (usually **compute time**, but can also be **compute space**) required to finish the job (by the algorithm).

### The Complexity Hierarchy:

**Summary Reference Table**
| Big O | Name | Performance | Memory Hook |
| :--- | :--- | :--- | :--- |
| **O(1)** | Constant | Instant | The billionaire's watch |
| **O(log n)** | Logarithmic | Great | The teleporting bounty hunter |
| **O(n)** | Linear | Fair | The vampire handshake |
| **O(n log n)** | Log-Linear | Fair | Deck of cards |
| **O(n^2)** | Quadratic | Slow | High school gossip |
| **O(2^n)** | Exponential | Horrible | The zombie apocalypse |

1. **O(1) - Constant Time**
   - No matter how much $n$ grows, the time stays the same.
   - **Scenario:** You are a billionaire who owns a private island. You have one gold watch. Whether you have 1 guest or 1,000,000 guests, it takes you the **exact same amount of time** to look at your wrist and tell someone the time.
   - **Vibe:** Complete indifference to the scale of the universe.
3. **O(log n) - Logarithmic Time**
   - **Smartest** way to work. Think of it as **Dive and Conquer**. Every time you take a step, you cut the remainder work in half.
   - **Scenario:** You are looking for a specific criminal in a 100-story building. You have a superpower: you can teleport to the middle floor and shout, "Is the criminal above me or below me?" By going to floor 50, then 25, you find them in about 7 steps. If the building grew to 1,000 floors, it would only take you 10 steps.
   - **Vibe:** Work smarter, not harder. 
5. **O(n) - Linear Time**
   - Works grows exactly as fast as the input.
   - **Scenario:** You are a vampire who has to shake hands with every person at a concert. If there are 10 people, it takes 10 seconds. If there are 10,000 people, it takes 10,000 seconds.
   - **Vibe:** A long, honest day of manual labor.
7. **O(n log n) - Log-Linear Time**
   - **Gold-standard** for efficient sorting algorithms like **Merge Sort**.
   - **Scenario:** You have a deck of cards to sort. You split the deck in half, give it to a friend, they split it again, until you have individual cards, then merge them back in order. It’s more work than **O(n)** but significantly better than the next nightmare.
   - **Vibe:** Organized bureacracy that actually works.
9. **O(n^2) - Quadratic Time**
   - The "High School Drama" - Every new person added makes the work grow exponentially more complex.
   - **Scenario:** A high school party where every single person wants to gossip individually with **every other person** there. If there are 1,000 people, that’s 1,000,000 conversations. The party will end before the gossip does.
   - **Vibe:** A toxic relationship that drains your soul.
11. **O(2^n) - Exponential Time**
    - **Game Over** of Big O
    - **Scenario:** You are a zombie. Every minute, you bite one person and they become a zombie. Then, both of you bite someone else. The population doubles every step. With just 33 steps, you’ve infected the entire population of Earth (2^33 ~ 8.5B$).
    - **Vibe:** Total, uncontrollable global collapse.

## The Space-Time Trade-off
The **Space-Time Trade-off** is a fundamental concept in computer science where you reduce the **time** it takes to run an algorithm by consuming more **memory (space)**, or vice-versa.

**Time is money**. You are almost always expected to sacrifice some memory (RAM) to make your code run faster.

**The Core Principle**
- **Time Complexity:** How many operations the CPU performs. (We want to minimize this).
- **Space Complexity:** How much RAM your algorithm holds while running. We are okay with using more of this, within reason.

## Python Internals


