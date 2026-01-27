print "Hola mundo"

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "¡Error! División entre cero."
    else:
        return x / y

x=input("Ingresa el valor de x")
y=input("Ingresa el valor de y")
result=add(x,y)
print(f"El resultado es: {result}")


