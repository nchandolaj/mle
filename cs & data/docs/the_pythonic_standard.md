# The Pythonic Standard

*Focus: Writing clean, idiomatic code and understanding complexity.*

## Whats Covered?
* **Big O Notation:** Review Time vs. Space complexity. Understand why $O(1) < O(\log n) < O(n) < O(n \log n) < O(n^2) < O(n!)$.
* **Python Internals:**
        * List vs. Tuple vs. Set (Lookup times).
        * `dict` implementation (Hash map).
        * List slicing `arr[start:stop:step]` (Note: Slicing creates a copy, costing $O(k)$ memory).

## Big O Notation

### What is it?

Think of **Big O Notation** not as a math equation, but as a "Stress Test for Reality." It **measures** how much a system "freaks out" as you give it more work to do. 

In programming, $n$ represents the number of items you’re dealing with. Big O describes the relationship between that $n$ and the resources (usually **compute time**, but can also be **compute space**) required to finish the job (by the algorithm).

### Time Complexity

**Summary Reference Table**
| Big O | Name | Performance | Memory Hook |
| :--- | :--- | :--- | :--- |
| **O(1)** | Constant | Instant | The billionaire's watch |
| **O(log n)** | Logarithmic | Great | The teleporting bounty hunter |
| **O(n)** | Linear | Fair | The vampire handshake |
| **O(n log n)** | Log-Linear | Fair | Deck of cards |
| **O(n^2)** | Quadratic | Slow | High school gossip |
| **O(2^n)** | Exponential | Horrible | The zombie apocalypse |
| **O(n!)** | Factorial | Impossible | Super-villains |

#### Time Complexity discussion, along with Python Examples
1. **O(1) - Constant Time**
   - No matter how much $n$ grows, the time stays the same.
   - **Scenario:** You are a billionaire who owns a private island. You have one gold watch. Whether you have 1 guest or 1,000,000 guests, it takes you the **exact same amount of time** to look at your wrist and tell someone the time.
   - **Vibe:** Complete indifference to the scale of the universe.
```python
def check_watch(guests):
    # It doesn't matter if the list has 1 or 1,000,000 items
    return guests[0]
```
3. **O(log n) - Logarithmic Time**
   - **Smartest** way to work. Think of it as **Dive and Conquer**. Every time you take a step, you cut the remainder work in half.
   - **Scenario:** You are looking for a specific criminal in a 100-story building. You have a superpower: you can teleport to the middle floor and shout, "Is the criminal above me or below me?" By going to floor 50, then 25, you find them in about 7 steps. If the building grew to 1,000 floors, it would only take you 10 steps.
   - **Vibe:** Work smarter, not harder. 
```python
def find_criminal(building_floors, target_floor):
    low = 0
    high = len(building_floors) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if building_floors[mid] == target_floor:
            return f"Found on floor {mid}!"
        elif building_floors[mid] < target_floor:
            low = mid + 1
        else:
            high = mid - 1
    return "Not in building."
```
5. **O(n) - Linear Time**
   - Works grows exactly as fast as the input.
   - **Scenario:** You are a vampire who has to shake hands with every person at a concert. If there are 10 people, it takes 10 seconds. If there are 10,000 people, it takes 10,000 seconds.
   - **Vibe:** A long, honest day of manual labor.
```python
def vampire_handshake(people):
    for person in people:
        print(f"Handshaking with {person}")
```
7. **O(n log n) - Log-Linear Time**
   - **Gold-standard** for efficient sorting algorithms like **Merge Sort**.
   - **Scenario:** You have a deck of cards to sort. You split the deck in half, give it to a friend, they split it again, until you have individual cards, then merge them back in order. It’s more work than **O(n)** but significantly better than the next nightmare.
   - **Vibe:** Organized bureacracy that actually works.
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    # Divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # Conquer (Merge)
    return sorted(left + right)
```
9. **O(n^2) - Quadratic Time**
   - The "High School Drama" - Every new person added makes the work grow exponentially more complex.
   - **Scenario:** A high school party where every single person wants to gossip individually with **every other person** there. If there are 1,000 people, that’s 1,000,000 conversations. The party will end before the gossip does.
   - **Vibe:** A toxic relationship that drains your soul.
```python
def high_school_gossip(students):
    for i in students:
        for j in students:
            if i != j:
                print(f"{i} tells a secret to {j}")
```
11. **O(2^n) - Exponential Time**
    - "The Zombie Apocalypse" - **Game Over** of Big O.
    - **Scenario:** You are a zombie. Every minute, you bite one person and they become a zombie. Then, both of you bite someone else. The population doubles every step. With just 33 steps, you’ve infected the entire population of Earth (2^33 ~ 8.5B$).
    - **Vibe:** Total, uncontrollable global collapse.
```python
def zombie_growth(n):
    if n <= 1:
        return n
    # Each call creates TWO more calls
    return zombie_growth(n - 1) + zombie_growth(n - 2)
```
11. **O(n!) - Factorial Time**
    - **The Ultimate Nightmare** of Big O. This is the "Traveling Salesperson Problem" territory—where you have to find the shortest possible route between a list of cities by checking every single possible combination.
    - **Scenario:** You are a wedding planner for a group of 100 super-villains who all hate each other. You have to arrange them in a single line for a photo, but you must check **every single possible seating arrangement** to make sure no two enemies are standing next to each other.
    - **Vibe:** You will grow old and die, and the sun will burn out, before your code finishes running. **The Math:** If you have just **10 villains**, there are **3,628,800** combinations. If you have **20 villains**, there are **2,432,902,008,176,640,000** combinations.
```python
import itertools

def villain_photo_op(villains):
    # itertools.permutations generates n! possibilities
    # If len(villains) is 20, your computer will likely freeze forever.
    all_possible_lineups = list(itertools.permutations(villains))
    return all_possible_lineups
```

### Space Complexity 

**Summary Reference Table**
| Complexity | Memory Usage | The Hook |
| :--- | :--- | :--- |
| **$O(1)$** | Constant | The "Counter" (One number in your head) |
| **$O(n)$** | Linear | The "Spy's Notebook" (One entry per person) |
| **$O(n^2)$** | Quadratic | The "Grudge Map" (A grid of everyone vs everyone) |

#### Space Complexity in discussion, along with Python Examples
When we talk about **Space Complexity**, we aren't asking "How long does this take?" but rather "How much extra room do I need in my brain (RAM) to finish the job?"

Using our previous weird examples, here is how they affect your computer's memory.

1. **O(1) Space:** The "Sticky Note" (Constant Space)
   - No matter how big the problem gets, you only need one tiny piece of information to solve it.
   - **Scenario:** You are counting how many people enter a stadium. It doesn't matter if 10 people or 10,000,000 people enter; you only need one number in your head to keep track of the total.
   - **Vibe:** Minimalist living.
3. **O(n) Space:** The "Hoarder" (Linear Space)
   - For every new item you deal with, you need a new shelf to store it.
   - **Scenario:** You are a spy who needs to remember the name of every person you meet at a gala. If 500 people show up, you need a notebook with 500 lines. If the guest list doubles, you need twice as much paper.
   - **Vibe:** Buying a bigger house just to fit your stuff.
5. **O(n^2) Space:** The "Roommate from Hell" (Quadratic Space)
   - This usually happens when you create a 2D grid or a map of relationships.
   - **The Scenario:** You are building a "Grudge Map" for your town. For every person in town, you need a list of how they feel about every other person in town. If there are 10 people, you need a 10x10 grid (100 cells). If there are 1,000 people, you need a 1,000,000-cell spreadsheet.
   - **The Vibe:** Your "stuff" is taking over the entire neighborhood.
```python
# O(1) Space: Only one variable 'total', regardless of input size
def count_people(people_list):
    total = 0
    for person in people_list:
        total += 1
    return total

# O(n) Space: Creating a brand new list that grows with the input
def clone_villains(villains):
    secret_copy = []
    for v in villains:
        secret_copy.append(v)
    return secret_copy

# O(n^2) Space: Creating a matrix (list of lists)
def create_grudge_map(people):
    grid = []
    for i in people:
        row = []
        for j in people:
            row.append(f"{i} hates {j}")
        grid.append(row)
    return grid
```

## The Space-Time Trade-off
The **Space-Time Trade-off** is a fundamental concept in computer science where you reduce the **time** it takes to run an algorithm by consuming more **memory (space)**, or vice-versa.

**Time is money**. You are almost always expected to sacrifice some memory (RAM) to make your code run faster.

**The Core Principle**
- **Time Complexity:** How many operations the CPU performs. (We want to minimize this).
- **Space Complexity:** How much RAM your algorithm holds while running. We are okay with using more of this, within reason.

## Python Internals


# References
To continue your learning journey on this topic, please be sure to visit the following links:
- https://www.bigocheatsheet.com/




