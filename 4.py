n=int(input("Enter total numbers: "))
list=[]


dict={
    "even":[],
    "odd":[]
}

for i in range(n):
    num=int(input())
    if (num%2==0):
        dict["even"].append(num)
    else:
        dict["odd"].append(num)


print("Even elements: ", end="")
print(dict["even"])
print("Odd elements: ", end="")
print(dict["odd"])