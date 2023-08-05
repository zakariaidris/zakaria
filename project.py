# Ask the user for the length and width of the rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate the area of the rectangle
area = length * width

# Display the area of the rectangle to the user
print("The area of the rectangle is:", area)

# Write the input values and the calculated area to a file
with open("rectanglearea.txt", "w") as file:
    file.write("Length: " + str(length) + "\n")
    file.write("Width: " + str(width) + "\n")
    file.write("Area: " + str(area) + "\n")
    file.write("\n")

# Ask the user if they want to calculate the area of another rectangle
while True:
    response = input("Do you want to calculate the area of another rectangle? (yes/no):")
    if response == "no":
        break
    elif response == "yes":
       length = float(input("Enter the length of the rectangle: "))
       width = float(input("Enter the width of the rectangle: "))

       area = length * width
       print("The area of the rectangle is:", area)
       break

