# Print numbers from 1 to 100 divisible by 4 or 6 but not both
# Print 5 numbers per line
# Show count and sum

count = 0
sum = 0

for i in range(1, 101):
    if (i % 4 == 0 or i % 6 == 0) and i % 12 != 0:
        print(i, end=" ")
        count += 1
        sum += i

        # print 5 numbers per line
        if count % 5 == 0:
            print()

print("\nCount:", count)
print("Sum:", sum)
