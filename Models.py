

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


def bresenham_algrithm(x,y,x2,y2):
    """Algoritmo de trazos Bresenham

    Args:
        x (integer): posicion x coordenada 1
        y (integer): posicion y coordenada 1
        x2 (integer): posicion x coordenada 2
        y2 (integer): posicion y coordenada 2

    Returns:
        List(int): Listas x,y coordinadas
    """
    dx = abs(x2 -x)
    dy = abs(y2 -y)
    p = 2 * dy -dx
    x_vars=[]
    y_vars=[]
    while x <= x2:
        x_vars.append(x)
        y_vars.append(y)   
        x += 1
        if p<0:
            p = p + 2 * dy
        else:
            p = p + (2 * dy) - (2 * dx)
            y += 1
    return x_vars,y_vars


if __name__ == '__main__':
    lista = bresenham_algrithm(0,0,0,10)
    print(lista)