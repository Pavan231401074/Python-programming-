

a = input()

ext = a.split('@')[0]

dom = a.split('@')[1].split('.')[0]

userno = a.find('.')

user = a[userno+1:]

print(user)

print(dom, end='\n')

print(ext,end='\n')
