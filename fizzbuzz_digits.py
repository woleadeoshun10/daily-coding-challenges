# From 1 to 150:
# - Print "FizzBuzz" if divisible by 15
# - Print "Fizz" if divisible by 3
# - Print "Buzz" if divisible by 5
# - Else, print the number if its digit sum is even
# - Print 5 values per line

count = 0

for i in range(1, 151):
    output = ""

    if i % 15 == 0:
        output = "FizzBuzz"
    elif i % 3 == 0:
        output = "Fizz"
    elif i % 5 == 0:
        output = "Buzz"
    else:
        digitSum = sum(int(d) for d in str(i))
        if digitSum % 2 == 0:
            output = str(i)

    if output:
        print(output, end=" ")
        count += 1
        if count % 5 == 0:
            print()
   


"""
# Print numbers from 1 to 150:
# - Print "FizzBuzz" if divisible by 15
# - Print "Fizz" if divisible by 3
# - Print "Buzz" if divisible by 5
# - Else, print the number if the sum of its digits is even
# - Print 5 results per line

count = 0  # Counter to track how many outputs have been printed (for formatting)

for i in range(1, 151):  # Loop from 1 to 150 inclusive
    printed = False  # Flag to track if we've printed something for this number

    if i % 15 == 0:  # Check if divisible by both 3 and 5
        print("FizzBuzz", end=" ")  # Print "FizzBuzz"
        printed = True  # Mark as printed

    elif i % 3 == 0:  # Check if divisible by 3 only
        print("Fizz", end=" ")  # Print "Fizz"
        printed = True  # Mark as printed

    elif i % 5 == 0:  # Check if divisible by 5 only
        print("Buzz", end=" ")  # Print "Buzz"
        printed = True  # Mark as printed

    if not printed:  # If none of the above printed
        digitSum = sum(int(d) for d in str(i))  # Calculate sum of digits
        if digitSum % 2 == 0:  # Check if digit sum is even
            print(i, end=" ")  # Print the number
            printed = True  # Mark as printed

    if printed:  # If anything was printed
        count += 1  # Increase the count
        if count % 5 == 0:  # Every 5 outputs, print a newline
            print()
"""
