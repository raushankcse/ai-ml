str = "hello"
s=""
for i in str[:]:
    asc = ord(i)-32
    s+= chr(asc)
print(s)
