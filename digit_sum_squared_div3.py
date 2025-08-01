"""
💡 Challenge: Sum of Squares for Odd Digits Only
Task:
Print numbers between 1 and 300 where the sum of the squares of their digits is divisible by 3.

Rules:

Only include odd digits (1, 3, 5, 7, 9) when calculating the sum of squares.
Print 5 results per line.
At the end, display the total count and sum of all such numbers.
 total count and sum.
"""

count = 0
sum = 0

for i in range(1,301):
    digitSum = 0
    temp = i

    # calculate sum of digits
    while temp > 0:
        digitSum += temp % 10 
        temp //= 10
    digitProduct = digitSum * digitSum

    #check if product is divisible by 3
    if digitProduct % 3 == 0:
        print(i, end = " ")
        count += 1
        sum += i

        # print new line after every 5 numbers
        if count % 5 == 0:
          print()        

print("\nCount:", count)
print("Sum:", sum)



