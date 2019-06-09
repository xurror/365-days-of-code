def addComplex(z1, z2):
    return z1 + z2

def multComplex(z1, z2):
    return z1 * z2

def invertComplex(z):
    conjugate = z.conjugate()
    z = z * conjugate
    z = conjugate / z
    return z

def negateComplex(z):
    return (-1)*z