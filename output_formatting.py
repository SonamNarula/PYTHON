# using format()

amount = 150.75
print("Amount: ${:.2f}".format(amount))

# using sep and end parameters

# end Parameter with '@'
print("Python", end="@")
print("GeeksforGeeks")

# Seprating with Comma
print("G", "F", "G", sep="")

# for formatting a date
print("09", "12", "2016", sep="-")

# another example
print("pratik", "geeksforgeeks", sep="@")

# using f-string
name = "Sonam Narula"
age = 19
print(f"Hello, My name is {name} and I'm {age} years old.")

# Using % Operator
num = int(input("Enter a value: "))
add = num + 5
print("The sum is %d" % add)
