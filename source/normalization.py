import string
import math

def max_min(datas):
    lenX = len(datas)
    lenY = len(datas[0])

    for i in range(lenY-1):
        nowmax = datas[0][i]
        nowmin = nowmax
        for j in range(lenX):
            xx = datas[j][i]
            if xx > nowmax:
                nowmax = xx
            if xx < nowmin:
                nowmin = xx

        for j in range(lenX):
            xx = datas[j][i]
            if nowmax > nowmin:
                datas[j][i] = (xx - nowmin)/(nowmax - nowmin)
            else:
                datas[j][i] = 1
                print i

    return datas

def z_score(datas):
    lenX = len(datas)
    lenY = len(datas[0])

    for i in range(lenY-1):
        u = 0.0
        for j in range(lenX):
            xx = datas[j][i]
            u += xx

        u = float(u)/float(lenX)
        o = 0.0
        for j in range(lenX):
            xx = datas[j][i]
            o += (u-xx)*(u-xx)

        o = math.sqrt(float(o)/float(lenX))

        for j in range(lenX):
            xx = datas[j][i]
            datas[j][i] = (xx-u)/o

    return datas
