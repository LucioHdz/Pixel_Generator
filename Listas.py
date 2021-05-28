class Puntos:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def to_list(self):
        return[self._x, self._y]

    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y

    def dda_algrithm(self,point):
        x = self.get_x()
        y = self.get_y()
        x2 = point.get_x()
        y2 = point.get_y()
        dx = abs(x2-x)
        dy = abs(y2-y)
        steps = 0
        if dx > dy:
            steps = dx
        else:
            steps = dy
    
        increment_x = dx / steps
        increment_y = dy / steps
    
        p1 = x
        p3 = y
        x_vars = [p1]
        y_vars = [p3]
        for i in range(steps):
            p1 += increment_x
            n = round(p1)
            x_vars.append(n)
    
            p3 += increment_y
            n = round(p3)
            y_vars.append(n)
        return x_vars, y_vars


    def bresenham_algrithm(self,point):
        x = self.get_x()
        y = self.get_y()
        x2 = point.get_x()
        y2 = point.get_y()
        dx = abs(x2 - x)
        dy = abs(y2 - y)
        p = 2 * dy - dx
        x_vars = []
        y_vars = []
        while x <= x2:
            x_vars.append(x)
            y_vars.append(y)
            x += 1
            if p < 0:
                p = p + 2 * dy
            else:
                p = p + (2 * dy) - (2 * dx)
                y += 1
        return x_vars, y_vars


def cuadrilateros(origen_x,origen_y,x,y):
    point1 = Puntos(origen_x,origen_y)
    point2 = Puntos(origen_x,y)
    point3 = Puntos(x,origen_y)
    point4 = Puntos(x,y)
    return [point1,point2,point3,point4]

def triangulo_equilatero(origen_x,origen_y,base):
    point1 = Puntos(origen_x,origen_y)
    point2 = Puntos(origen_x,base)
    y = origen_y/2
    b = y
    c = origen_x
    x = (origen_x**2) - (origen_y**2)
    x = x**2
    x = int(x)
    point3 = Puntos(x,y)
    return [point1,point2,point3]

def triangulo_rectangulo(origen_x,origen_y,base,altura):
    point1 = Puntos(origen_x,origen_y)
    point2 = Puntos(origen_x,base)
    point3 = Puntos(base,altura)
    return [point1,point2,point3]

    #         p3
    #        /|
    #       / |
    #      /  |
    #     /___|
    #   p1    p2