import numpy as np

m=np.array([7,14,11,0])

def cifrado_julio_cesar(m,n):
    c=(m+3)%n
    return c

def descrifrado_julio_cesar(c,n):
    m=(c-3)%n
    return m

print("el cifrado de julio cesar es: ",cifrado_julio_cesar(m,26))
c=cifrado_julio_cesar(m,26)
print("el descifrado de julio césar: ",descrifrado_julio_cesar(c,26))