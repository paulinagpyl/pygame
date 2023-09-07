# Este programa que usa módulo pygame muestra a Mario Bross,
# cuando se presiona barra espaciadora, aparece la tortuga que persigue a Mario por la pantalla,
# Mario se puede arrancar con las flechas del teclado.
# Desafío: entender el código, como funciona pygame y modificarlo con las sugerencias que están abajo
# pygame: pantalla, eventos  

# Importar librerías
import pygame
#import time

# Inicializar pygame
pygame.init()
# Pantalla de 400 x 300, alto x ancho
screen = pygame.display.set_mode((400, 300))

# Imágenes de mario y de la tortuga
tortuga = pygame.image.load('files/TortugaChernobyl.png')
mario = pygame.image.load('files/mario.png')

#Posición inicial de MArio
x = screen.get_width()//2
y = screen.get_height()//2

#velocidad de Mario
velocity_x = 5
velocity_y = 5

#velocidad de la tortuga
vel_tor = 3 

#Posición inicial de la tortuga
pos_tor_x = x+100
pos_tor_y = y+100

#Impedimos con un False que se muestre la tortuga
muestra_tortuga = False

# Que no se termine
running = True
while running:
    #escuchamos los eventos del programa
    for event in pygame.event.get():
        #hacemos que se detecte si apretamos la cruz que cierra la ventana
        if event.type == pygame.QUIT:
            running = False
        
        #activamos la escucha de los eventos del teclado
        elif event.type == pygame.KEYDOWN:
            
            #hacemos que el evento del teclado nos permita mover a Mario
            if event.key == pygame.K_LEFT:
                x -= velocity_x
            elif event.key == pygame.K_RIGHT:
                x += velocity_x
            elif event.key == pygame.K_UP:
                y -= velocity_y
            elif event.key == pygame.K_DOWN:
                y += velocity_y
            #hacemos que el evento del teclado nos permita mostrar a la tortuga
            elif event.key == pygame.K_SPACE:
                muestra_tortuga = True 
    
    #Pintamos un fondo negro y dibujamos a Mario en la posición (x,y)
    screen.fill((0, 0, 0))
    screen.blit(mario, (x, y))
    
    #La imagen se muestra sólo si muestra_imagen es True.
    if muestra_tortuga:
        screen.blit(tortuga,(pos_tor_x,pos_tor_y)) 
        # Comparamos las posiciones de mario y de la tortuga. 
        # Si la tortuga está a la izquierda de mario, hacemos que se mueva a la derecha.
        if pos_tor_x < x:
            pos_tor_x = pos_tor_x + vel_tor
        # Si la tortuga está a la arriba de mario, hacemos que se mueva hacia abajo.
        if pos_tor_y < y:
            pos_tor_y = pos_tor_y + vel_tor
        # Si la tortuga está a la derecha de mario, hacemos que se mueva a la izquierda.
        if pos_tor_x > x:
            pos_tor_x = pos_tor_x - vel_tor
        # Si la tortuga está abajo de mario, hacemos que se mueva hacia arriba.
        if pos_tor_y > y:
            pos_tor_y = pos_tor_y - vel_tor

    pygame.display.flip()
    pygame.time.delay(200)
    #time.sleep(1)

pygame.quit()

#Sugerencias para complegizar el programa:
#1. Que otro jugador pueda mover la tortuga
#2. Que se cuente un puntaje cada vez que la tortuga toca a Mario
#3. Mostrar un fondo que parezca un tablero de un juego y que tanto mario como la tortuga puedan navegar sólo por los espacios habilitados.