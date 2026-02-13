
while True:
    try:
        n=int(input("Enter total number of numbers: "))
        break
    except:
        print("Enter integer")

dict={
    "EVEN":[],
    "ODD":[],

}

for i in range(n):
    num=input("Enter number: ")
    if (int(num)%2)==0:
        dict["EVEN"].append(num)
    else:
        dict["EVEN"].append(num)

print("ODD: ", end="")
print(dict["EVEN"])
print("EVEN: ", end="")
print(dict["ODD"])

