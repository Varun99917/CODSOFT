num1 = int(input("Enter first number = "))
num2 = int(input("Enter second number = "))
print("choices are = ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
a = int(input("choose froom the above choices = "))
if a==1:
    print("your sum is = ",num1 + num2)
elif a==2:
    print("your subtraction is = ", num1 - num2)
elif a==3:
    print("your product is = ", num1 * num2)
elif a==4:
    if num2 != 0:
        result = num1/num2
        print("your division is  = ",result)
    else:
        print("your denominator cannot be zero")
else:
    print("choose from 1 to 4 only")
