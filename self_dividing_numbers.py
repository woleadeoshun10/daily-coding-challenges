"""
Challenge: "Self-Dividing Numbers"
🟢 LeetCode-Style Easy Problem
📘 Problem Statement:
A number is called a self-dividing number if:

It is divisible by each of its digits
It does not contain the digit 0
Write a function that prints all the self-dividing numbers between 1 and 200.
"""

def print_self_dividing_numbers(start: int, end: int) -> None:
  for num in range(start, end + 1):
    #make temp equal num
    temp = num
    is_Valid = True

    while temp > 0:
      #remove the last number
      digit = temp % 10
 #if last number is 0 or not divisible by its digit its false
      if digit == 0 or num % digit != 0:
        is_Valid = False
        break
        #remove the number
      temp //= 10

    #if its true print the number
    if is_Valid:
      print(num, end= " ")

print_self_dividing_numbers(1, 200)


