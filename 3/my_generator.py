def countdown():

    print('starting..')

    while True:
        yield num #return by ukoncil cyklus
        num -= 1


max_iter = 3000
i = 0

for val in countdown():
    print(val)
    i += 1
    if i > max_iter:
        break

