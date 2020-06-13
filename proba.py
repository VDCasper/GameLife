import numpy as np

array_copy = np.array([(0,0,0,1,1,1),
                 (1,1,0,1,0,1),
                 (0,0,0,1,1,1),
                 (1,0,0,1,0,1),
                 (1,0,1,1,0,1),
                 (1,1,0,0,0,0)])
                 
while np.sum(array_copy) > 0:

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