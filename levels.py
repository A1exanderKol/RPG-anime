import math
def opt_epe(epesods):
    if epesods <=25:
        o=epesods*5
    elif epesods >25 and epesods <=50:
        o=epesods*4
    elif epesods >50 and epesods <=100:
        o=epesods*3
    elif epesods >100 and epesods <=500:
        o=epesods*2
    elif epesods >500 and epesods <=1000:
        o=epesods*1
    elif epesods >1000:
        o=int(math.floor(epesods/2))

    return o

def lev (e,l,exp):
    e=e+exp
    if l==15:
        return e, 15
    else:
        l=all_levels(e)
        return e,l

def all_levels(e):
    if 0>= e < 160:
        return 1
    elif e>=160 and e < 360: #200
        return 2
    elif e>=360 and e < 600:#240
        return 3
    elif e>=600 and e < 880:#280
        return 4
    elif e>=880 and  e < 1200:#320
        return 5
    elif e>=1200 and e <1580 :#380
        return 6
    elif e>=1580 and e < 2020:#440
        return 7
    elif e>=2020 and e < 2520:#500
        return 8
    elif e>=2520 and e < 3080:#560
        return 9
    elif e>=3080 and e < 3700:#620
        return 10
    elif e>=3700 and e < 4400:#700
        return 11
    elif e>=4400 and e < 5180:#780
        return 12
    elif e>=5180 and e < 6040:#860
        return 13
    elif e>=6040 and e < 6980:#940
        return 14
    elif e>=6980 and e < 8000:#1020
        return 15