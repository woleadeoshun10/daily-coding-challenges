"""
🧠 Problem Name: "Count of Special Even Digits"
🔹 Difficulty: Easy-Medium
🔸 Prompt:
Write a program that prints all numbers from 1 to 250 that meet the following condition:
The number has only even digits (e.g., 2, 4, 6, 8, 0 — no odd digits allowed).
At the end, print:
Total count of such numbers
Their sum
5 values per line for readability
💡 Example Output:
2 4 6 8 20  
22 24 26 28 40  
...
Total Count: 31  
Sum: 3078

"""

count = 0
total_sum = 0
for i in range (1,251):
  temp = i #let temp be i
  isEven = True
  while temp > 0:
    digit = temp % 10
    if digit % 2 != 0:
     isEven = False
     break
    temp //= 10
  if isEven:
    print(i, end=" ")
    count += 1
    total_sum += i
  if count % 5 == 0:
      print()
  
print("\nTotal Count: ", count)
print("Sum: ", total_sum)
  
