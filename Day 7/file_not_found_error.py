try:
    f=open("t.txt","r")
    print(f.read())
    f.close()

except FileNotFoundError:
    print("the file is not in the storage")