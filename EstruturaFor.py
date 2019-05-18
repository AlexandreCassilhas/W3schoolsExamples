fruits = ["apple", "banana", "grapes", "orange", "cherry"]
for x in fruits:
    print(x)

for x in "banana":
    print(x)

print ('')
for x in fruits:
    print(x)
    if x == "grapes":
        break

print('')
for x in fruits:
    if x == "banana":
        continue # exclui a banana do resultado
    print(x)
# Imprime de 0 a 9
print('')
for x in range(10):
    print (x)

# Imprime um range específico (entre 1 e 10)
print ('')
for z in range (1,11):
    print (z)

# Imprime de 5 em 5 (entre 0 e 25)
print ("")
for b in range (0,26,5):
    print (b)

# Imprimir uma mensagem ao final do loop
print ("")
for c in range(5):
    print (c)
else:
    print ("Fim de papo")

# Loops aninhados
print ("")
keys = ["1", "2", "3", "4", "5"]
valores = ["Land Rover", "Freelander 2", "branca", "SUV 4x4"]
for x in keys:
    for y in valores:
        print (x,y)