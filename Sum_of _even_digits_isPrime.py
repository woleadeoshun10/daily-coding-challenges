"""
🔥 Challenge:
"Sum of Even Digits is Prime"

🧠 Problem Statement:
Write a program that prints all numbers from 100 to 500 where:

The sum of the even digits in the number is a prime number.

Print 5 numbers per line.

Print the total count of such numbers.

Print the sum of all such numbers.
"""
def primeNumber(n):
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

for i in range(100,501):
    temp = i
    digitSum = 0
    while temp > 0:
        digit = temp % 10
        if digit % 2 == 0:
            digitSum += digit
        temp //= 10
    if primeNumber(digitSum):
        print(f"{i:4}", end=" ")
        count += 1
        sum_num += i
        if count % 5 == 0:
            print()
print("\nCount: ", count)
print("Sum: ",sum_num)



