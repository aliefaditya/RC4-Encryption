#Soal : Enkripsi NIM dengan kunci sebanyak 4 dengan RC4

#Deklarasi sebuah variabel
S               = [1,3,0,1,1,7,4,0,5,5]
K               = [3,4,5,1]
ListKSB         = []


print()
print("ENCRYPTION PROCESS WITH RC4")
print("===========================")

#Function Swap
def swap(S, i, j):
    temp = S[i]
    S[i] = S[j]
    S[j] = temp 
    return S

print("S awal    : ", S)

#Random the Key
for i in range(4):
    K[i] = K[i%4]

j = 0

#Random the S
for i in range(0, len(S)):
    j = ((j + S[i] + K[i%4]) % 4)
    swap(S, i, j)
print("S Aksen   : ", S)

i = 0
j = 0

#Random the KeyStream
for i in range(10):
    i = ((i+1) % 4)
    j = ((j + S[i]) % 4)
    swap(S, i, j)
    t = ((S[i] + S[j]) % 4)
    KeyStreamByte = S[t]
    if(i <= 3):
         ListKSB.append(KeyStreamByte) #save the KeyStreamByte on each iteration in List for decryption  
   

    #Proses XOR antara setiap bit dengan keystream
for i in range(10):
    S[i] = S[i]^ListKSB[i%3]

print("List KSB  : ", ListKSB)
print("S Akhir   : ", S)
print()
print("DECRYPTION PROCESS WITH RC4")
print("===========================")

#Decryption Process

"""
    1. Jangan lupa niat sm do'a wkwk
    2. Use the same secret key as during the encryption phase
    3. XOR keystream with the encrypted text to generate the plaint text

    sama aja kaya gini cuy --> (A XOR B) XOR B = A
    dimana,
    A = Plain Text 
    B = KeyStream
"""

for i in range(10):
    #Proses XOR antara setiap bit dengan keystream
    S[i] = ((S[i]^ListKSB[i%3]))

print("S Aksen    : ",S)

