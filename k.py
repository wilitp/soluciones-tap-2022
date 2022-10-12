def datos():
    nmk = input()
    nmk = nmk.split(" ")
    nmk = list(map(int, nmk))
    [N, M, K] = nmk
    xds = []
    while(True):
        try:
            xd = input()
            xd = xd.split(" ")
            xd = list(map(lambda x : int(x), xd))
            xds.append(xd)
        except EOFError:
            break
    
    return (N, M, K, xds)

# def salto(piedra, e, K, N, saltos):
#     if(piedra > N):
#         return 0
#     elif(e > K):
#         return 0
#     elif(piedra == N):
#         return 1
#     else:
#         acc = 0
#         for saltox in saltos:
#             acc += salto(piedra + saltox[0], e + saltox[1], K, N, saltos)
#         return acc

(N, M, K, saltos) = datos()
tabla = []

try:
    for n in range(0, N):
        aux = []
        for ener in range(0, K + 1):
            aux.append(0)
        tabla.append(aux)


    for ener in range(0, K+1):
        tabla[N-1][ener] = 1

    for piedra in range(N-1, -1, -1):
        for ener in range(K, -1, -1):
            acc = 0
            for salto in saltos: 
                if ((ener + salto[1]) <= K) and ((piedra + salto[0]) <= N):
                    acc += tabla[piedra + salto[0] - 1][ener + salto[1]]
            tabla[piedra-1][ener] = acc
except:
    tabla[0][0] = 1

print(int(tabla[0][0] % 10**9))
