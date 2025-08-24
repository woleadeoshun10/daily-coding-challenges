"""
Write a program that prints numbers from 1 to 100, but:
Add the number to the sum if the number is at an odd index (like 1st, 3rd, 5th...).
Subtract the number from the sum if the number is at an even index.
At the end, print:
All the numbers with their operation (+ or -)
The final result of the alternating sum
The total count of numbers added and subtracted
🔢 Sample Output Format:
+1 -2 +3 -4 +5 -6 ... +99 -100
Final Result: -50
Added Count: 50
Subtracted Count: 50
"""



sum_odd = 0
diff_even = 0
count = 0

for i in range(1,101):
  if i % 2 == 1:
    sum_odd += i
    print("+" + str(i) , end=" ")
  else:
    diff_even -= i
    print("-" + str(i) , end=" ")
  count += 1
  if count % 10 == 0:
    
    
print("\nFinal Result: ", sum_odd + diff_even)
print("Added Count: ",sum_odd)
print("Subtracted Count: ", diff_even)


"""
Chat Gpt Solution:


sum_odds = 0
sum_evens = 0
count = 0

for i in range(1, 101):
    if i % 2 == 1:
        sum_odds += i
        print(f"+{i}", end=" ")
    else:
        sum_evens += i
        print(f"-{i}", end=" ")

    count += 1
    if count % 10 == 0:
        print()

final_result = sum_odds - sum_evens

print("\nFinal Result:", final_result)
print("Sum of Odds (Added):", sum_odds)
print("Sum of Evens (Subtracted):", sum_evens)

"""
