"""
"Reverse and Prime Digit Sum"

Write a program that prints all numbers from 200 to 600 where:

When the number is reversed,

The sum of its digits in the reversed number is prime.

📌 Also:

Print 5 numbers per line.

Print the total count of such numbers.

Print the sum of all such numbers.

"""

def reverseNum(n):
    reverse_num = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        reverse_num = reverse_num * 10 + digit
        temp //= 10
    return reverse_num

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

for i in range(200, 601):
    num = reverseNum(i)
    sumDigit = 0
    while num > 0:
        digit = num % 10
        sumDigit += digit
        num //= 10
    if isPrime(sumDigit):
        print(f"{i:4}", end = " ")
        count += 1
        sum_num += i
        if count % 5 == 0:
            print()
print("\nCount: ",count)
print("Sum: ",sum_num)


