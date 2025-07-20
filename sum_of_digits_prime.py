"""
🧠 Challenge: Sum of Digits Is Prime
Problem Statement:
Write a program that prints all numbers from 1 to 300 such that the sum of their digits is a prime number.
Also:

Keep track of how many such numbers there are.
Print 5 numbers per line.
At the end, print the total count and the sum of all valid numbers.
🔢 Example:
If 23 → 2 + 3 = 5, and 5 is prime → ✅ print 23.
If 45 → 4 + 5 = 9, and 9 is not prime → ❌ skip.

"""
# Function to check if a number is prime
def is_prime(n):
    # Any number less than 2 is not a prime number
    if n < 2:
        return False

    i = 2  # Start checking from 2 (first prime)
    while i * i <= n:  # Only check up to the square root of n
        if n % i == 0:  # If n is divisible by i, it's not prime
            return False  # Exit early, not a prime
        i += 1  # Move to next number

    return True  # If no divisors found, n is a prime number


count = 0
total_sum = 0

for i in range(1, 301):
    temp = i
    digitSum = 0
    while temp > 0:
        digit = temp % 10
        digitSum += digit
        temp //= 10

    if is_prime(digitSum):
        print(i, end=" ")
        count += 1
        total_sum += i

        if count % 5 == 0:
            print()

print("\nCount:", count)
print("Sum:", total_sum)

"""
print numbers from 1 - 300, but only print numbers whose digit 
sum is a prime number
if its true print it and count it
if not dont print

print only 5 of the numbers per line
print the sum and count of the numbwrs you printed
"""
#Im not gonna lie, I had an hardtime with this because I did not know to get a prime number I needed a function. 

