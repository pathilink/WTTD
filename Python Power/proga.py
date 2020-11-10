print('Begin', __name__)

print('Define fA')
def fA():
    print('Dentro fA')

if __name__ == '__main__': # verifica se é entry point ou biblioteca
    print('Chama fA')
    fA()

print('End', __name__)