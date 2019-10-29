larg = int(input("digite a largura:"))
alt = int(input("digite a altura:"))
coluna = 0
altura = 0


while alt > altura:
    altura = altura + 1
    while larg > coluna + 1:
        if coluna == 0 or altura == 1 or altura == alt:
            print ("#", end = "")
            coluna = coluna + 1
        else:
            print (" ", end = "")
            coluna = coluna + 1
    print ("#", end = "") 
    coluna  =  0
    print()

    