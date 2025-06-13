#ACTUALLY I didn't know how to initalize the linked list
#but i will convert those into list and do the below steps and append into the list 
print("Enter the no.of linked lists")
k = int(input())
p = []
print("Enter the data in linkedLists")
for i in range(0,k):
    p.append(list(map(int,input().split())))
result = []
for i in range(0,k):
    for j in range(0,len(p[i])):
        result.append(p[i][j])
result.sort()
for i in range(0,len(result)):
    if (i==len(result)-1):
        print(result[i])
    else:
        print(result[i],end="->")
    
