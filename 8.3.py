s = input()

j = []

repeated = set()

for i in range(len(s) - 9):

    sequence = s[i:i+10]

    if sequence in j:

        repeated.add(sequence)

    else:

        j.append(sequence)

l=list(repeated)

l=list(reversed(l))

for i in l:

    print(i)
