mylist=[1,2,3,4,9,6,7,8,9]

even=0
odd=0
for i in mylist:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1

print("count of even number is ",even)
print("count of odd number is ",odd)