'''
Problem Statement: Given an array of integers nums and an integer target, 
                    return indices of the two numbers such that they add up to target.

LC1: https://leetcode.com/problems/two-sum
     Slight variance because I am using random function to generate nums and target. 
     Using a predfined nums ands target, its exactly the same LeetCode problem.                    
'''
import random

# Brute Force: Loop through the list in two nested loops
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def twoSum_Approach1(nums: list[int], target: int) -> list[int]:
  for i in range(len(nums)):
      for j in range(len(nums)):
          if (i != j) & (nums[i] + nums[j] == target):
              return [i, j]

  return []

# Better Approach: Loop through the list and use a Hash Map / Python Dictonary 
#                  to store the values and indices of already traversed values. 
#                  Add the values from list and hash map to check if they sum to target. 
# Time Complexity: O(n)
# Space Complexity: O(n)
def twoSum_Approach2(nums: list[int], target: int) -> list[int]:
  temp = {}
  for i, n in enumerate(nums):
      diff = target - nums[i]
      if diff in temp:
        return [i, temp[diff]]
      temp[n] = i     
  return []


# CODE TO CALL FUNCTIONS
nums = [random.randint(-5, 5) for _ in range(6)]
target = random.randint(-5, 5)
answer = twoSum_Approach1(nums, target)
print(f"{nums=} {target=} {answer=}")

nums = [random.randint(-5, 5) for _ in range(6)]
target = random.randint(-5, 5)
answer = twoSum_Approach2(nums, target)
print(f"{nums=} {target=} {answer=}")