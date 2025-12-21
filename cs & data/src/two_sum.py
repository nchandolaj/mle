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
nums = [3, 2, 4]
target = 6
answer = twoSum_Approach1(nums, target)
print(f"{answer=}")

nums = [3, 2, 4, 10, 6]
target = 9
answer = twoSum_Approach2(nums, target)
print(f"{answer=}")