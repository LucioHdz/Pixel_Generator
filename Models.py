

def dda_algrithm(x,y,x2,y2):
    """Algoritmo de trazos DDA

    Args:
        x (integer): posicion x coordenada 1
        y (integer): posicion y coordenada 1
        x2 (integer): posicion x coordenada 2
        y2 (integer): posicion y coordenada 2

    Returns:
        List(int): Listas x,y coordinadas
    """
    dx = abs(x2-x)
    dy = abs(y2-y)
    steps = 0
    if dx>dy:
        steps = dx
    else:
        steps = dy

    increment_x = dx / steps     
    increment_y = dy / steps

    p1 = x
    p2 = y
    x_vars=[p1]
    y_vars=[p2]
    for i in range(steps):
        if x2 < x:
            p1 -= increment_x
        else:
            p1 += increment_x
        n = round(p1)
        x_vars.append(n)
        if y2>y:
            p2 += increment_y
        else:
            p2 -= increment_y 
        n = round(p2)
        y_vars.append(n)
    return x_vars,y_vars


# ESTE ALGORITMO SE PUEDE DESCARGAR DESDE PIP 
#LINK DE PYPI https://pypi.org/project/bresenham/


def bresenham_algrithm(x0, y0, x1, y1):
    """Yield integer coordinates on the line from (x0, y0) to (x1, y1).

    Input coordinates should be integers.

    The result will contain both the start and the end point.
    """
    dx = x1 - x0
    dy = y1 - y0
    xvars = []
    yvars = []

    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0

    D = 2*dy - dx
    y = 0

    for x in range(dx + 1):
        xvars.append(x0 + x*xx + y*yx)
        yvars.append(y0 + x*xy + y*yy)
        if D >= 0:
            y += 1
            D -= 2*dx
        D += 2*dy
    return xvars,yvars


if __name__ == '__main__':
    lista = bresenham_algrithm(0,0,0,10)
    print(lista)