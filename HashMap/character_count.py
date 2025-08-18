"""
Write a function that counts how many times each letter appears in a word.

Example:

Input: "banana"
Output: {'b': 1, 'a': 3, 'n': 2}

"""

def count_letters(word):
    counts = {}
    for ch in word:
        if ch in counts:
            counts[ch] += 1   # already seen → increase count
        else:
            counts[ch] = 1    # first time → set to 1
    return counts

# Example usage
word = "banana"
print(count_letters(word))
