"""
🧩 Foundation Exercise 3: Are Two Strings Anagrams?

👉 Problem:
Check if two strings are anagrams (they contain the same letters in any order).

Example:
"listen" and "silent" → ✅ True
"hello" and "world" → ❌ False

Hint: Compare frequency dictionaries of both strings.

"""
def compare_hash(wordA,wordB):
    countA = {}
    countB = {}
    for ch in wordA:
        if ch in countA:
            countA[ch] += 1
        else:
            countA[ch] = 1
            
    for ch in wordB:
        if ch in countB:
            countB[ch] += 1
        else:
            countB[ch] = 1
    
    if countA == countB:
       return True
    else:
        return False

wordA = "listen"
wordB = "silent"
print(compare_hash(wordA,wordB))

"""
Better solution
def compare_hash(wordA, wordB):
    if len(wordA) != len(wordB):
        return False
    
    count = {}
    for ch in wordA:
        count[ch] = count.get(ch, 0) + 1
    for ch in wordB:
        if ch not in count:
            return False
        count[ch] -= 1
        if count[ch] < 0:
            return False
    return True

"""


