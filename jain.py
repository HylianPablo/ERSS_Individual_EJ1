import numpy as np

def jain(x):
    n = len(x)
    k = np.sum(x)**2
    m = np.square(x)
    l = np.sum(m)
    j = k/(n*l)
    return j

with open("usuariosLOCAL.csv","r") as f:
    array=[]
    for line in f:
        array.append([float(x) for x in line.split()])
resultado = jain(array)
print("Coeficiente de Jain: "+str(resultado))
