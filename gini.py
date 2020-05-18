import numpy as np

def gini(x):
    mad = np.abs(np.subtract.outer(x,x)).mean()
    rmad = mad / np.mean(x)
    g = 0.5 * rmad
    return g

with open("usuariosLOCAL.csv","r") as f:
    array=([])
    for line in f:
        array.append([float(x) for x in line.split()])
resultado = gini(array)
print("Coeficiente de Gini: "+str(resultado))
