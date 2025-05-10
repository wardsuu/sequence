# ---------------------------------------------
# Program: Number Sequence with Input Validation
# Description:
# This program generates a sequence of numbers
# based on user input: starting value, stopping value,
# and incrementing value. It uses both a for loop
# and a while loop to display the sequence.
# ---------------------------------------------

# Get user input for the starting, stopping, and incrementing values
startValue = int (input("Enter starting value: "))
stopValue = int (input("Enter stopping value: "))
incrementValue = int (input("Enter incrementing value: "))

# Validate the inputs:
# - starting value must be less than stopping value
# - incrementing value must be greater than 0
while startValue >= stopValue or incrementValue <= 0:
    print("\nInvalid input")

    if startValue >= stopValue:
        print("\nStart value must be less than stop value")

    if incrementValue <=0:
        print("\nIncrement value must be greater than 0")

    # Ask again for valid input
    startValue = int(input("Enter starting value: "))
    stopValue = int(input("Enter stopping value: "))
    incrementValue = int(input("Enter incrementing value: "))

# Display the sequence using a for loop
print("\nUsing for loop: ")
for i in range(startValue, stopValue, incrementValue):
    print(i)

# Display the sequence using a while loop
print("\nUsing while loop: ")
i = startValue
while i < stopValue:
    print(i)
    i += incrementValue
