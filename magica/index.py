a = ["A1","A2","A3","A4","A5","A6","A7"]
b = ["B1","B2","B3","B4","B5","B6","B7"]
c = ["C1","C2","C3","C4","C5","C6","C7"]
lista = []
listaA= []
listaB= []
listaC= []

for i in range(7):
    print(a[i], b[i], c[i])

selecionado = input("Selecione alguma opção e diga se está na coluna a, b ou c: ")

if (selecionado == "a" or "A"):
        lista.append(b + a + c)
        lista = lista[0]

        for i in range(7):
            listaA.append([lista[0], lista[3],lista[6], lista[9],lista[12], lista[15],lista[18]])
            listaB.append([lista[1], lista[4],lista[7], lista[10],lista[13], lista[16],lista[19]])
            listaC.append([lista[2], lista[5],lista[8], lista[11],lista[14], lista[17],lista[20]])
        listaA = listaA[0]
        listaB = listaB[0]
        listaC = listaC[0]

        for i in range(7):
            print(listaA[i],listaB[i], listaC[i])
            
        selecionado = input("Selecione alguma opção e diga se está na coluna a, b ou c: ")

elif(selecionado == "b" or "B"):
        lista.append(a + b + c)
        for i in range(7):
            listaA.append([lista[0], lista[3],lista[6], lista[9],lista[12], lista[15],lista[18]])
            listaB.append([lista[1], lista[4],lista[7], lista[10],lista[13], lista[16],lista[19]])
            listaC.append([lista[2], lista[5],lista[8], lista[11],lista[14], lista[17],lista[20]])
        listaA = listaA[0]
        listaB = listaB[0]
        listaC = listaC[0]

        for i in range(7):
            print(listaA[i],listaB[i], listaC[i])

        selecionado = input("Selecione alguma opção e diga se está na coluna a, b ou c: ")

elif(selecionado == "c" or "C"):
        lista.append(a + c + b)

        for i in range(7):
            listaA.append([lista[0], lista[3],lista[6], lista[9],lista[12], lista[15],lista[18]])
            listaB.append([lista[1], lista[4],lista[7], lista[10],lista[13], lista[16],lista[19]])
            listaC.append([lista[2], lista[5],lista[8], lista[11],lista[14], lista[17],lista[20]])
        listaA = listaA[0]
        listaB = listaB[0]
        listaC = listaC[0]

        for i in range(7):
            print(listaA[i],listaB[i], listaC[i])

        selecionado = input("Selecione alguma opção e diga se está na coluna a, b ou c: ")

