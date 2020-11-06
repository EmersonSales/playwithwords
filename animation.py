def onda(frase):
    for i in range(20):
        print(e*i,frase,sep='')
    for i in range(20,-1,-1):
        print(e*i,frase,sep='')

def separar(frase):
    marcador = len(frase)-1
    for k in range(len(frase)):
        i = 0
        for j in range(4):
            
            for letra in range(len(frase)):
                
                if(letra == marcador):
                    print(e*i,frase[letra],sep='',end='')
                    i += 1
                elif(letra > marcador):
                    print(e*4,frase[letra],sep='',end='')
                else:
                    print(frase[letra],sep='',end='')
            print()
        marcador -= 1
def unir_dir(frase):
    frase2 = []
    cont_frasefim = 0
    check_cont_fim = 0
    cont = 0
    for letra in frase:
        frase2.append(' ')
        frase2.append(' ')
        frase2.append(' ')
        frase2.append(' ')
        frase2.append(letra)
        if(letra != ' '):
            cont_frasefim += 1
        cont += 4
    for k in range(cont):
        
        for i in range(len(frase2)):
            print(frase2[i],sep='',end='')
        print()
        if(check_cont_fim == cont_frasefim):
            break
        check_cont_fim = 0
        
        m = len(frase2)-1
        
        while(frase2[m] != ' '):
            m -= 1
            if(frase2[m] == ' '):
                del(frase2[m])
                frase2.insert(0,' ')
            check_cont_fim += 1
        
def esquerda(frase):
    frase2 = []
    cont = 0
    for letra in frase:
        cont += 4
    for i in range(5):
        print(e*cont,frase,sep='')    
    return(cont)
def let_meio(frase,cont):
    metade = int(len(frase)/2)
    
    j = 9
    k = 11
    for i in range(6):
        print(e*(cont-10),frase[0:metade-1],e*j,frase[metade-1],e*k,frase[metade:],sep='')
        j -= 1
        k += 1
    for i in range(6):
        j += 1
        k -= 1
        print(e*(cont-10),frase[0:metade-1],e*j,frase[metade-1],e*k,frase[metade:],sep='')    
def dir_meio(frase):
    metade = int(len(frase)/2)
    cont = esquerda(frase)
    for i in range(10):
        print(e*(cont-i),frase[0:metade-1],e*i,frase[metade-1],e*i,frase[metade:],sep='')
   
    let_meio(frase,cont)
    let_meio(frase,cont)
    for i in range(10,-1,-1):
        print(e*(cont-i),frase[0:metade-1],e*i,frase[metade-1],e*i,frase[metade:],sep='')

def dir_esq(frase):
    cont = esquerda(frase)
    for i in range(cont):
        print(e*(cont-i),frase,sep='')
     
def separa_uma_letra(frase):
    ini = ''
    for k in range(len(frase)):
        tam_ini = len(ini)    
        for i in range(5):
            print(ini,e*i,frase[tam_ini:],sep='')
        for i in range(5,-1,-1):
            print(ini,e*i,frase[tam_ini:],sep='')
        ini += frase[tam_ini]

def caminha_uma_letra(frase):
    ini = ''
    limite = 10
    for i in range(limite):
        print(ini,e*i,frase,sep='')    
    for k in range(len(frase)):
        tam_ini = len(ini)    
        j = 0
        for i in range(limite,-1,-1):
            print(ini,e*i,frase[tam_ini],e*j,frase[tam_ini+1:],sep='')
            j += 1
        ini += frase[tam_ini]

def deslizar(frase):
    acum = ''
    print(frase)
    for i in range(1,len(frase)+1):
        acum = frase[-i] + acum
        print(acum + frase[:-i])
  
        
      
frase = input('Insira Frase')

e = ' '

for i in range(10):
    print(frase)

onda(frase)
onda(frase)
separar(frase)
unir_dir(frase)
esquerda(frase)
dir_meio(frase)
dir_esq(frase)
caminha_uma_letra(frase)
separa_uma_letra(frase)

deslizar(frase)
deslizar(frase)