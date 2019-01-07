from sys import argv

a = input("input first:")
b = input("second")
c = input("third")

script, first, second, third = argv 
print(a, b, c)
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
