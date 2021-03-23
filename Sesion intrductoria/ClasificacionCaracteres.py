vocales = {'A', 'E', 'I', 'O', 'U'}
n = input()
if n.isupper():
    print('mayuscula')
else:
    print('minuscula')
if n.upper() in vocales:
    print('vocal')
else:
    print('consonante')