# Write a program that prints numbers from 1 to 100, but:
# + Add odd numbers
# - Subtract even numbers
# Print operations, final result, and counts

sum_odd = 0
diff_even = 0
count = 0

for i in range(1, 101):   # 1 to 100
    if i % 2 == 1:
        sum_odd += i
        print(f"+{i}", end=" ")
    else:
        diff_even -= i
        print(f"-{i}", end=" ")
    
    count += 1
    if count % 10 == 0:
        print()  # New line every 10 numbers

total_res = sum_odd + diff_even

print("\nFinal Result:", total_res)
print("Added Count:", sum_odd)
print("Subtracted Count:", diff_even)
