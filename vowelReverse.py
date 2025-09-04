"""
Problem: Reverse Only Vowels

Write a function that takes a string s and returns the string with only the vowels reversed, while keeping the positions of all other characters the same.

Example 1:
Input: "hello"
Output: "holle"

Example 2:
Input: "leetcode"
Output: "leotcede"

Example 3:
Input: "ChatGPT"
Output: "ChtaGPT"

"""

def reverseVowel(s):
    vowels = set("aeiouAEIOU")
    s = list(s)
    left, right = 0, len(s) - 1
    
    
    while left <= right:
        if s[left] not in vowels:
            left += 1
        elif s[right] not in vowels:
            right -= 1
        else:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    return "".join(s)
        
        
print(reverseVowel("leetcode"))       
print(reverseVowel("loveleetcode")) 
print(reverseVowel("aabb"))     
print(reverseVowel("hello"))         
