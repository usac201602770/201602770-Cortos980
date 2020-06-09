
#PABLO ALEJANDRO RIOS REYNOSO 
import os
numero= 770 #Carnet 201602770
def collatz(num):                                       #FUNCION PARA SECUENCIA DE COLLATZ DE 2 HASTA NUMERO
    for i in range(2,numero+1):                         #INICIA CICLO FOR DONDE I RECORRE DESDE 2 HASTA NUMERO+1
        while i != 1 and i != 0:                        #CICLO WHILE QUE SE EJECUTARA TANTAS VECES I NO SEA IGUAL A 1 Y 0 
            if i % 2 == 0:                              # SI I ES PAR SE DIVIDE
                print("%d," % (i), end = "")
                i = i / 2
            else:                                       #SI ES IMPAR SE I*3 +1 
                print("%d," % (i), end = "")        
                i = (i * 3) + 1
            if i == 1:                                  #SI ES IGUAL A 1 SOLO SE IMPRIME 
                print("1")
    return 

collatz(numero)
#file = open("collatz.txt, "w")                 #PRUEBA ESCRIBIR EN TXT
#file.write("Primera línea" + os.linesep)
#file.write("Segunda línea")
#file.close()