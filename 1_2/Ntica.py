mysum = 0
ntica = (1,3,5,7,13,12,10)

minimum = ntica[0]
maximum = ntica[0]
pocet_prvkov = len(ntica)

prvy = ntica[0]

for i in ntica:
    if i < minimum:
        minimum = i
    if i > maximum:
        maximum = i
    
    posledny = i
    

print(f"Minimum: {minimum}, Maximum: {maximum}, pocet prvkov: {pocet_prvkov}, 1. clen: {prvy}, posledny: {posledny}.")


    



