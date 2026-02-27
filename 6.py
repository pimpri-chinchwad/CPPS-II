num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

def GCD(num1, num2, i):
    if (num1%i==0) and (num2%i==0):
        return i
    else:
        return GCD(num1, num2, i-1)

if num1>num2:
    print("GCD is: "+str(GCD(num1, num2, num2)))
else:
    print("GCD is: "+str(GCD(num1, num2, num1)))
    