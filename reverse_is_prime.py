"""
🧠 Challenge: Reverse Is Prime

📝 Problem Statement:
Print all numbers from 10 to 300 such that:

The reverse of the number is a prime number.

Example: 13 → 31 → ✅ because 31 is prime.

Also:

Keep track of the count of such numbers.

Print only 5 numbers per line.

Print the final count and sum of all valid numbers.
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
def reverseNum(n):
    return int(str(n)[::-1])

count = 0
sum_num = 0

for i in range(10, 301):
    isPrimeNum = isPrime(i)
    isreversePrime = isPrime(reverseNum(i))
    if isreversePrime and isPrimeNum:
        print(i,end=" ")
        count += 1
        sum_num += i
        if count % 5 == 0:
            print()
    
    
print("\nCount: ",count)
print("Sum: ",sum_num)


