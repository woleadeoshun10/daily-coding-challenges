# Function to reverse a number
def reverse_number(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10          # Get the last digit
        reversed_num = reversed_num * 10 + digit
        n //= 10                # Remove the last digit
    return reversed_num

# Call the function
num = int(input("Enter a number: "))
reversed_result = reverse_number(num)
print("Reversed number:", reversed_result)

"""
OR 
def reverse_number(n):
    return int(str(n)[::-1])  # Convert to string, reverse with slicing, back to int

# Call the function
num = int(input("Enter a number: "))
reversed_result = reverse_number(num)
print("Reversed number:", reversed_result)
"""