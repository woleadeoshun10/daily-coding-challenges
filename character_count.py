"""
Write a function that counts how many times each letter appears in a word.

Example:

Input: "banana"
Output: {'b': 1, 'a': 3, 'n': 2}

"""

word = "banana"
counts = {}

for ch in word:
    if ch in counts:
        counts[ch] += 1
    else:
        counts[ch] = 1
print(counts)