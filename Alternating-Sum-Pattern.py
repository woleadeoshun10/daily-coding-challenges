# Prints numbers 1 to 100 with alternating + and - operations
# Adds odd-index numbers, subtracts even-index numbers
# Then displays final result, and counts of added/subtracted numbers

sum_odd = 0
diff_even = 0
count = 0

for i in range(1, 101):
    if i % 2 == 1:
        sum_odd += i
        print(f"+{i}", end=" ")
    else:
        diff_even -= i
        print(f"-{i}", end=" ")
    
    count += 1
    if count % 10 == 0:
        print()  # new line every 10 numbers

total_res = sum_odd + diff_even

print(f"\nFinal Result: {total_res}")
print(f"Added Count: {sum_odd}")
print(f"Subtracted Count: {diff_even}")



