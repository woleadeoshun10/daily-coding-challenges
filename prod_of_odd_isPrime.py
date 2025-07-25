"""
🧠 Challenge: Product of Odd Digits is Prime
Problem Statement:

Print all numbers from 10 to 300 where:

The product of the odd digits in the number is a prime number.

Print 5 numbers per line.

At the end, print the total count and the sum of all valid numbers.

🔍 Example:
35 → digits: 3, 5 → 3 × 5 = 15 → ❌ Not prime

73 → digits: 7, 3 → 7 × 3 = 21 → ❌ Not prime

53 → 5 × 3 = 15 → ❌

23 → 2 (even), 3 (odd) → product = 3 → ✅ (3 is prime) → print 23
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

for i in range(10, 301):
    temp = i
    prodNum = 1
    while temp > 0:
        digit = temp % 10
        if digit % 2 == 1:
            prodNum *= digit
        temp //= 10
    if isPrime(prodNum):
        print(i, end=" ")
        count += 1
        sum_num += i
        if count % 5 == 0:
            print()
print("\nCount: ",count)
print("Sum: ",sum_num)


"""
I didnt think I could do that.
"""