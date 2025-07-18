# Print a pyramid of stars with 10 rows

for row in range(1, 11):  # Rows 1 through 10
    # Print leading spaces to right-align the stars
    print("  " * (10 - row), end="")

    # Print stars for the current row
    print("* " * row)

