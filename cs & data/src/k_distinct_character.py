'''
Challenge: Longest Substring with K Distinct Characters (Hard)
Given a string s and an integer k, find the length of the longest substring that contains at most k distinct characters.

Input: s = "eceba", k = 2
Expected Output: 3 (The substring is "ece").
'''

def longest_str(s: str, k: int) -> str:

  if len(s) < 2: return s

  # dict1 stores the count of characters
  dict1 = {}

  for r, c in enumerate(s):
    if c in dict1:
      dict1[c] += 1
      if dict1[c] >= k:
        return s[:r+1]
    else:
      dict1[c] = 1 
  
  return s


# TEST CASES
print(longest_str("eceba", 2))
print(longest_str("ecebbdabrheee", 3))
print(longest_str("ecebbdabrheee", 4))
print(longest_str("ecebbdabbrheee", 4))