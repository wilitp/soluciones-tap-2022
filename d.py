from math import inf, sqrt
def datos():
    return list(map(int, input().split(" ")))


def dist(trg, act):
    (x, y) = trg
    (xact, yact) = trg

    return sqrt( (x-xact)**2 + (y-yact)**2)

def move(act, activ, trg, N):
    if act[0] == trg[0] and act[1] == trg[1]:
        return 0
    else:
        options = []
        for i in range(4):
            options.append(inf)
        for i in range(0, 4):
            if(i == 0):
                after = (act[0]/2, act[1]/2)
            if(i == 1):
                after = ((act[0] + 2**N)/2, act[1]/2)
            if(i == 2):
                after = ((act[0] + 2**N)/2, (act[1]+2**N)/2)
            if(i == 3):
                after = (act[0]/2, (act[1]+2**N)/2)
            if dist(after, trg) < dist(act, trg):
                    options[i] = move(after, activ+1, trg, N)
        return min(options)

(N, x, y) = datos()
print(move((2**N-1, 2**N-1), 0, (x,y), N))