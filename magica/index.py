a = ["A1","A2","A3","A4","A5","A6","A7"]
b = ["B1","B2","B3","B4","B5","B6","B7"]
c = ["C1","C2","C3","C4","C5","C6","C7"]

print("A  B  C")
for i in range(0,7):
    print(a[i], b[i], c[i] )
seleciona = input("Selecione uma das opções e diga em qual coluna ele se encontra: ")
print("#################################################################")

if seleciona == "a" or seleciona == "a":
    lista =  b + a + c
elif seleciona == "b" or seleciona == "B":
    lista =  a + b + c
elif seleciona == "c" or seleciona == "C":
    lista =  b + c + a
else:
    print("Opção Inválida")

listaA = []
listaB = []
listaC = []

for i in range(7):
    listaA.append([lista[0], lista[3],lista[6], lista[9],lista[12], lista[15],lista[18]])
    listaB.append([lista[1], lista[4],lista[7], lista[10],lista[13], lista[16],lista[19]])
    listaC.append([lista[2], lista[5],lista[8], lista[11],lista[14], lista[17],lista[20]])
listaA = listaA[0]
listaB = listaB[0]
listaC = listaC[0]

print("A  B  C")
for i in range(7):
    print(listaA[i], listaB[i], listaC[i])
    
seleciona2 = input("Selecione a coluna que está sua opção: ")
print("#################################################################")


if seleciona2 == "a" or seleciona2 == "a":
    lista =  listaB + listaA + listaC
elif seleciona2 == "b" or seleciona2 == "B":
    lista =  listaA + listaB + listaC
elif seleciona2 == "c" or seleciona2 == "C":
    lista =  listaB + listaC + listaA
else:
    print("Opção Inválida")

listaA = []
listaB = []
listaC = []

for i in range(7):
    listaA.append([lista[0], lista[3],lista[6], lista[9],lista[12], lista[15],lista[18]])
    listaB.append([lista[1], lista[4],lista[7], lista[10],lista[13], lista[16],lista[19]])
    listaC.append([lista[2], lista[5],lista[8], lista[11],lista[14], lista[17],lista[20]])
listaA = listaA[0]
listaB = listaB[0]
listaC = listaC[0]

print("A  B  C")
for i in range(7):
    print(listaA[i], listaB[i], listaC[i])

seleciona3 = input("Selecione a coluna que está sua opção: ")
print("#################################################################")

if seleciona3 == "a" or seleciona3 == "a":
    lista =  listaB + listaA + listaC
elif seleciona3 == "b" or seleciona3 == "B":
    lista =  listaA + listaB + listaC
elif seleciona3 == "c" or seleciona3 == "C":
    lista =  listaB + listaC + listaA
else:
    print("Opção Inválida")

listaA = []
listaB = []
listaC = []

for i in range(7):
    listaA.append([lista[0], lista[3],lista[6], lista[9],lista[12], lista[15],lista[18]])
    listaB.append([lista[1], lista[4],lista[7], lista[10],lista[13], lista[16],lista[19]])
    listaC.append([lista[2], lista[5],lista[8], lista[11],lista[14], lista[17],lista[20]])
listaA = listaA[0]
listaB = listaB[0]
listaC = listaC[0]

lista = listaA+listaB+listaC

print("A opção escolhida foi: "+lista[10])