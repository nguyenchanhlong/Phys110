import math

def convert(xA, yA, q):

    xQ = 0
    yQ = 0
    ke = 9*(10**9)
    Q = q*(10**(-9))

    r = math.sqrt((xA-xQ)**2+(yA-yQ)**2)

    rx = (xA-xQ)/r
    ry =(yA-yQ)/r

    E0 = ke*Q/r**2
    Ex = E0*rx
    Ey = E0*ry
    
    return Ex, Ey

print(convert(1,1,1))