'''
Problem: Given two strings s and t, return true if t is an anagram of s, and false otherwise.

LC242: https://leetcode.com/problems/valid-anagram 
'''
import random
import string

def isAnagram_Approach1(s: str, t: str) -> bool:
    '''
    Algorithm: Sort both strings and compare. 
    Time Complexity: O(N log N)
    Space Complexity: O(n) 
    '''
    # Pre-Conditions
    if (len(s) == 0) | (len(t) == 0):
            return False

    if len(s) != len(t):
        return False

    # Proceed to Solution
    sorted_s = sorted(s)
    sorted_t = sorted(t)

    if sorted_s == sorted_t:
      return True
    else:
      return False


def isAnagram_Approach2(s: str, t: str) -> bool:
    '''
    Algorithm: Use HashMap to store the unique characters & its frequency 
               from one of the input strings. Loop through the other string
               decrementing the count of matching character from the HashMap.
               Check HashMap to see if all character counts are zero.
    Time Complexity: O(n)
    Space Complexity: O(1). HashMap space is limited by the number of possible characters.
    '''
    # Pre-Conditions
    if (len(s) == 0) | (len(t) == 0):
            return False

    if len(s) != len(t):
        return False
   
    # Proceed to algorithm
    s2 = {}

    for c in s:
        if c in s2:
            s2[c] += 1
        else:
            s2[c] = 1
    
    for c in t:
        if c not in s2:
            return False
        else:
            s2[c] -= 1

    for c in s2:
      if s2[c] > 0:
        return False

    return True

def isAnagram_Approach3(s: str, t: str) -> bool:
    '''
    # 
    Algorithm: Use HashMap to store the unique characters & its frequency 
               from one of the input strings. Loop through the other string
               decrementing the count of matching character from the HashMap.
               Check HashMap to see if all character counts are zero.
    Time Complexity: O(n)
    Space Complexity: O(1). HashMap space is limited by the number of possible characters.
    NOTE: Slightly better time complexity than Approach 2.
    '''
    # Pre-Conditions
    if (len(s) == 0) | (len(t) == 0):
            return False

    if len(s) != len(t):
        return False
   
    # Proceed to algorithm

    # Hash map to store characters and it frquency
    char_counts = {}

    for i in range(len(s)):
        c1= s[i]
        c2 = t[i]

        # check char from first string in hash_map, 
        # increment count or start with -1
        if c1 in char_counts:
          char_counts[c1] += 1
        else: 
          char_counts[c1] = 1
        
        # check char from second string in hash_map, 
        # decrement count or start with -1
        if c2 in char_counts:
          char_counts[c2] -= 1
        else: 
          char_counts[c2] = -1
    
    for i, (c, n) in enumerate(char_counts.items()):
        if char_counts[c] != 0:
          return False
    '''
    for c in char_counts:
      if char_counts[c] != 0:
        return False
    '''

    return True


# CODE TO CALL FUNCTIONS

# Helper Function
def random_string():
  # character set
  chars = string.ascii_letters + string.digits
  
  # Randomly generate length of string. Limit from 0 to 5 characters.
  n = random.randint(0, 5)

  # randomly pick characters
  random_chars = random.choices(chars, k=n)

  return ''.join(random_chars)

# Call algorithms
#s = random_string()
#t = random_string()
#print(f"{s=} {t=}")
s = "car"
t = "tac"
answer = isAnagram_Approach1(s, t)
print(f"{s=} {t=} {answer=}")

s = "car"
t = "tac"
answer = isAnagram_Approach2(s, t)
print(f"{s=} {t=} {answer=}")

s = "anagram"
t = "gnarama"
answer = isAnagram_Approach3(s, t)
print(f"{s=} {t=} {answer=}")

