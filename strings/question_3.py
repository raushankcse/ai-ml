


def lower_case(str):
    s = ""
    for i in str[:]:
        s+= chr(ord(i)+32)
    print(s)

lower_case("HEELLO")


