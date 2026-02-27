n=int(input("Enter total numbers: "))
list=[]

def max(list):
    max=list[0]
    for i in list:
        if i>max:
            max=i
    return max

def min(list):
    min=list[0]
    for i in list:
        if i<min:
            min=i
    return min

def mean(list, n):
    mean=0
    for i in list:
        mean+=i
    return mean/n

for i in range(n):
    num=int(input())
    list.append(num)

print("Mean: " + str(mean(list, n)))
print("Maximum: " + str(max(list)))
print("Minimum: "+ str(min(list)))

