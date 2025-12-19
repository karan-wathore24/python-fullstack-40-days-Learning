mylist=[1,2,3,4,4,2]
mylist2=[]
for i in mylist:
    if i not in mylist2:
        mylist2.append(i)


print(mylist2)