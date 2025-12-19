mydi={"karan":98,"nikk":99,"Arya":100}

name=input("enter name:-")
marks=input("enter marks:-")

if name in mydi:
    mydi[name]=marks
    print("marks updated sucessfully")
else:
    print("student not found")
print(mydi)