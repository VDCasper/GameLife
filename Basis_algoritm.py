import numpy as np
my_dim=np.array([(0,0,0,1,1,1),
                 (1,1,0,1,0,1),
                 (0,0,0,1,1,1),
                 (1,0,0,1,0,1),
                 (1,0,1,1,0,1),
                 (1,1,0,0,0,0)])

# git ciomment
array_copy = my_dim.copy()

j = 0
while j < 5:
    i = 0
    while i < 5:

        b = my_dim[j:j+3, i:i+3] # делаем срез матрицы 3х3
            
        if b[1][1] == 0  and np.sum(b) == 3: # проверяем состояние центарльноuj элемента b[1][1]
            array_copy[j+1, i+1] = 88
        
        elif b[1][1] == 1 and np.sum(b) > 4 or np.sum(b) < 3:
            array_copy[j+1, i+1] = 99 
        print(my_dim)
        print(b)
        print(array_copy)
      
        i += 1
    
    j += 1