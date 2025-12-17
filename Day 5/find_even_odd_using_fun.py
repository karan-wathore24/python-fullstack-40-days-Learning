def check(num):
    if num%2==0 and num!=0:
        print("The given number is even")
    elif num==0:
        print("the given number is Zero")
    else:
        print("The given number is odd")


num=int(input("Enter a number:- "))

check(num)
