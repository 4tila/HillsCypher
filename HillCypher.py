from numpy import *
eg=matrix([[10,5,12],[3,14,21],[8,9,11]])
def cof(mat):
    n = len(mat)
    adjoint = list()
    for i in range(n):
        add = list()
        for j in range(n):
            cofij = mat
            cofij = delete(cofij, i, 0)
            cofij = delete(cofij,j,1)
            add.append((-1)**(i+j)*round(linalg.det(cofij)))
        adjoint.append(add)
    adjoint = array(adjoint)
    return adjoint.transpose()
modadjoint = array(cof(eg))%26
modajoint = modadjoint.astype(int)
inveg = 15*modajoint%26#15 is the multiplicative inverse of 7
                                #that is the determinant of eg
print eg
print inveg
alphabet = "a;b;c;d;e;f;g;h;i;j;k;l;m;n;o;p;q;r;s;t;u;v;w;x;y;z".split(";")
msg = "thatsmybulsh"
nums = [alphabet.index(elem) for elem in msg]
triples = list()
enc = list()
for i in range(len(nums)/3):
    triples.append(array(nums[3*i:3*i+3]))
for elem in triples:
    new = array(dot(eg, elem).tolist()[0])
    new = new%26
    new = new.astype(int)
    new = new.tolist()
    for elem in new:
        enc.append(alphabet[elem])
encrypted = ''.join(enc)
print encrypted
#starting decryption
decrypted = str()
for i in range(len(nums)/3):
    triple = encrypted[3*i:3*i+3]
    number = array([alphabet.index(elem) for elem in triple])
    dec = dot(inveg, number).astype(int)%26
    dec = dec.tolist()
    decrypted+=''.join([alphabet[j] for j in dec])
print decrypted
