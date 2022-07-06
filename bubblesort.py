#this is a test file to understand how git work

lst = [-1,-4,2,1,-5,4,6,3]

print('list befor sort',lst)
print("length of list",len(lst))
print("length of list with one short",len(lst) - 1)


#bubble sort
def sort(lst):
    for i in range(len(lst)-1,0,-1): #6 -1
        for j in range(i):
            if lst[j]>lst[j+1]:
                temp = lst[j]
                lst[j]=lst[j+1]
                lst[j+1]=temp
    return lst

#reverse bubble sort               
def rsort(lst):
    for i in range(len(lst)-1,0,-1):
        for j in range(i):
            if lst[j]<lst[j+1]:
                temp = lst[j]
                lst[j]=lst[j+1]
                lst[j+1]=temp
    return lst


list1 = [4,3,2,1]              
print(sort(lst))
print(rsort(lst))
