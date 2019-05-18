a = 30
b = 40
if a > b:
    print ("a é maior que b")
elif a == b:
    print ("a é igual a b")
else:
    print ("b é maior que a")

x = "boi"
y = "camarão"
if len(x) > len(y):
    print (x)
elif len(x) < len(y):
    print (y)
else:
    print (x,y)

# Short hand if...else
print (" ")
print (x) if len(x) > len(y) else print (y) if len (x) < len (y) else print (x,y)
