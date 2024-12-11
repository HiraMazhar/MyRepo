# Function to add 5 integers
def add_five_integers(a, b, c, d, e):
    return a + b + c + d + e

# Example usage
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))
num4 = int(input("Enter the fourth integer: "))
num5 = int(input("Enter the fifth integer: "))

# Calculate the sum
result = add_five_integers(num1, num2, num3, num4, num5)

# Display the result
print(f"The sum of the five integers is: {result}")
