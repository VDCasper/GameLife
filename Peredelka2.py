import pygame
import sys
import pygbutton
import numpy as np

pygame.init()

SIZE_X = 1020
SIZE_Y = 1020
FPS = 30
clock = pygame.time.Clock()
size = (SIZE_X, SIZE_Y)
screen = pygame.display.set_mode(size)
width = 20 
heigth = 20
white = (255, 255, 255)
red = (255, 0, 0)
margin = 4
#mas = [[0] * 10 for i in range(10)]

COUNT_X = SIZE_X//(width+margin)
COUNT_Y = SIZE_Y//(heigth+margin)
print(COUNT_X, COUNT_Y)
mas = np.zeros((SIZE_X//(width+margin), SIZE_Y//(heigth+margin)), int)
print(mas) 

def life_start():
    for row in range(COUNT_Y):
        #color = white
        for col in range(COUNT_X):
            if mas[row][col] == 1:
                color = red
            else: 
                color = white


            x = col * width + (col+1) * margin
            y = row * heigth + (row+1) * margin
            pygame.draw.rect(screen, color, (x, y, width, heigth))

buttonObj = pygbutton.PygButton((400, 500, 60, 30), 'Start')
buttonStop = pygbutton.PygButton((300, 500, 60, 30), 'Stop')  

while True:
    clock.tick(FPS)
    buttonObj.draw(screen) # where DISPLAYSURFACE was the Surface object returned from pygame.display.set_mode() 
    buttonStop.draw(screen) # where DISPLAYSURFACE was the Surface object returned from pygame.display.set_mode() 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:

            
            x_mouse, y_mouse = pygame.mouse.get_pos()

            if y_mouse < (SIZE_Y-30):
             
                print(f'x={x_mouse} y={y_mouse}')
                column = x_mouse//(margin + width)
                row = y_mouse//(margin + heigth)
                mas[row][column] ^= 1
                print(mas)
            else:
                pass
        
    life_start()

    
    array_copy = mas.copy()
    
    if 'click' in buttonObj.handleEvent(event):
        
        
        while np.sum(array_copy) > 0:
            play = True
            if 'click' in buttonStop.handleEvent(event):
                play = False
                pygame.quit()
            pygame.time.delay(5)
            

            j = 0
            while j < (heigth-1):
                i = 0
                while i < (width-1):

                    b = mas[j:j+3, i:i+3] # делаем срез матрицы 3х3
                        
                    if b[1][1] == 0  and np.sum(b) == 3: # проверяем состояние центарльноuj элемента b[1][1]
                        array_copy[j+1, i+1] = 1
                    
                    elif b[1][1] == 1 and np.sum(b) > 4 or np.sum(b) < 3:
                        array_copy[j+1, i+1] = 0 
                    #print(mas)
                    #print(b)
                    #print(array_copy)
                
                    i += 1
                
                j += 1
            
            
            print(array_copy)

            
            life_start()

            pygame.display.update()
            pygame.time.delay(100)
            mas = array_copy.copy()
                
            
    pygame.display.update()
