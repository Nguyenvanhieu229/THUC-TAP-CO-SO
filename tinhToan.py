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


