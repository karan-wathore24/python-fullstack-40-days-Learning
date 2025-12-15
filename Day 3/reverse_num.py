num=128
rev=0
while num!=0:
    rim=num%10
    rev=(rev*10)+rim
    num=num//10
print(rev)