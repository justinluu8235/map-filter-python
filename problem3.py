retro_jordans = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

def under_13 (num):
    if num <= 13:
        return True
    else:
        return False

def bought (num):
    return 'Retro ' + str(num) + ' bought'

fav_jordans = list(filter(under_13, retro_jordans))
print('FAV JORDAN #s', list(fav_jordans))

jordans_bought = map(bought, fav_jordans)
print('JORDANS BOUGHT..', list(jordans_bought))


