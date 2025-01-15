# Write a program to check whether a number is positive, negative, or zero.
num = float(input("Please enter a number: "))

if num < 0:
    print(f"{num} is negative.")
elif num == 0:
    print(f"{num} is zero.")
else:
    print(f"{num} is positive.")

