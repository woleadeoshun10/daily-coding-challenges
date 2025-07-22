"""
🧠 Challenge: Multiply Even Digit Sum
Problem Statement:
Print numbers from 1 to 250 where the sum of even digits in the number is divisible by 4.
Your Task:

Print only those numbers where the sum of even digits (like 0, 2, 4, 6, 8) is divisible by 4.
Print 5 numbers per line.
At the end, print the total count and the sum of all valid numbers.

"""

"""
Challenge:
Print numbers from 4 to 250 where the sum of their even digits is divisible by 4.
- Print 5 numbers per line.
- At the end, print total count and sum.
"""

count = 0
sum_num = 0

for i in range(4,251):
    temp = i
    digitSum = 0
    while temp > 0:
        digit = temp % 10
        if digit % 2 == 0:
         digitSum += digit
        temp //= 10
        
    if digitSum != 0 and digitSum % 4 == 0:
      print(i,end=" ")
      count += 1
      sum_num += i
      if count % 5 ==0:
        print()
print("\nCount: ",count)
print("Sum: ", sum_num)



"""
🧠 Challenge: Multiply Even Digit Sum
Problem Statement:
Print numbers from 1 to 250 where the sum of even digits in the number is divisible by 4.
Your Task:

Print only those numbers where the sum of even digits (like 0, 2, 4, 6, 8) is divisible by 4.
Print 5 numbers per line.
At the end, print the total count and the sum of all valid numbers.

"""

"""
Challenge:
Print numbers from 4 to 250 where the sum of their even digits is divisible by 4.
- Print 5 numbers per line.
- At the end, print total count and sum.
"""

count = 0
sum_num = 0

for i in range(4,251):
    temp = i
    digitSum = 0
    while temp > 0:
        digit = temp % 10
        if digit % 2 == 0:
         digitSum += digit
        temp //= 10
        
    if digitSum != 0 and digitSum % 4 == 0:
      print(i,end=" ")
      count += 1
      sum_num += i
      if count % 5 ==0:
        print()
print("\nCount: ",count)
print("Sum: ", sum_num)



