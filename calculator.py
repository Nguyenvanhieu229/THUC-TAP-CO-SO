import math
def khoangCach(a, b, c, d):
    return math.sqrt((c-a)**2 + (d-b)**2)

def find(a, b, c):
    minx, miny = b.x, b.y
    for i in c:
        if khoangCach(a.x, a.y, i.x, i.y) < khoangCach(a.x, a.y, minx, miny):
            minx = i.x
            miny = i.y
    return (minx, miny)

def checkInsideEclip(x0, y0, x, y, a, b):

    kc = ((x-x0)**2)/(a**2) + ((y-y0)**2)/(b**2)
    if kc <= 1:
        return True
    return False



