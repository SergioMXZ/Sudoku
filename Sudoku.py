# Sergio Gonzalez Chavez
# Interfaz de un Sudoku jugable en pygame
# 31-MAY-23 V1.2

from tkinter import messagebox as mBox
import pygame # librería para el desarrollo de videojuegos en segunda dimensión 2D
from pygame import *
import copy  # Brinda opciones de copeado(para evitar problemas al copear listas)
import sys  # sys — Configuración específica del sistema(interprete y recurso para interactuar con el entorno operativo)
import random
pygame.font.init()  # inicializar pygame

# sudokuBase = [[0 for j in range(9)] for i in range(9)] # Crea la estructura del sudoku 9 * 9

sudokuInicial = []
sudokuFinal = []


def lineas_a_sudokus(sudoku_x):
    sudoku = [[ int(sudoku_x[i+j*9]) for i in range(9)] for j in range(9) ]
    return sudoku


def nuevo_sudoku():  # Introduce un nuevo sudoku
    global sudokuInicial
    global sudokuFinal
    numero_random = random.randrange(1, 12, 2)  # Se elige un numero al azar
    sudokus = open("sudokus.txt", 'r')  # Abre el archivo en el que estan todos los sudokus("Sudokus")
    sudokutxt = sudokus.readlines()  # Lee las lineas que contienen todos los sudokus
    sudoku_i = sudokutxt[numero_random]  # Con el numero al azar indicamos que linea guardar (sudoku inicial)
    sudoku_f = sudokutxt[numero_random-1]  # Con el numero al azar menos uno guardamos una linea antes (sudoku final)
    sudokus.close()  # Cierra el archivo
    # Se llama a la funcion para convertir la lineas a sudokus
    sudokuInicial = copy.deepcopy(list(lineas_a_sudokus(sudoku_i)[:]))
    sudokuFinal = copy.deepcopy(list(lineas_a_sudokus(sudoku_f)[:]))


nuevo_sudoku()
sudokuTemp = copy.deepcopy(list(sudokuInicial[:]))  # Copea el sudoku inicial al sudoku temporal

# Variables
total = 500  # Valor universal para el tamaño del sudoku
cordLinea = total / 3  # Para dibujar las lineas grandes
cordCuadro = cordLinea / 3  # Para dibujar las lineas pequeñas
entreNueve = total / 9  # Para dibujar los numeros

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ColorGeneral = (0, 153, 0)  # Color general del sudoku (permite cambiar el color del sudoku) inicia con verde
L_GREEN = (0, 255, 0)  # Verde claro que da la apariencia de un efecto neon.
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Tamaño
size = (553, 573)

# Crear Ventana
ventana = pygame.display.set_mode(size)  # Tamaño Ventana
pygame.display.set_caption("SUDOKU")  # Nombre Ventana
# Logo
img = pygame.image.load("LogoSudoku.png")  # Imagen de logo
display.set_icon(img)  # Coloca el logo

# ----- Botones(Tamaño) y su Texto respectivamente -----
miFuente = font.SysFont("ComicSans", 30)  # Fuente de texto
miFuenteMini = font.SysFont("ComicSans", 20)  # Fuente de texto mini
textoExit = miFuente.render("EXIT", True, WHITE)
botonExit = Rect(300, total + 13, 90, 50)
textoReload = miFuente.render("RELOAD", True, WHITE)
botonReload = Rect(150, total + 13, 135, 50)
textoCheck = miFuente.render("CHECK", True, WHITE)
botonCheck = Rect(19, total + 13, 115, 50)
textoNew = miFuente.render("NEW", True, ColorGeneral)
botonNew = Rect(410, total + 13, 85, 50)
colorGreen = Rect(501, total + 26, 20, 20)
colorOrange = Rect(501, total + 47, 20, 20)
colorBlue = Rect(522, total + 26, 20, 20)
colorMagenta = Rect(522, total + 47, 20, 20)
# ----- ----- ----- ----- ----- ----- ----- ----- -----
numPress = {
    pygame.K_KP1 : 1, pygame.K_1 : 1,
    pygame.K_KP2 : 2, pygame.K_2 : 2,
    pygame.K_KP3 : 3, pygame.K_3 : 3,
    pygame.K_KP4 : 4, pygame.K_4 : 4,
    pygame.K_KP5 : 5, pygame.K_5 : 5,
    pygame.K_KP6 : 6, pygame.K_6 : 6,
    pygame.K_KP7 : 7, pygame.K_7 : 7,
    pygame.K_KP8 : 8, pygame.K_8 : 8,
    pygame.K_KP9 : 9, pygame.K_9 : 9,
}

def quit_pygame():  # Cerrar ventana
    pygame.quit()
    sys.exit()


def funcion_check():  # Verifica si el estado del sudoku es incompleto/incorrecto/correcto
    ceros = 0
    for i in sudokuTemp:  # Calcula el numero de ceros/casillas-vacias en el sudoku
        for j in i:
            if j == 0:
                ceros += 1
    if sudokuTemp == sudokuFinal:  # Si son iguales
        mBox.showinfo("Inspected", "Sudoku is correct")
    elif ceros != 0:  # Si hay algun cero/casilla-vacia
        mBox.showwarning("Inspected", "Sudoku is incomplete")
    else:  # Si no es coorecto y no hay ceros/casillas-vacias
        mBox.showerror("Inspected", "Sudoku is wrong")


def pintar_numerosudoku(numero, borrar_uno):
    # Pintar numeros Permanentes y numeros ingresados que sean diferentes a "0"
    for i in range(9):
        for j in range(9):
            cuadro_mouse = Rect(i * entreNueve + 7, j * entreNueve + 6.4, 45, 45)  # Posicion que tomara si se dibuja
            rect_h = Rect(6.4, j * entreNueve + 3, total - 7, 51.5)  # Posicion que tomara si se dibuja
            rect_v = Rect(i * entreNueve + 4, 6.4, 50, total - 9)  # Posicion que tomara si se dibuja
            # Si el sudoku inicial en su actual posicion es "0"/casilla-vacia este permitira hacer lo siguiente
            if sudokuInicial[j][i] == 0:
                if cuadro_mouse.collidepoint(mouse.get_pos()):  # Seleccion casillas
                    draw.rect(ventana, WHITE, rect_h, 3)  # Dibuja el formato del rectangulo de seleccion horizontal
                    draw.rect(ventana, WHITE, rect_v, 3)  # Dibuja el formato del rectangulo de seleccion vertical
                    if numero != 0:  # Si "numero" es diferente a "0" se le asigna su valor a la casilla seleccionada
                        sudokuTemp[j][i] = numero
                    elif borrar_uno == 1:  # Si "borrar_uno" es "1" se cambia el valor a "0" dejando vacia esa casilla
                        sudokuTemp[j][i] = numero
                if sudokuTemp[j][i] != 0:  # Si el numero actual en el bucle es diferente a "0" se dibuja verde
                    numtemp = miFuente.render(str(sudokuTemp[j][i]), True, ColorGeneral)
                    ventana.blit(numtemp, (i * entreNueve + 20, j * entreNueve + 9))
            else:  # Si el sudoku inicial en su actual posicion No es "0"/casilla-no-vacia
                if cuadro_mouse.collidepoint(mouse.get_pos()):  # Seleccion casillas
                    draw.rect(ventana, ColorGeneral, cuadro_mouse, 0)  # Dibuja fondo al numero permanente seleccionado
                    draw.rect(ventana, WHITE, rect_h, 3)  # Dibuja el formato del rectangulo de seleccion horizontal
                    draw.rect(ventana, WHITE, rect_v, 3)  # Dibuja el formato del rectangulo de seleccion vertical
                # Pintamos el numero en Blanco de los numeros permanentes
                numpintao = miFuente.render(str(sudokuInicial[j][i]), True, WHITE)
                ventana.blit(numpintao, (i * entreNueve + 20, j * entreNueve + 9))


def ventana_juego():
    global sudokuTemp
    while True:
        numero = 0
        borrar_uno = 0
        global ColorGeneral
        ventana.fill(BLACK)  # Color de fondo
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Evento Cerrar de Ventana
                quit_pygame()
            if evento.type == MOUSEBUTTONDOWN and evento.button == 1:  # Evento click
                if botonExit.collidepoint(mouse.get_pos()):  # Click boton Exit
                    quit_pygame()
                if botonCheck.collidepoint(mouse.get_pos()):  # Click boton Ckeck
                    funcion_check()
                if botonReload.collidepoint(mouse.get_pos()):  # Click boton Reload
                    # Borra los numeros ingresados al copear el sudoku inicial al sudoku temporal
                    sudokuTemp = copy.deepcopy(sudokuInicial[:])
                if botonNew.collidepoint(mouse.get_pos()):  # Click boton New
                    nuevo_sudoku()  # Busca en el archivo un sudoku nuevo y lo asigna para que se dibuje
                    sudokuTemp = copy.deepcopy(sudokuInicial[:])  # Copea el sudoku inicial al sudoku temporal
                if colorOrange.collidepoint(mouse.get_pos()):
                    ColorGeneral = 'orange'
                if colorBlue.collidepoint(mouse.get_pos()):
                    ColorGeneral = 'blue'
                if colorMagenta.collidepoint(mouse.get_pos()):
                    ColorGeneral = 'magenta'
                if colorGreen.collidepoint(mouse.get_pos()):
                    ColorGeneral = (0, 153, 0)
            if evento.type == pygame.KEYDOWN:  # Detecta los numeros tecleados y se actualiza el valor de "numero"
                if evento.key in numPress:
                    numero = numPress[evento.key]
                if evento.key in (pygame.K_KP0, pygame.K_0, pygame.K_BACKSPACE, pygame.K_SPACE):
                    borrar_uno = 1  # Asigna un "1" para borrar el numero seleccionado
        # - Pinta fondos de botones al detectar el cursor sobre ellos
        if botonExit.collidepoint(mouse.get_pos()):
            draw.rect(ventana, RED, botonExit, 0)
        else:
            draw.rect(ventana, BLACK, botonExit, 0)
        if botonReload.collidepoint(mouse.get_pos()):
            draw.rect(ventana, BLUE, botonReload, 0)
        else:
            draw.rect(ventana, BLACK, botonReload, 0)
        if botonCheck.collidepoint(mouse.get_pos()):
            draw.rect(ventana, 'darkgreen', botonCheck, 0)
        else:
            draw.rect(ventana, BLACK, botonCheck, 0)
        if botonNew.collidepoint(mouse.get_pos()):
            draw.rect(ventana, WHITE, botonNew, 2)
        else:
            draw.rect(ventana, BLACK, botonNew, 0)
        """ --- Dibujo Sudoku --- """
        #       DIBUJA SUDOKU
        # - Lineas para separar botones
        pygame.draw.line(ventana, WHITE, [140, total + 130], [140, total + 20])
        pygame.draw.line(ventana, WHITE, [293, total + 130], [293, total + 20])
        pygame.draw.line(ventana, WHITE, [400, total + 130], [400, total + 20])
        for i in range(1, 9, 1):  # Lineas delgadas
            for j in range(1, 9, 1):
                pygame.draw.line(ventana, ColorGeneral,
                                 [10, cordCuadro * i], [total, cordCuadro * i])  # Lineas Horizontales
                pygame.draw.line(ventana, ColorGeneral,
                                 [cordCuadro * j, 10], [cordCuadro * j, total])  # Lineas Verticales
        # - Circulos negros entre las lineas delgadas  en cuadriculas para dar efecto de separacion
        for i in range(10):
            for j in range(10):
                pygame.draw.circle(ventana, BLACK, [cordCuadro * j, cordCuadro * i], 7)  # Circulos
        # - Lineas Grandes
        for i in range(1, 3, 1):  # Ciclo for para pintar dos veces las lineas en posiciones difentes
            pygame.draw.line(ventana, ColorGeneral,
                             [5, cordLinea * i], [total - 5, cordLinea * i], 3)  # lineas Horizontales
            pygame.draw.line(ventana, ColorGeneral,
                             [cordLinea * i, 5], [cordLinea * i, total - 5], 3)  # Lineas Verticales
            pygame.draw.line(ventana, L_GREEN,
                             [5, cordLinea * i], [total - 5, cordLinea * i])  # Neon de lineas Horizontales
            pygame.draw.line(ventana, L_GREEN,
                             [cordLinea * i, 5], [cordLinea * i, total - 5])  # Neon de lineas Verticales
        pintar_numerosudoku(numero, borrar_uno)  # pinta los numeros temporales e ingresados en el sudoku
        """ --- Dibujo Sudoku --- """
        # - Dibuja el texto de los botones
        texto_new = miFuente.render("NEW", True, ColorGeneral)  # Asigan el color general al texto del boton new
        ventana.blit(textoCheck, (25, total + 13))
        ventana.blit(textoReload, (155, total + 13))
        ventana.blit(textoExit, (305, total + 13))
        ventana.blit(texto_new, (415, total + 13))
        # - Cuenta las veces que se repite un numero en el sudoku
        # Se usa un diccionario para ir guardando la cantidad
        cantidad_numeros = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        for i in sudokuTemp:
            for j in i:
                if j in cantidad_numeros:  # Si j que es un numero en el sudoku temporal existe en el diccionario
                    cantidad_numeros[j] = cantidad_numeros[j]+1  # Se suma uno al numero que coincidio en el diccionario
        # - Dibuja los numeros de la derecha del sudoku (contador de numeros en sudoku)
        for i in range(9):
            cantidad_nums = cantidad_numeros.pop(i + 1)
            if cantidad_nums < 10:  # Si el contador de cualquier numero se mantiene menor a 10 su color sera el general
                numeros1al9 = miFuenteMini.render(str(cantidad_nums), True, ColorGeneral)
                ventana.blit(numeros1al9, (total + 30, cordCuadro * i + 25))
            else:  # Si el contador de cualquier numero exede 9 este sera rojo para indicar un error
                numeros1al9 = miFuenteMini.render(str(cantidad_nums), True, RED)
                ventana.blit(numeros1al9, (total + 30, cordCuadro * i + 25))
            numeros1al9 = miFuente.render(str(i+1), True, "darkgrey")  # Formato numeros grices
            ventana.blit(numeros1al9, (total+10, cordCuadro*i+8))  # Dibuja los nuemros grises
        # Cuadros para seleccionar el color del sudoku
        draw.rect(ventana, (0, 153, 0), Rect(501, total + 26, 20, 20), 0)
        draw.rect(ventana, 'orange', Rect(501, total + 47, 20, 20), 0)
        draw.rect(ventana, BLUE, Rect(522, total + 26, 20, 20), 0)
        draw.rect(ventana, 'magenta', Rect(522, total + 47, 20, 20), 0)
        # - Actualiza la pantalla
        pygame.display.flip()


ventana_juego()
