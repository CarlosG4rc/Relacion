def relacion(a,b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0
a = input ("Escribe el valor de a ")
b = input ("Escribe el valor de b ")
a = int (a)
b = int (b)
print( relacion(a,b))