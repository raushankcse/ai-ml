str = input("enter any string: ")
s1 = "aeiouAEIOU"
v=0
for i in str:
    if i in s1:
        v+=1
print(f"total vowel in string: {v}")

