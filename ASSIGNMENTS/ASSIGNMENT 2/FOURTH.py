lst=[]
n=int(input("enter the number of element in list : "))
for i in range (n):
    element=int(input(f"enter number as the element in list {i+1} : "))
    lst.append(element)
a=int(input('''
    1. to find smallest value
    2. to find second largest value
    3. to find second smallest value  \n:'''))
if a==1:
     print(f"The smallest value is :{min(lst)}")
elif a==2:
    lst.sort()
    print(f"the second largest value is :{lst[-2]}")
elif a==3:
    lst.sort()
    print(f"the second smallest value is :{lst[2]}")





