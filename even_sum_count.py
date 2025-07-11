# Print even numbers from 50 to 100
# Print 5 numbers per line
# Show total count and sum

count = 0
sum = 0

for i in range(50, 101, 2):
    print(i, end=" ")
    count += 1
    sum += i
    if count % 5 == 0:
        print()

print("\nCount:", count)
print("Sum:", sum)
