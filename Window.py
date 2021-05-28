import turtle
from Models import *
class Window:
    def __init__(self):
        self.salto = 20
        self.origen = -100
        self.p= None
    
    def show(self):
        window = turtle.Screen()
        window.bgcolor("black")
        self.p = turtle.Turtle()
        self.p.pencolor('#ff05ea')
        self.p.pu()
        self.p.goto(self.origen,self.origen)
        self.p.pd()
        self.p.speed(0)

    def _dibujar_pixeles(self,x,y):
        self.p.pu()
        self.p.goto(x,y)
        self.p.pd()
        for i in range(4):
            self.p.forward(self.salto)
            self.p.right(90)
    
    def callpx(self,lista_x,lista_y):
        for i in range(len(lista_x)):
            x = lista_x[i] * self.salto + self.origen
            y = lista_y[i]*self.salto+self.origen
            self._dibujar_pixeles(x,y)
    
    
    
    
    # callpx(lista_x,lista_y)