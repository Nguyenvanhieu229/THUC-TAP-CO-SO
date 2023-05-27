import math
def khoangCach(a, b, c, d):
    return math.sqrt((c-a)**2 + (d-b)**2)

def find(goc, d1, d2, d3 = None):
    minx, miny = (d1.x, d1.y) if d1.health > 0 else (10000,10000)
    for i in d2:
        if khoangCach(goc.x, goc.y, i.x, i.y) < khoangCach(goc.x, goc.y, minx, miny):
            minx = i.x
            miny = i.y
    if d3 and d3.health > 0:
        minx,miny = (d3.x,d3.y) if khoangCach(goc.x,goc.y,minx, miny) > khoangCach(goc.x, goc.y, d3.x, d3.y) else (minx,miny)
    return (minx, miny)

def checkInsideEclip(x0, y0, x, y, a, b):

    kc = ((x-x0)**2)/(a**2) + ((y-y0)**2)/(b**2)
    if kc <= 1:
        return True
    return False



