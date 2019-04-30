import time
bottle = ' bottles of beer on the wall'
take = '.\nTake one down and pass it around,'
for n in reversed(range(100)):
    nBottle = str(n) + bottle
    if n == 1:
        nBottle = nBottle.replace('es','e')
        time.sleep(1)
    if n == 0:
        nBottle = 'no more' + bottle
        take = '.\nGo to the store and buy some more, 99' + bottle + '.'
        time.sleep(1)
    if n != 99:
        print(nBottle + '.\n')
        print(nBottle.capitalize() + ', ' + nBottle[:-12] + take,)
        time.sleep(1)