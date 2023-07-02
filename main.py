import string
print("Formatting the string")
str=input("Enter Your name : ")
print("I'm {}".format(str))
str = input("Enter your name: ")
print(f"I'm {str}")
# using format option in a simple string
print("{} Leave the Rest".format("Do Your best"))
# using format option for avalue stored in a variable
str = "Do Your best {} "
print(str.format("Leave The Rest"))
# formatting a string using a numeric constant
print("Hello, I am {} years old !".format(17))
print("Finding indexing")
str ="Always Try your best"
print(str.index("Try"))

print("----------")
print(str.index("your",11,15))
print("----------")
print("Rani".index("a"))
print("----------")
str1="Rani"
print(len(str1))
print("----------")
print(str.index("a", 1, 4))
print("Using swapcase() function")
str = "do your best ,  leave the rest "
print(str.swapcase())
print("Using relace() function ")
var="Raniaaaa"
print(var.replace("a","S",3))
