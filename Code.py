# Function to add 5 integers and calculate their average
def add_and_average(a, b, c, d, e):
    total = a + b + c + d + e
    average = total / 5
    return total, average

# Example usage
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))
num4 = int(input("Enter the fourth integer: "))
num5 = int(input("Enter the fifth integer: "))

# Calculate the sum and average
total, average = add_and_average(num1, num2, num3, num4, num5)

# Display the results
print(f"The sum of the five integers is: {total}")
print(f"The average of the five integers is: {average}")
