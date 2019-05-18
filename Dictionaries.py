thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}
print (thisdict)

x = thisdict["model"]
print(x)

# Acessando o valor de um elemento do dicionário
z = thisdict.get("brand")
print(z)

# Alterando o valor de um elemento do dicionário
thisdict["year"] = 2018
print (thisdict)

# Varrendo as chaves do dicionário
for x in thisdict:
    print(x)

# Varrendo os valores de cada elemento de um dicionário
print (" ")
for x in thisdict:
    print (thisdict[x])

print ("ou")
for x in thisdict.values():
    print (x)

# Varrendo as chaves e os respectivos valores
print(" ")
for x, y in thisdict.items():
    print (x, y)

# Verificando a existência de um valor no dicionário
if "Ford" in thisdict.values():
    print ("Ok. Existe")

# Verificando a existência de uma key no dicionário
if "model" in thisdict:
    print ("Ok. Model Existe")

# Adicionando novo item ao dicionário
thisdict["color"] = "red"
print (thisdict)

# Removendo um item do dicionário
thisdict.pop("color")
print(thisdict)
print("ou")
del thisdict["model"]
print(thisdict)

# Copiando um dicionário
print (" ")
novodicionario = thisdict.copy()
print(novodicionario)

# Esvaziando o conteúdo do dicionário
thisdict.clear()
print(thisdict)

# Construindo pelo método dict()
thisdict = dict(brand="Ford", model="Mustang", year=2019, color="red")
print (thisdict)
