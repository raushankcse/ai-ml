str = input("enter a string: ")
l=0
for i in str:
    if i.islower():
        l+=1
print(f"count of small case in string: {l}")