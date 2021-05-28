from os import system,name
import turtle
from Window import Window
from Models import *


window = Window()
def menu():
    if name == "nt":
        system("cls")
    else:
        system("clear")
    print("""
        Ingresa una opcion a graficar
        1)cuadrado
        2)rectangulo
        3)Triangulo equilatero
        4)Triangulo rectangulo
        5)Poligono(N lados)
    """)
    options = int(input('   Option: '))
    
    if name == "nt":
        system("cls")
    else:
        system("clear")
    print("""
        Elige el algoritmo a realizar la imagen:

        1)DDA
        2)bresenham
    """)
    algorithm = int(input('   Option: '))

    return options,algorithm


def cuadrilateros(option,b,h):
    x1 =[0,0]
    x2 =[0,h-1]
    x3 =[b-1,0]
    x4 =[b-1,h-1]
    
    if option == 1:
        #dda
        lado1_x,lado1_y = dda_algrithm(x1[0],x1[1],x2[0],x2[1])
        lado2_x,lado2_y = dda_algrithm(x1[0],x1[1],x3[0],x3[1])
        lado3_x,lado3_y = dda_algrithm(x2[0],x2[1],x4[0],x4[1])
        lado4_x,lado4_y = dda_algrithm(x3[0],x3[1],x4[0],x4[1])

        return [lado1_x,lado1_y,lado2_x,lado2_y,lado3_x,lado3_y,lado4_x,lado4_y]
    else:
        #bresenham
        lado1_x,lado1_y = bresenham_algrithm(x1[0],x1[1],x2[0],x2[1])
        lado2_x,lado2_y = bresenham_algrithm(x1[0],x1[1],x3[0],x3[1])
        lado3_x,lado3_y = bresenham_algrithm(x2[0],x2[1],x3[0],x3[1])
        lado4_x,lado4_y = bresenham_algrithm(x3[0],x3[1],x4[0],x4[1])
        return [lado1_x,lado1_y,lado2_x,lado2_y,lado3_x,lado3_y,lado4_x,lado4_y]
    

def triangulos_equilateros(opcion,b,h):
    x1 =[0,0]
    x = b/2
    y = ((b**2)-(x**2))**0.5
    y = int(y)
    x2 =[round(x),y]
    x3 =[b-1,0]
    if opcion == 1:
        lado1_x,lado1_y = dda_algrithm(x1[0],x1[1],x2[0],x2[1])
        lado2_x,lado2_y = dda_algrithm(x1[0],x1[1],x3[0],x3[1])
        lado3_x,lado3_y = dda_algrithm(x2[0],x2[1],x3[0],x3[1])
        return [lado1_x,lado1_y,lado2_x,lado2_y,lado3_x,lado3_y]
    else:
        lado1_x,lado1_y = bresenham_algrithm(x1[0],x1[1],x2[0],x2[1])
        lado2_x,lado2_y = bresenham_algrithm(x1[0],x1[1],x3[0],x3[1])
        lado3_x,lado3_y = bresenham_algrithm(x2[0],x2[1],x3[0],x3[1])
        return [lado1_x,lado1_y,lado2_x,lado2_y,lado3_x,lado3_y]

def triangulos_rectangulos(opcion,b,h):
    x1 =[0,0]
    x2 =[b-1,h-1]
    x3 =[b-1,0]
    if opcion == 1:
        lado1_x,lado1_y = dda_algrithm(x1[0],x1[1],x2[0],x2[1])
        lado2_x,lado2_y = dda_algrithm(x1[0],x1[1],x3[0],x3[1])
        lado3_x,lado3_y = dda_algrithm(x2[0],x2[1],x3[0],x3[1])
        return [lado1_x,lado1_y,lado2_x,lado2_y,lado3_x,lado3_y]
    else:
        lado1_x,lado1_y = bresenham_algrithm(x1[0],x1[1],x2[0],x2[1])
        lado2_x,lado2_y = bresenham_algrithm(x1[0],x1[1],x3[0],x3[1])
        lado3_x,lado3_y = bresenham_algrithm(x2[0],x2[1],x3[0],x3[1])
        return [lado1_x,lado1_y,lado2_x,lado2_y,lado3_x,lado3_y]

def poligonos():
    pass

def options(opciones,algoritmo):
   

    if opciones == 1:
        # Cuadrado
        steps = int(input(' Distancia (px): '))
        coordenadas = cuadrilateros(algoritmo,steps,steps)
        window.callpx(coordenadas[0],coordenadas[1])
        window.callpx(coordenadas[2],coordenadas[3])
        window.callpx(coordenadas[4],coordenadas[5])
        window.callpx(coordenadas[6],coordenadas[7])
    elif opciones == 2:
        #rectangulo
        steps = int(input(' base (px): '))
        steps2 = int(input(' Altura (px): '))
        coordenadas = cuadrilateros(algoritmo,steps,steps2)
        window.callpx(coordenadas[0],coordenadas[1])
        window.callpx(coordenadas[2],coordenadas[3])
        window.callpx(coordenadas[4],coordenadas[5])
        window.callpx(coordenadas[6],coordenadas[7])
        pass
    elif opciones == 3:
        #equilatero
        steps = int(input(' base (px): '))
        coordenadas = triangulos_equilateros(algoritmo,steps,steps)
        window.callpx(coordenadas[0],coordenadas[1])
        window.callpx(coordenadas[2],coordenadas[3])
        window.callpx(coordenadas[4],coordenadas[5])
    elif opciones == 4:
        # Triangulo rectangulo
        steps = int(input(' base (px): '))
        steps2 = int(input(' Altura (px): '))
        coordenadas = triangulos_rectangulos(algoritmo,steps,steps2)
        window.callpx(coordenadas[0],coordenadas[1])
        window.callpx(coordenadas[2],coordenadas[3])
        window.callpx(coordenadas[4],coordenadas[5])
        pass
    elif opciones == 5:
        # Poligono
        pass
    else:
        print ("Opción incorrecta, intente ejecutando de nuevo el programa")
        exit()


def run():
    opc,alg = menu()
    window.show()
    options(opc,alg)
    turtle.mainloop()

if __name__ == "__main__":
    run()
    


    # a,b = dda_algrithm(5,8,9,0)
    # print("Hola")
    # print(f"{a},{b}")