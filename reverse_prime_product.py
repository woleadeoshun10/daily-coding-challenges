"""
🔥 Challenge: "Reverse Prime Product"

🧠 Problem Statement:
Print all numbers from 50 to 400 where:

When the digits of the number are reversed,

The product of the digits of the reversed number is a prime number.

📌 Also:

Print 5 numbers per line.

Print the total count of such numbers.

Print the sum of all such numbers.

"""

def reverseNum(n):
    temp = n
    reverse_num = 0
    while temp > 0:
        digit = temp % 10
        reverse_num = reverse_num * 10 + digit
        temp //= 10
    return reverse_num
    
def primeNum(n):
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

for i in range(50,401):
    reverse_num = reverseNum(i)
    temp = reverse_num
    productNum = 1
    while temp > 0:
        digit = temp % 10
        productNum *= digit
        temp //= 10
    if primeNum(productNum):
        print(f"{i:4}", end=" ")
        count += 1
        sum_num += i
        if count % 5 == 0:
            print()
print("\nCount: ", count)
print("Sum: ",sum_num)

