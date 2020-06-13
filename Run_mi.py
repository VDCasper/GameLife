import pygame
import sys
import pygbutton
import numpy as np

pygame.init()


FPS = 30
clock = pygame.time.Clock()
size = (510, 540)
screen = pygame.display.set_mode(size)
width = heigth = 40
white = (255, 255, 255)
red = (255, 0, 0)
margin = 10
#mas = [[0] * 10 for i in range(10)]
mas = np.zeros((10, 10), int)
print(mas) 

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

            if y_mouse < 510:
             
                print(f'x={x_mouse} y={y_mouse}')
                column = x_mouse//(margin + width)
                row = y_mouse//(margin + heigth)
                mas[row][column] ^= 1
                print(mas)
        
    
    for row in range(10):
        #color = white
        for col in range(10):
            if mas[row][col] == 1:
                color = red
            else: 
                color = white


            x = col * width + (col+1) * margin
            y = row * heigth + (row+1) * margin
            pygame.draw.rect(screen, color, (x, y, width, heigth))

    
    array_copy = mas.copy()
    
    if 'click' in buttonObj.handleEvent(event):
        
        
        while np.sum(array_copy) > 0:
            play = True
            if 'click' in buttonStop.handleEvent(event):
                play = False
                pygame.quit()
            pygame.time.delay(5)
            

            j = 0
            while j < 9:
                i = 0
                while i < 9:

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

            
            for row in range(10):
                #color = white
                for col in range(10):
                    if array_copy[row][col] == 1:
                        color = red
                    else: 
                        color = white


                    x = col * width + (col+1) * margin
                    y = row * heigth + (row+1) * margin
                    pygame.draw.rect(screen, color, (x, y, width, heigth))
                    pygame.display.update()
                    pygame.time.delay(5)
            mas = array_copy.copy()
                
            
    pygame.display.update()
