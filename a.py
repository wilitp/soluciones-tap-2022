def datos():
    n = int(input())
    line = input()

    sum = 0
    loc = 0
    for i in range(0, n):
        if(line[i] == "a"):
            loc += 1
        else:
            if(loc > 1):
                sum += loc
            loc = 0
    if(loc > 1):
        sum += loc
    return sum

print(datos())
