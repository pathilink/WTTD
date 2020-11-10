# row = 'Patrícia', 'São Paulo', 23.5, 46.6

# def f(t):
#     '''
#     nome = t[0]
#     cidade = t[1]
#     lat = t[2]
#     lon = t[3]
#     print(nome, cidade, lat, lon)
#     '''
#     '''
#     nome, cidade, lat, lon = t[0], t[1], t[2], t[3]
#     print(nome, cidade, lat, lon)
#     '''
#     '''
#     nome, cidade, lat, lon = t
#     print(nome, cidade, lat, lon)
#     '''
#     '''
#     nome, cidade = t[0:2]
#     print(nome, cidade)
#     '''
#     '''
#     nome, lon = t[0], t[-1]
#     print(nome, lon)
#     '''
#     '''
#     nome, _, _, lon = t
#     print(nome, lon, _)
#     '''
#     nome, *_, lon = t
#     print(nome, lon, _)

# if __name__ == '__main__':
#     f(row)

table = (('Patrícia', 'São Paulo', 23.5, 46.6),
        ('Loro', 'São Paulo', 23.5, 46.6))
'''
for row in table:
    nome, cidade, lat, lon = row
    print(nome, cidade, lat, lon)
'''
for nome, *_, lon in table:
    print(nome, lon, *_)
