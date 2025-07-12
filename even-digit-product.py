"""
🔹 Challenge Title:
Count and Sum All Numbers Between 1–200 Where the Product of Digits Is Even

🔹 Instructions:
Loop through numbers from 1 to 200.
For each number, calculate the product of its digits.
If the product is even, print the number.
Also, keep track of:
The count of such numbers
The sum of such numbers
Print 5 numbers per line.
At the end, display the total count and sum.
"""

count = 0
sum = 0

for i in range(1,201):
    digitProduct = 1
    temp = i
    while temp > 0:
        digit = temp % 10 
        digitProduct *= digit
        temp //= 10
    if digitProduct % 2 == 0:
        print(i, end = " ")
        count += 1
        sum += i
    else:
       continue
    
    if count % 5 == 0:
        print()        

print("\nCount:", count)
print("Sum:", sum)


