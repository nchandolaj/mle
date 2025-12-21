'''
Problem: Given an integer array nums, return true if any value appears
         at least twice in the array, and return false if every element 
         is distinct.

LC217: https://leetcode.com/problems/contains-duplicate/         
'''
import random

# Brute Force: Loop through the list in two nested loops
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def containsDuplicate_Approach1(nums: list[int]) -> bool:
    for i in range(len(nums)):
      for j in range(i+ 1, len(nums)):
        if nums[i] == nums[j]:
            return True
    return False

# Better Solution: Use a Set to store . 
#                  Loop through the first list and 
#                  compare with the Set variable.
# Time Complexity: O(n)
# Space Complexity: O(n)
def containsDuplicate_Approach2(nums: list[int]) -> bool:
    temp = set()
    for i, n in enumerate(nums):
        if n in temp:
            return True
        temp.add(n)
    return False

# CODE TO CALL FUNCTIONS
nums = [random.randint(-5, 10) for _ in range(5)]
answer = containsDuplicate_Approach1(nums)
print(f"{nums=} {answer=}")

nums = [random.randint(-100, 100) for _ in range(10)]
answer = containsDuplicate_Approach2(nums)
print(f"{nums=} {answer=}")