def even(num):
    for i in range(1,num+1):
        if i%2==0:
            list1.add(i)
    
        
num=int(input("Enter number for the even numbers :-"))
list1=set({})

even(num)
print(list1)           


