# Jogo de mágica em Python

## Passo a passo até a conclusão do código

Grupo composto por: [Flávia Juchen](https://github.com/flaviajuchen), [Katiana Hanisch](https://github.com/KatianaHanisch), [Iago Ferreira](https://github.com/iagoaparecido)

Link do código

[https://github.com/IagoAparecido/magica](https://github.com/IagoAparecido/magica)

Após a explicação por meio das cartas de baralho, que nos ajudou a entender a lógica por trás da mágica e também da explicação do Prof. Will de como seria o início do código, se tornou fácil iniciarmos o programa.

Com a criação das três primeiras listas, denominadas de “a”, ”b” e “c”, expomos elas na tela em colunas (coluna A, B e C) junto com a pergunta sobre qual coluna abrigava  a opção escolhida.

```python
a = ["A1","A2","A3","A4","A5","A6","A7"]
b = ["B1","B2","B3","B4","B5","B6","B7"]
c = ["C1","C2","C3","C4","C5","C6","C7"]

for i in range(0,7):
    print(a[i], b[i], c[i] )
seleciona = input("Selecione uma das opções e diga em qual coluna ele se encontra: ")
```

Com o usuário escolhendo entre as opções “A”, “B” ou “C”, o programa filtra e e diz qual o calculo necessário para prosseguir, guardando a informação em uma variável chamada ”lista”, essa “lista’ recebe a concatenação das três primeiras listas criadas, além de uma opção caso nenhuma das três seja selecionada.

```python
if seleciona == "a" or seleciona == "A":
    lista =  b + a + c
elif seleciona == "b" or seleciona == "B":
    lista =  a + b + c
elif seleciona == "c" or seleciona == "C":
    lista =  b + c + a
else:
    print("Opção Inválida")
```

Após isso, criamos outras três variáveis, denominadas “listaA”, “listaB” e “listaC”, que são arrays vazias.

```python
listaA = []
listaB = []
listaC = []
```

Com as variáveis de arrays vazios criadas, o próximo passo foi criarmos um for com o range de 7, onde em cada passagem do for, as variáveis “listaA”, “listaB” e “listaC” receberiam um valor, determinado por nós, da variável “lista”(variável contendo o valor das três varáveis iniciais).

```python
contador = 0
for i in range(7):
    listaA.append(lista[contador])
    contador +=1
    listaB.append(lista[contador])
    contador += 1
    listaC.append(lista[contador])
    contador += 1
```

Com cada lista recebendo seus valores, exibimos elas na tela em colunas e é perguntado novamente para o usuário em qual coluna está a opção por ele escolhida.

```python
for i in range(7):
    print(listaA[i], listaB[i], listaC[i])
    
seleciona2 = input("Selecione a coluna que está sua opção: ")
```

O usuário indica qual a coluna, “A”, ”B” ou “C”, o processo acima se repete, com a coluna selecionada a concatenação é feita novamente e as variáveis “listaA”, “listaB” e “listaC” são transformadas novamente em arrays vazias para prosseguir ao próximo for.

Após a primeira escolha, esse processo se repete três vezes, onde na terceira vez é exibida a opção escolhida pelo usuário.

```python
print("A opção escolhida foi: "+lista[10])
```

No fim, a opção escolhida pelo usuário estará sempre na 11° posição da ultima lista criada.
