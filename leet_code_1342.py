"""
Prompt:

Write a program that takes a number as input and counts how many steps it takes to reduce the number to zero.

Rules:

If the number is even, divide it by 2.
If the number is odd, subtract 1.
Repeat this process until the number becomes 0.
Print the number of steps it took.
Example Input:
num = 14

Example Output:
6


Leet code problem - Number of Steps to Reduce a Number to Zero

"""




num = int(input("Enter a number: "))
count = 0

while num > 0:
  if num % 2 == 0:
    num = num / 2
  else:
    num = num - 1
  count += 1

print("\nCount: ", count)
  
