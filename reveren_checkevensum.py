"""
🔥 Challenge:
"Reverse and Check Even Sum"

🧠 Problem Statement:
Write a program that prints all numbers from 50 to 400 where:

When the number is reversed,

The sum of its digits in the reversed number is even.

📌 Also:

Print 5 numbers per line.

Print the total count of such numbers.

Print the sum of all such numbers.

"""

def reverseNum(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return reversed_num
    
count = 0
sum_num = 0
for i in range(50, 401):
    temp = reverseNum(i)
    digitNum = 0
    while temp > 0:
        digit = temp % 10
        digitNum += digit
        temp //= 10
    if digitNum % 2 == 0:
        print(f"{i:4}", end=" ")
        count += 1
        sum_num += i
        if count % 5 == 0:
            print()
print("\nCount: ",count)
print("Sum: ",sum_num)



    