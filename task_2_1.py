a = 15 * 3
b = 15 / 3
c = 15 // 2
d = 15 ** 2
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(b.is_integer())

# <class 'int'>
# <class 'float'>
# <class 'int'>
# <class 'int'>
# Единственное, что смущает: в методичке написано, что // дает только целые числа, но на практике получается,
# что если делить на дробное число, то int меняется на float
# подсказками не пользовалась :)

# https://github.com/Solmyrr/Voronova_Darya_Python/pull/1