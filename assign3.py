hello=input("Enter string: ")
array=[]
n=0
for i in hello:
    array.append(i)
    n+=1

print(array[-1], end="")
print(array[-2], end="")
for i in range(n-2):
    print(array[i], end="")
print("")
