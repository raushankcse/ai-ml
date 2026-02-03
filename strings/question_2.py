# convert lower case to upper case



def upper_case(str):
    s=""
    for i in str[:]:
        if 'a' <= i <= 'z': 
            s+= chr(ord(i)-32)
    print(s)

upper_case("hello")