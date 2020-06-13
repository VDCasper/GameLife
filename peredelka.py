import pygame
import sys
import pygbutton
import numpy as np

pygame.init()


width = heigth = 20
margin = 3          
SIZE_COLUMN = 40
SIZE_ROW = 40
FPS = 20
clock = pygame.time.Clock()
size = ((width + margin)*SIZE_COLUMN - margin, (heigth+margin)*SIZE_ROW-margin)
screen = pygame.display.set_mode(size)

def draw_cell():
    for row in range(SIZE_ROW):
        #color = white
        for col in range(SIZE_COLUMN):
            if mas[row][col] == 1:
                color = red
            else: 
                color = white


            x = col * width + (col+1) * margin
            y = row * heigth + (row+1) * margin
            pygame.draw.rect(screen, color, (x, y, width, heigth))
    



buttonObj = pygbutton.PygButton((800, 750, 60, 30), 'Start')
buttonStop = pygbutton.PygButton((600, 750, 60, 30), 'Stop')


            


white = (255, 255, 255)
red = (255, 0, 0)

#mas = [[0] * 10 for i in range(10)]
mas = np.zeros((width, heigth), int)
print(mas) 




while True:
    clock.tick(FPS)
    buttonObj.draw(screen) # where DISPLAYSURFACE was the Surface object returned from pygame.display.set_mode() 
    buttonStop.draw(screen) # where DISPLAYSURFACE was the Surface object returned from pygame.display.set_mode() 

    for event in pygame.event.get():

        
        if 'click' in buttonStop.handleEvent(event):
            break

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:

            
            x_mouse, y_mouse = pygame.mouse.get_pos()

            if y_mouse < SIZE_ROW:
             
                print(f'x={x_mouse} y={y_mouse}')
                column = x_mouse//(margin + width)
                row = y_mouse//(margin + heigth)
                mas[row][column] ^= 1
                print(mas)
        
  
    draw_cell()

    
    array_copy = mas.copy()
    
    if 'click' in buttonObj.handleEvent(event):
        
        
        
        
        while np.sum(array_copy) > 0:
        #while None ('click' in buttonStop.handleEvent(event)):
            if 'click' in buttonStop.handleEvent(event):
                break
            
            pygame.time.delay(50)
            

            j = 0
            while j < SIZE_COLUMN-1:
                if 'click' in buttonStop.handleEvent(event):
                    break
                i = 0
                while i < SIZE_ROW-1:

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

            draw_cell()

            pygame.display.update()
            pygame.time.delay(100)
            #play = True
            
            #play = False
            
            
            mas = array_copy.copy()
            
            
                
            
    pygame.display.update()
