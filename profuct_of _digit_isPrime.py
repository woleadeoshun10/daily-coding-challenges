"""
🧠 Problem Statement
Print all numbers from 10 to 300 where the product of all digits is a prime number.

✅ Requirements
Print 5 numbers per line

Print the total count of such numbers

Print the sum of all such numbers

🔍 Example
23 → 2 * 3 = 6 ❌

53 → 5 * 3 = 15 ❌

13 → 1 * 3 = 3 ✅

29 → 2 * 9 = 18 ❌

37 → 3 * 7 = 21 ❌

11 → 1 * 1 = 1 ❌

17 → 1 * 7 = 7 ✅


"""


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
for i in range(10,301):
    temp = i;
    productNum = 1
    while temp > 0:
        digit = temp % 10
        productNum *= digit
        temp //= 10
    if isPrime(productNum):
        print(f"{i:4}", end=" ")
        count += 1
        sum_num += i
        if count % 5 == 0:
            print()
print("\nCount: ",count)
print("Sum: ",sum_num)
        
        
        
        