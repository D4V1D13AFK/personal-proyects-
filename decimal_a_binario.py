def binario(num):
    lista = [] 
    while num != 0:
        modulo = num%2
        cociente = num//2
        lista.append(modulo)
        num = cociente
    lista = lista[::-1]
    for i in lista:
        print(i,end="")
    
        

num = int(input("introduce un número base décimal: "))
binario(num)

        
    
    
    

    




    