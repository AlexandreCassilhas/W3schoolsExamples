def my_function ():
    print ("Alô mundo by Function")
my_function()

def recebe_param (nome, idade):
    print ("Nome: ", nome)
    print ("Idade:", idade)
recebe_param("Alexandre", 45)
recebe_param("Jacqueline", 44)
recebe_param("Adriano", 51)

# Função com parâmetro Default
print("")
def recebe_param2 (nome, idade=45):
    print("Nome: ", nome)
    print("Idade:", idade)
recebe_param2("Alexandre")
recebe_param2("Jacqueline", 44)
recebe_param2("Adriano", 51)

# Passando uma sequência de parâmetros
def processa_comida (food)