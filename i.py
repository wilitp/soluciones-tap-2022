def datos():
    bits = input()
    bits = bits.split(" ")
    bits = list(map(lambda x : int(x), bits))

    a = True
    for b in bits:
        if b == 9:
            a = False
            break
    if a:
        print("S")
    else:
        print("F")

 
            

datos() 