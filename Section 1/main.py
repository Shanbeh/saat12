import pygame
from pygame.locals import *

SIZE = (800, 700) 

cell_x = 134
cell_y = 90 #100

# ! color
RED = (255, 0, 0)
GRAY = (150, 150, 150)
bord_U_D = (0, 0, 0)
bord_L_R = (0, 0, 0)
car_color_type_1_2 = (255, 255, 0)
car_color_type_3_4 =( 22, 249, 249 )


pygame.init()
pygame.display.set_caption('No name :)')
screen = pygame.display.set_mode(SIZE)

                # L T     , w ,h
main_car = Rect((376,220), (cell_x  * 2 , cell_y)) # 510,355

all_car_type_1 = []
all_car_type_2 = []
all_car_type_3 = []
all_car_type_4 = []


def Make_car_(type_car,Last_x,Last_y):

   
    if(type_car == 1): # --

            tmp_L ,tmp_T  = (510+134 ), ( 30 - 110 )
            tmp_w ,tmp_h = cell_x  * 2 , cell_y

            tmp_L = tmp_L - (134 * Last_x)
            tmp_T = tmp_T + (110 * (Last_y ))

            
            if (Last_x == 2):
                tmp_L = 388 
            
            elif (Last_x == 3):
                tmp_L = 266

            elif (Last_x == 4):
                tmp_L = 144



            if (Last_y == 4):                
                tmp_T = 355
           
            elif(Last_y == 5):
                tmp_T = 467
           
            elif(Last_y == 6):
                tmp_T = 567

            if(tmp_L<20):
                tmp_L = 23

            tmp_= Rect((tmp_L,tmp_T), (tmp_w  , tmp_h))
            all_car_type_1.append(tmp_)

    elif (type_car == 2 ): # ---
          
            tmp_L ,tmp_T  = (376 +134 ), ( 30 - 110 )
            tmp_w ,tmp_h = cell_x  * 3  - (22 + 19) , cell_y

            # tmp_L = tmp_L - (132 * Last_x) #! 134 --> 132 !
            tmp_T = tmp_T + (110 * (Last_y ))

            if(Last_x == 1):
                tmp_L = 398 + 19
            
            elif (Last_x == 2):
                tmp_L = 276 + 19
            
            elif (Last_x == 3):
                tmp_L = 154 + 19
            
            elif(Last_x == 4):
                    tmp_L = 32 + 19



            if (Last_y == 4):
                tmp_T = 355
           
            elif(Last_y == 5):
                tmp_T = 467
           
            elif(Last_y == 6):
                tmp_T = 567





            tmp_= Rect((tmp_L,tmp_T), (tmp_w  , tmp_h))
            all_car_type_2.append(tmp_)

    elif (type_car == 3):

            tmp_L ,tmp_T  = (680), (20)
            tmp_w ,tmp_h = cell_x  - 53 , cell_y  * 2 +22

            if (Last_x == 2):
                tmp_L = 680 - (cell_x - 8 ) 
            
            elif (Last_x == 3):
                tmp_L = 680 - (2*cell_x - 20 )

            elif (Last_x == 4):
                tmp_L = 680 - ((3*cell_x - 10 ))

            elif (Last_x == 5):
                tmp_L = 680 - ((4*cell_x - 28 ))
                
            elif (Last_x == 6):
                tmp_L = 680 - ((5*cell_x - 20 ))

          
           #! Last_Y   
          

            if (Last_y == 2):
                tmp_T = 120

                
            elif(Last_y == 3):
                tmp_T = 220

            elif(Last_y == 4):
                tmp_T = 355
           
            elif(Last_y == 5):
                tmp_T = 467
           
            elif(Last_y == 6):
                tmp_T = 567



            tmp_= Rect((tmp_L,tmp_T), (tmp_w  , tmp_h))
            all_car_type_3.append(tmp_)

    elif (type_car == 4):
        
            tmp_L ,tmp_T  = (680), (20)
            tmp_w ,tmp_h = cell_x  - 53 , cell_y  * 3 +22

            if (Last_x == 2):
                tmp_L = 680 - (cell_x - 8 ) 
            
            elif (Last_x == 3):
                tmp_L = 680 - (2*cell_x - 20 )

            elif (Last_x == 4):
                tmp_L = 680 - ((3*cell_x - 25 ))

            elif (Last_x == 5):
                tmp_L = 680 - ((4*cell_x - 28 ))
                
            elif (Last_x == 6):
                tmp_L = 680 - ((5*cell_x - 20 ))


             #! Last_Y   

            tmp_= Rect((tmp_L,tmp_T), (tmp_w  , tmp_h))
            all_car_type_4.append(tmp_)


TOP_BORD  =  Rect((0,0), (798, 15))
DOWN_BORD =  Rect((0,667), (800, 30))
Right_bord = Rect((780,0), (20, 700))
Left_Bord =  Rect((0,0),  (20, 700))

# ! MOVE
                                      
dir = { 
         K_LEFT:[ (-1 * (cell_x - 12 ), 0) , '1_2'] ,  K_RIGHT: [((cell_x - 12 ), 0) ,'1_2'] ,
         K_UP: [((0), -1*(cell_y+20)) ,'3_4' ]      ,   K_DOWN: [((0), 1*(cell_y+20))   ,'3_4' ] 
      }



Make_car_(4,6,0)

Make_car_(3,4,2)


Now_my_TURRRN = []


if __name__ == '__main__':
        
    
    running = True

    while running: # Main 
    
        screen.fill(GRAY) 
        
        last_move_ = []

        for event in pygame.event.get():
            if (event.type == QUIT):
                running = False
            
            elif ( event.type == KEYDOWN  ) :
                if (event.key in dir):
                    
                    last_move_.append(dir[event.key][1])
                    
                    if(dir[event.key][1] == '1_2' ):
                        
                        
                        if(len(Now_my_TURRRN)==0):
                                print("***:  ", main_car)
                                main_car.move_ip(dir[event.key][0])
                        else:
            
                            type_ =  Now_my_TURRRN [1]
                            r = Now_my_TURRRN[0]
                          

                            r.move_ip(dir[event.key][0])


                    if (dir[event.key][1] == '3_4'):

                        type_ =  Now_my_TURRRN [1]
                        r = Now_my_TURRRN[0]
                      

                        r.move_ip(dir[event.key][0])

                else:
                    "Brooo baba"

            elif ( event.type == pygame.MOUSEBUTTONUP ):
                
                    mouse_position = pygame.mouse.get_pos()

                    is_out_sid = True
                    
                    for r in all_car_type_1:
                        if(r.collidepoint(mouse_position)):
                            
                                                
                            while(len(Now_my_TURRRN)!= 0):
                                Now_my_TURRRN.pop()
                                # print('-->' ,Now_my_TURRRN)

                            Now_my_TURRRN.append(r)
                            Now_my_TURRRN.append("type_1")
                            is_out_sid = False

                    for r in all_car_type_2:
                        if(r.collidepoint(mouse_position)):
                        
                            # global Now_my_TURRRN
                            
                            while(len(Now_my_TURRRN)!= 0):
                                Now_my_TURRRN.pop()
                                # print('-->' ,Now_my_TURRRN)

                        
                            Now_my_TURRRN.append(r)
                            Now_my_TURRRN.append("type_2")
                            
                            # print(Now_my_TURRRN)
                            is_out_sid = False

                    
                    for r in all_car_type_3:
                        if(r.collidepoint(mouse_position)):
                        
                            # global Now_my_TURRRN
                            
                            while(len(Now_my_TURRRN)!= 0):
                                Now_my_TURRRN.pop()
                                # print('-->' ,Now_my_TURRRN)

                        
                            Now_my_TURRRN.append(r)
                            Now_my_TURRRN.append("type_3")
                            
                            # print(Now_my_TURRRN)
                            is_out_sid = False


                    for r in all_car_type_4:
                        if(r.collidepoint(mouse_position)):
                        
                            # global Now_my_TURRRN
                            
                            while(len(Now_my_TURRRN)!= 0):
                                Now_my_TURRRN.pop()
                                # print('-->' ,Now_my_TURRRN)

                        
                            Now_my_TURRRN.append(r)
                            Now_my_TURRRN.append("type_3")
                        
                            
                            # print(Now_my_TURRRN)
                            is_out_sid = False




                    if (main_car.collidepoint(mouse_position )):
                        print("main car Move!")   
                        # is_out_sid = False


                    if is_out_sid == True:
                        Now_my_TURRRN = []

        collide = pygame.Rect.colliderect (main_car  , Right_bord) # FOR RGHIT
        collide2 = pygame.Rect.colliderect(main_car , Left_Bord) # FOR LEFT
    

        if ( collide or collide2): #1_2 R & L to bord

          
            a = list(dir[event.key][0])                
            a[0] = a[0] * -1
            a[1] = a[1] * -1        
            a = tuple(a)
            main_car.move_ip(a)

        pygame.draw.rect(screen, RED, main_car)

        pygame.draw.rect(screen, bord_U_D , TOP_BORD)
        pygame.draw.rect(screen, bord_U_D, DOWN_BORD)

        pygame.draw.rect(screen, bord_U_D, Right_bord)
        pygame.draw.rect(screen, bord_U_D, Left_Bord)


        for i in [all_car_type_1,all_car_type_2]:
            for r in i:
                pygame.draw.rect(screen, car_color_type_1_2, r)
        
        for i in [all_car_type_3,all_car_type_4]:
            for r in i:
                pygame.draw.rect(screen, car_color_type_3_4, r)


        pygame.display.update()
        pygame.display.flip()

    pygame.quit()
