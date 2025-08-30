"""
You are given a string s consisting of lowercase letters.
Return the index of the first non-repeating character in the string. If there is no such character, return -1.

Example 1:
Input:
s = "leetcode"
Output:
0
Explanation: 'l' is the first character that does not repeat.
Example 2:
Input:
s = "loveleetcode"
Output:
2
Explanation: 'v' is the first non-repeating character.
Example 3:
Input:
s = "aabb"
Output:
-1
Explanation: All characters repeat.
"""

def nonRepeat(s):
    character = {}

    for ch in s.lower():
        if ch not in character:
            character[ch] = 1
        else:
            character[ch] += 1
    for i, ch in enumerate(s.lower()):
        if character[ch] == 1:
            return i

    
    return -1
        
        
print(nonRepeat("leetcode"))       
print(nonRepeat("loveleetcode")) 
print(nonRepeat("aabb"))     
print(nonRepeat("sky"))         
