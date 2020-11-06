palavra = 'Rita'
#palavra = input()
tam = len(palavra)
lim = len(palavra)*2
matriz = []
for i in range(lim):
    matriz.append([palavra[0]]*lim) #Cria e preenche com primeira letra


for k in range(1,tam):
    for i in range(k,lim-k):
        for j in range(k,lim-k):
            matriz[i][j] = palavra[k]

for i in range(lim):
    for j in range(lim):
        print(matriz[i][j],end='')
    print()