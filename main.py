stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()

# Type your code below
a = stdform.find("x")
b = stdform.find("^")
text = stdform[:a] + "E" + stdform[b+1:]
print("This number in E notation is {}.".format(text))


