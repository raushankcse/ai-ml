str = input("enter string: ")
strrev=""
for i in range(len(str),0,-1):
    strrev = strrev+str[i-1]

if(str.lower() == strrev.lower()):
    print("palindrome")
else:
    print("not palindrome")