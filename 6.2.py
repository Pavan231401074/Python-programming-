import re

a=input()

all=re.findall('\d+',a)

all_w=re.findall('[a-z]',a)

b=''

for i,j in zip(all,all_w):

    b+=int(i)*j

print(b)
