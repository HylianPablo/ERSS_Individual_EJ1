with open("datos.txt","r") as f:
    x = f.readlines()
for i in range(len(x)):
    print(x[i])
