"""
🧩 Foundation Exercise 1: Count Frequencies

👉 Problem:
Write a program that counts how many times each digit appears in a number.

Example:
n = 55221 → {5: 2, 2: 2, 1: 1}

"""
def digitCount(n):
    count = {}
    while n > 0:
        digit = n % 10
        if digit in count:
            count[digit] += 1
        else:
            count[digit] = 1
        n //= 10
    return count
    
num = 738199291293213312333
print("Number:", num)
print("Digit frequencies:", digitCount(num))
    


