# first non repeating character


def first_non_repeating(str):
    char_count = {}
    for char in str:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char]=1
    
    for char in range(len(str)):

        if char_count[str[char]]==1:
            return char
    
    return -1




print(first_non_repeating("raushan"))
