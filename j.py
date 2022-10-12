def sumaPts(cartas):
    acc = 0
    for carta in cartas:
        if(carta >= 11):
            acc += 10
        else:
            acc += carta 
    return acc

def ganaMaria(ptsJ, ptsM, maso):
    menor = 14
    for carta in maso:
        if(carta >= 11):
            if(10 + ptsM == 23):
                menor = min(menor, carta)
        else:
            if(carta + ptsM == 23):
                menor = min(menor, carta)
    return menor

def pierdeJuan(ptsJ, ptsM, maso):
    menor = 14
    for carta in maso:
        if(carta >= 11):
            if(10 + ptsM <= 23 and 10 + ptsJ > 23):
                menor = min(menor, carta)
        else:
            if(carta + ptsM <= 23 and carta + ptsJ > 23):
                menor = min(menor, carta)
    return menor


N = int(input())
juan = list(map(int, input().split(" ")))
maria = list(map(int, input().split(" ")))
pozo = list(map(int, input().split(" ")))

maso = []
for palo in range(0,4):
    for carta in range(1,14):
        maso.append(carta)
for carta in juan:
    maso.remove(carta)
for carta in maria:
    maso.remove(carta)
for carta in pozo:
    maso.remove(carta)

ptsJ = sumaPts(juan) + sumaPts(pozo)
ptsM = sumaPts(maria) + sumaPts(pozo)

carta = (min(pierdeJuan(ptsJ, ptsM, maso), ganaMaria(ptsJ, ptsM, maso)))
if(carta == 14):
    print(-1)
else:
   print(carta)