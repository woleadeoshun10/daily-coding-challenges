# Challenge:
# - Print all numbers between 1 and 100 that are divisible by 3
# - Count how many there are
# - Print their sum

count = 0
sum = 0

for i in range(1, 101):
    if i % 3 == 0:
        print(i, end=" ")
        count += 1
        sum += i

print("\nCount:", count)
print("Sum:", sum)
