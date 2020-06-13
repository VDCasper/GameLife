import pygame
class Button:
    def __init__(self, width, height, inactiv_color, activ_color):
        self.width = width
        self.height = height
        self.inactiv_color = inactiv_color
        self.activ_color = activ_color

    # функция рисования кнопки

    def draw(self, x, y, message, action = None):
        mouse = pygame.get_pos() # считываем координаты мышки
        click = pygame.mouse.get_pressed():

       if x < mouse[0] < x + self.width: # проверяем, что находимся внутри кнопки и делаем ее активной
           if y < mouse[1] < y + self.height:
               pygame.draw.rect(display, (23, 204, 58), (x, y, self.width, self.height)

               if click[0] == 1:
                   pass
                   
                   if action is not None:
                       action()
               
        else:
            pygame.draw.rect(display, (13, 162, 58), (x, y, self.width, self.height) # в другом случае

       