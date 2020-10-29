print('Begin', __name__)
import proga # nome do módulo é o nome do arquivo pq não é entry point

print('Define fB')
def fB():
    print('Dentro fB')
    proga.fA()

print('Chama fB')
fB()

print('End', __name__)