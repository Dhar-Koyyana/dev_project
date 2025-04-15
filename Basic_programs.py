#program 1

print("Hello world")

a = 4
print(a)

#program 2 - Basic arithmetic operations
a = 1
b = 3
print("addition", a+b)
print(a - b)
print(a*b)
print(a/b)
print(a==b)


# program 3 - Finding the largest no of three numbers
a = 3
b = 6
c = 8
if a>=b and c<a:
   largest = a
elif b<=a and b<=c:
    largest = b
else:
    largest = c


    print("the largest number is:", largest)


# program 3 - positive or negative or zero

# num = int(input("enter a number:",))
#
# if num>0:
#     print ("number is positive")
# elif num<0:
#     print("number is negative")
# else:
#     print("zero")

num = float(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
