import RC4

#Soal : Enkripsi NIM dengan kunci sebanyak 4 dengan RC4

#Deklarasi sebuah variabel
S = [1,3,0,1,1,7,4,0,5,5]
K = [3,4,5,1]
a = [11,12,13]

#Function Swap
def swap(S, i, j):
    temp = S[i]
    S[i] = S[j]
    S[j] = temp 
    return S

#Random the Key
for i in range(4):
    K[i] = K[i%4]
j = 0

#Random the S
for i in range(10):
    j = ((j + S[i] + K[i%4]) % 4)
    swap(S, i, j)
print("S Aksen : ", S)

i = 0
j = 0

#Random the KeyStream
for i in range(4):
    i = ((i+1) % 4)
    j = ((j + S[i]) % 4)
    swap(S, i, j)
    t = ((S[i] + S[j]) % 4)
    KeyStreamByte = S[t]

    #proses XOR
    
print("Keystream : ",KeyStreamByte)