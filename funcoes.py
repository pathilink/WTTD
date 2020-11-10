'''
def f():
    return 42

print(f())
'''

'''
def f():
    pass

print(f()) # None
'''

'''
def f(a, b, c):
    print(a, b, c) 

f('A', 'B', 'C')       # positional parameters
f(a='A', c='C', b='B') # named parameters
'''

'''
def f(a, b, c='dC'): # default value
    print(a, b, c) 

f('A', 'B')
f(b='B', a='A')
'''

'''
def f(a, b, c='dC', *args): # undefined positional parameters
    print(a, b, c, args) 

f('A', 'B', 'C', 'D', 'E', 'F')
'''

'''
def f(a, b, c='dC', **kwargs): # indefinite number of named parameters
    print(a, b, c, kwargs) 

f(c='C', z='Z', a='A', f='F', b='B')
'''

'''
def f(a, b, c='dC', *args, **kwargs): 
    print(a, b, c, args, kwargs) 

f('A', 'B', 'C','D','E', z='Z', w='W') # positional, posicional in tuple args, named in dictionary kwargs
'''

'''
def f(a, b, c='dC', *args, x, y, **kwargs): 
    print(a, b, c, args, x, y, kwargs) 

f('A', 'B', 'C','D','E', x=1, y=2, z='Z', w='W') 
'''

'''
def f(a, b, c='dC', *args, x=42, y=51, **kwargs): 
    print(a, b, c, args, x, y, kwargs) 

f('A', 'B', 'C','D','E', z='Z', w='W') 
'''

'''
# Django
def filter(**lookups): # lookups is a dictionary in Django
    for k, v in lookups.items(): # k as key, v as value
        print(k.split('__'), v)

filter(name__startswith='Pat', age__lt=39, city__endswith='ulo')
'''

'''
def f(*args, **kwargs):
    print(args, kwargs)

f('A', 'B', 'C', z='Z', w='W')
'''

'''
def f(*args, **kwargs):
    print(args, kwargs)

t = 'A', 'B', 'C'
d = dict(z='Z', w='W')

print(t, d)
'''

'''
def f(*args, **kwargs):
    print(args, kwargs)

t = 'A', 'B', 'C'
d = dict(z='Z', w='W')

f(t, d) # args
'''

def f(*args, **kwargs):
    print(args, kwargs)

t = 'A', 'B', 'C'
d = dict(z='Z', w='W')

#f(t[0], t[1], t[2], z=d['z'], w=d['w']) # args, kwargs
f(*t, **d) # pythonic

