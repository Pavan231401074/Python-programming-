

def remove_chars(s1, s2):

    return ''.join([char for char in s1 if char not in s2])

s1=input()

s2=input()

result = remove_chars(s1, s2)

print(result)
