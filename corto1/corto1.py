numero= 770 #Carnet 201602770
def collatz(num):
    for i in range(2,10):
        lista = []
        while i != 1 and i != 0:
            if i % 2 == 0:
                print("%d," % (i), end = "")
                i = i / 2
            else:
                print("%d," % (i), end = "")
                i = (i * 3) + 1
            if i == 1:
                print("1")
    return 

collatz(numero)