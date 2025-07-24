"""
Challenge: Reverse and Check Divisibility
Problem Statement:
Print all numbers from 10 to 300 where:
If you reverse the number, the reversed number is divisible by 7.
Print 5 numbers per line.
At the end, print the total count and sum of all valid numbers.
Example:
Number 70 → reversed = 07 = 7 → 7 is divisible by 7 → ✅ print 70.
Number 21 → reversed = 12 → 12 is not divisible by 7 → ❌ skip.


"""
def reverse_number(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10          # Get the last digit
        reversed_num = reversed_num * 10 + digit
        n //= 10                # Remove the last digit
    return reversed_num


count = 0
sum_num = 0

for i in range(10,301):
   reverseNum = reverse_number(i)
   if reverseNum % 7 == 0:
       print(i, end=" ")
       count += 1
       sum_num += i
       if count % 5 == 0:
           print()
print("\nCount: ", count)
print("Sum: ",sum_num)

