def prime(num):
    if num<=1:
        return False
    
    for i in range(2,num):
        if num %i==0:
            return False
        
    return True

num=int(input("enter number :- "))

if prime(num):
    print(num,"Is prime number")

else:
    print(num, "Is not prime number")
