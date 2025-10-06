
"""
🧠 Problem Statement:
Print all numbers from 10 to 300 where the product of the digits is a palindrome number.

✅ Also:
Print 5 numbers per line

Print the total count of such numbers

Print the sum of all such numbers

🔍 What’s a palindrome?
A number that reads the same forwards and backwards.
Example: 121, 9, 44 ✅
Not: 42, 123, 90 ❌

🧪 Example:
22 → 2 * 2 = 4 → ✅ (4 is a palindrome)

36 → 3 * 6 = 18 → ❌ (not a palindrome)

121 → 1 * 2 * 1 = 2 → ✅ (2 is a palindrome)

"""


def isPalindrome(n):
    return str(n) == str(n)[::-1]

count = 0
sum_num = 0
for i in range(10,301):
    temp = i
    productNum = 1
    while temp > 0:
        digit = temp % 10
        productNum *= digit
        temp //= 10
    if isPalindrome(productNum):
        print(f"{i:4}", end=" ")
        count += 1
        sum_num += i
        if count % 5 == 0:
            print()
print("\nCount: ", count)
print("Sum: ", sum_num)

