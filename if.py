nome = 'Patrícia'

for c in nome:
    #if c == 'a' or c == 'í' or c == 'i':
    #if c in('a', 'í', 'i'):
    if c in 'aíi':
        print(c.upper())
    elif c == 'c':
        print('@')
    else:
        print(c)
    