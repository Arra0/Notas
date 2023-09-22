#suma cualquier tipo de numero ya sea flotantes o enteros 
def suma (a:int|float, b:int|float) -> int|float:
    return a + b

if __name__ == '__main__':
    res = suma(3.4, 5.6)
    print (res)