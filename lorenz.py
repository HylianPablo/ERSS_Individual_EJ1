import numpy as np

def lorenz(x):
    mad = np.mean(np.absolute(x - np.mean(x)))
    l = mad/ (2 * np.mean(x))
    return l

with open("usuariosLOCAL.csv","r") as f:
    array=([])
    for line in f:
        array.append([float(x) for x in line.split()])
resultado = lorenz(array)
print("Diferencia de la curva de Lorenz: "+str(resultado))
