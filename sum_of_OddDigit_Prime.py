"""
🔥 Daily Python Challenge: Sum of Odd Digits That Are Prime

🧠 Problem Statement:
Write a program that prints all numbers from 10 to 300 where the sum of the odd digits in the number is a prime number.

📌 Also:

Print 5 numbers per line

Print the total count of such numbers

Print the sum of all such numbers

🔍 Example:
35 → 3 + 5 = 8 ❌ (not prime)

27 → 7 + 0 = 7 ✅ (prime)

123 → 1 + 3 = 4 ❌

135 → 1 + 3 + 5 = 9 ❌

113 → 1 + 1 + 3 = 5 ✅ (prime) ✅✅✅
"""

def isPrime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

count = 0
sum_num = 0
for i in range (10,301):
    temp = i
    oddSum = 0
    while temp > 0:
        digit = temp % 10
        if digit % 2 == 1:
            oddSum += digit
        temp //= 10
    isPrimeNum = isPrime(oddSum)
    if isPrimeNum:
        print(i, end=" ")
        count += 1
        sum_num += i
        if count % 5 == 0:
            print()
print("\nCount: ",count)
print("Sum: ",sum_num)