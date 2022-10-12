from bisect import bisect_left

N = int(input())
globos = list(map(int, input().split(" ")))
novisit = set(list(range(0, N)))

sum = 0 # solucion

while(True):
    try:
        i = min(novisit)
    except ValueError:
        break # se termino el problema
    h = globos[i]
    sum += 1
    while(i < N): # Actualizamos el problema siguiendo la cadena
        if(globos[i] == h):
            novisit.remove(i)
        i = bisect_left(novisit, i)


print(sum)
