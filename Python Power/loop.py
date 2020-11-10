nome = 'Patrícia'

print(nome, len(nome))

'''
i = 0
while i < len(nome):
    print(nome[i])
    i += 1
'''

'''
for i in range(len(nome)):
    print(nome[i])
'''
'''
for i in nome:
    print(i)
'''
'''
for i, c in enumerate(nome):
    print(i, c) # index, character
'''
'''
for i, c in enumerate(nome):
    if c == 'a':
        continue
    print(i, c) 
'''
for i, c in enumerate(nome):
    if c == 'a':
        break
    print(i, c) 