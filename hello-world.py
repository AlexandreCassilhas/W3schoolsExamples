print ("Hello World!")

if 5 > 2:
    print ("Five is greater than two")

a = "   Hello, World"
x = 5
y = "John"
b = int(float("3.2"))
z = int(12.5)
w = 3+5j
print (x)
print (y)
print ("Meu nome é " + y)
print (x + z)
# Retornando o tipo da variável
print (type(x))
print (type(y))
print (type(z))
print (type(w))
print (type(b))
print (x/b)
# A string sendo tratada como array
print (a[0:5] + a[5:8] + a[8:12])
a = (a.strip())
print (a[0:5] + a[5:8] + a[8:12])
# Outras Funções
print (len(a))
print (a.upper())
print (a.lower())
print (a.replace("Hello", "Alô"))
# Input em linha de Comando
print ("Entre com seu nome:")
x = input()
print ("Hello, ", x)