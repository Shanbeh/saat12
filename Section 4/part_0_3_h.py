
# todo: چک کردن کل مخصوصا ماشین قرمز را و این که الکوریتم .،. DFS است یا BFS آخر 

import copy

class cars:
    
    def __init__(self, Name_ = 'No name',Tupe_ = -1 ,r = -1,c =-1) :
        
        self.name_ = Name_
      
         #
            # !type 5 ==> main car
            # type 1 and 2 : Horizontal
            # type 3 and 4 : Vertical
      
        self.type_ = Tupe_
        
        self.row_  = r
        self.column_  = c

                  # Front   Back
        self.move=[False , False]  # Front   Back

    def showinfo(self):

        print(" <<< SHOWINFO >>> ")
        print("Name: ",self.name_ , '   type: ',self.type_)
        print('(x,y) :  ',self.row_, ' , ',self.cow_)
        print('(F,B) : ',self.move)
        print(" <<< END_SHOWINFO >>> ")

    def showinfo_2(self):

        print("Name: ",self.name_ , ' type: ',self.type_ ,end=' ')
        print('(x,y): ',self.row_,',',self.column_,end=' ')
        print('(F,B): ',self.move,end =' ')


class Stat:
    # all_car = [cars]

    def __init__(self) :
        
        self.board=[
        #col 0 1 2 3 4 5
            [0,0,0,0,0,0], # Row 0
            [0,0,0,0,0,0], # Row 1
            [0,0,0,0,0,0], # Row 2
            [0,0,0,0,0,0], # Row 3
            [0,0,0,0,0,0], # Row 4
            [0,0,0,0,0,0], # Row 5
        ]
        
        tmp_car = cars()
        self.all_car = [tmp_car]

        self.Tra = []
        self.g_n = 0

    def show_Board(self) :
        for i in range(6):
            for j in range(6):
                print('  ',self.board[i][j],end = '')
            print()

    def show_cars(self) :
        index_ = 0
        for i in self.all_car:
            print('index: ', index_ ,end=' ')
            index_+=1
            i.showinfo()

    def set_car_in_Board(self, car : cars ) :
        
        self.all_car.append(car)

        self.board[car.row_][car.column_] = car.type_

        # ! فقط ماشین اصلی هست که سرو تهش با ماشین های نوع یک فرق دارد
        tmp_type = car.type_ 
        
        if (tmp_type == 5):
            self.board[car.row_][car.column_ - 1] = car.type_
        
        elif(tmp_type == 1):
            self.board[car.row_][car.column_ + 1] = car.type_
        elif(tmp_type == 2):
            self.board[car.row_][car.column_ + 1] = car.type_
            self.board[car.row_][car.column_ + 2] = car.type_


        elif(tmp_type == 3):
            self.board[car.row_ -1 ][car.column_ ] = car.type_
        elif(tmp_type == 4):
            self.board[car.row_ - 1][car.column_ ] = car.type_
            self.board[car.row_ - 2][car.column_ ] = car.type_

    def set_move_car(self, car : cars): # ==> car.Move =[F = ? , B =  ?] ;
        
        type_of_car_is_ = car.type_
        
        x_is , y_is = car.row_ , car.column_

        # todo: می خواهیم دوتا متغییر حرکت رو به جلو و یا حرک رو به عقب هر ماشین ورودی را چک کنیم و یادمان هم هست که در بورد ها نوشتیم که چی به جی هست

        if (type_of_car_is_ == 5): # Min car

            # ! محور ایکس که ثابت هست و حرکت فقط روی محور وای است پس
            # X : x_is
            
            y_b , y_f = y_is + 1 , y_is - 2
            
            # <<  Back >>
            if (y_b <=5 and self.board[x_is][y_b] == 0):
                car.move[1] = True
            else:
                car.move[1] = False
           
            # << Front >>
            if (y_f >=0  and self.board[x_is][y_f] == 0):
                  car.move[0] = True
            else:
                  car.move[0] = False
        
            # 2 TA 
        elif(type_of_car_is_ == 1):
            # ! در اصل ماشین اصلی هم همین نوع است ولی بااین تفاوت که ماشین اصلی و این نوع سرو ته است
            # ! پس باز هم محور یک؛ همون ایکس ها ثابت است
            
            # X : X_is
            y_b , y_f = y_is - 1 , y_is + 2
            
            # <<  Back >>
            if(y_b >= 0 and self.board[x_is][y_b] == 0):
                car.move[1] = True
            else:
                car.move[1] = False
            
            # << Front >>
            if (y_f <=5  and self.board[x_is][y_f] == 0):
                  car.move[0] = True
            else:
                  car.move[0] = False
        
            # 3 TA
        elif(type_of_car_is_ == 2):
            #! این هم مثل نوع یک هست با این تفاوت که یک خانه بیشتر هست
             # X : X_is
            y_b , y_f = y_is - 1 , y_is + 3
            
            # <<  Back >>
            if(y_b >= 0 and self.board[x_is][y_b] == 0):
                car.move[1] = True
            else:
                car.move[1] = False
           
            # << Front >>
            if (y_f <=5  and self.board[x_is][y_f] == 0):
                  car.move[0] = True
            else:
                  car.move[0] = False
        

        # ! از این جا به بعد نوع های عمودی هستند
            # 2 TA 
        elif(type_of_car_is_ == 3):
            # در این حالت محور دوم ما یعنی ایگرد ها ثابت است و حرحت ناشی از عوض شدن شماره سطر ها پس
            #! Y= y_is
            x_b , x_f = x_is + 1, x_is - 2

            # << Front >>
            if (x_f >= 0  and self.board[x_f][y_is] == 0):
                  car.move[0] = True
            else:
                  car.move[0] = False
            
            # << Back >>
            if(x_b <= 5 and self.board[x_b][y_is] == 0):
                  car.move[1] = True
            else:
                  car.move[1] = False

            # 3 TA
        elif(type_of_car_is_ == 4):

            #! Y= y_is
            x_b , x_f = x_is + 1, x_is - 3

            # << Front >>
            if (x_f >= 0  and self.board[x_f][y_is] == 0):
                  car.move[0] = True
            else:
                  car.move[0] = False
            
            # << Back >>
            if(x_b <= 5 and self.board[x_b][y_is] == 0):
                  car.move[1] = True
            else:
                  car.move[1] = False

    def set_move_of_all_car(self):
        for i in self.all_car:
            self.set_move_car(i)

    def h_n(self ):

        fa = 1

        for i in range(6):
         
            if (self.board[2][i] == 0):
                 fa += 2
            elif (self.board[2][i] != 5):
                 fa += 3
            else:
                break

        # fa *=-1
        self.g_n += fa


# !         <<  Ai TIME  >>>         

#! هدف نهایی
    # def Tree_search(p,F):
    #     INT()
    #  (0) while(1){
        #  (1) if( MT() ) { return Failure or  exit(-3) }
        #  (2) cu = fringe.Remove()
        #  (3) if( GOAL ( cu )) {retuen "Sooution"}
        #  (4) else
        #           { fringe.push("EXPAND(cu)") }
    #   }



def MT() -> bool:
    return False

    # T ==> Yes
def is_goald(stat_ : Stat) -> bool: 
    return (stat_.board[2][0] == 5)

def is_selection(car_ : cars) -> bool: # Bool >> T = yes /\ F : No
    return car_.move[0] or car_.move[1]

                            # ( i ( car) , chr = 'F' OR 'B' , index_of_car )
def Make_test_Fringe(S : Stat) -> list:  #  << Mina Fun>>

        Test_Fringe =[] # ( i (type : car) , chr = 'F' OR 'B' , index_of_car )

        index_of_car_in_Stat_all_car = 0
        
        for i in S.all_car :
            
            if(is_selection(i)):

                if(i.move[0]):

                    Test_Fringe.append( (i,'F',index_of_car_in_Stat_all_car) )
                
                if(i.move[1]):

                    Test_Fringe.append((i,'B',index_of_car_in_Stat_all_car))

            index_of_car_in_Stat_all_car +=1
        
        # print('len (Test_Fringe): ',len(Test_Fringe)) 
        return Test_Fringe

                        #  (  (car) i , (char) 'F' OR 'B' , (int)  index_of_car.... )
def do_action( s : Stat , AA) -> Stat:
    #
        # todo :قرار است همین اکشنی که به شکل یک تاپل سه تایی است را روی همین استیت اعمال کنیم
        # ! اول اون ماشین را کلا حذف کن چه تو نقشه و چه تو لیست ماشین ها و چه هرجای دیگه که یادم رفت
        # ! دوم مثل این که یک ماشین جدید وارد شده همین ماشین مه تو اکشن هست را وارد کن ولی با این تفاوت که خانه انتهای این ماشین باید بروز رسانی شود به مقدار جدید اکشنمان
        # مقدار سوم تاپل اکشن ورودی برای این است مه تو لیست ماشین های همان استیت بشود حذف کرد
        #  //پایان کد نویسی امروز 3 شنبه ساعت 12

    A = copy.deepcopy(AA)
    tmp_s = copy.deepcopy(s)
   
    cur_car_is = A[0] 
    cur_car_is : cars
    
    x_  = cur_car_is.row_
    y_ = cur_car_is.column_
    
    tmp_type =  cur_car_is.type_

    tmp_s.board[x_][y_] = 0

    if (tmp_type == 5):
        tmp_s.board[x_][y_ - 1] = 0

        if (A[1] == 'F'):
             cur_car_is.column_ =  cur_car_is.column_ - 1

        else: # Ba
             cur_car_is.column_ =  cur_car_is.column_ + 1

    elif(tmp_type == 1):
        tmp_s.board[x_][y_ + 1] = 0
        
        if (A[1] == 'F'):
             cur_car_is.column_ =  cur_car_is.column_ + 1

        else: # Back
             cur_car_is.column_ =  cur_car_is.column_ - 1
    elif(tmp_type == 2):
            tmp_s.board[x_][y_+ 1] = 0
            tmp_s.board[x_][y_ + 2] = 0

            if (A[1] == 'F'):
                cur_car_is.column_ =  cur_car_is.column_ + 1

            else: # B
                cur_car_is.column_ =  cur_car_is.column_ - 1

    # ! type 3 and 4
    elif(tmp_type == 3):
            tmp_s.board[x_ -1 ][y_ ] = 0

            if (A[1] == 'F'):
                cur_car_is.row_ =  cur_car_is.row_ - 1

            else:
                cur_car_is.row_ =  cur_car_is.row_ + 1 
    elif(tmp_type == 4):
        tmp_s.board[x_ - 1][y_ ] = 0
        tmp_s.board[x_ - 2][y_ ] = 0
        if (A[1] == 'F'):
            cur_car_is.row_ =  cur_car_is.row_ - 1
        else:
            cur_car_is.row_ =  cur_car_is.row_ + 1


    #! remot form ALl_Car ?
    tmp_s.all_car.pop(A[2])



    #! AdD Time
    tmp_s.set_car_in_Board(cur_car_is)
    # tmp_s.set_move_car(cur_car_is)
    #! NEW
    for i in tmp_s.all_car:
        tmp_s.set_move_car(i)
    

    

    #! g(N)
    tmp_s.g_n += 1

    #! H(N)
    tmp_s.h_n()


    return tmp_s


def INT_car_Mian(sta : Stat) :
    
    red_car = cars('red_car',5,2,4)
    sta.set_car_in_Board(red_car)

            # name , Type , Row (X) , col (Y)
  
            # name , Type , Row (X) , col (Y)
    Car_ = [
        cars('A',4,2,2) ,
        cars('B',3,4,3) ,
                            # 120
        cars('c',2,4,0) ,
        # cars('D',2,5,2) ,
    ]
    for i in Car_:
        sta.set_car_in_Board(i)



if __name__ == '__main__':

    s_ = Stat()

    INT_car_Mian(s_)
    s_.show_Board()
    # exit(0)
    print("\n~~~~~~~~~~~~~~\n")

    s_.set_move_of_all_car() 
    Test_1 = Make_test_Fringe(s_)

    # print(Test_1)
    # exit(0)   
    # ! تا الان اوکی هست

    List_of_min_Stat = [s_]

    taad_takrar = 0

    while (True):

        print('taad_takrar -> ',taad_takrar)
        taad_takrar+=1

        if(len(List_of_min_Stat) == 0):
            print(" :( ")
            exit(-3)

        #! مال جلسه جدید

        # Cu_stat = List_of_min_Stat.pop(0)

        min_Val = 100000 #max_int
        cu_ind = -1
        for i in range(len(List_of_min_Stat)):
            
            tmp_val= List_of_min_Stat[i].g_n

            if(tmp_val < min_Val) :
                min_Val = tmp_val
                cu_ind = i

        Cu_stat = List_of_min_Stat.pop(cu_ind)

        
        if(taad_takrar % 5000 <= 2  ):
            Cu_stat.show_Board()
            input(">> ")


        if(is_goald(Cu_stat)):

                    print(" :)")
                    print(len(Cu_stat.Tra))
                    for i in range(len(Cu_stat.Tra)):
                        (Cu_stat.Tra[i][0]).showinfo_2()
                        print(">>>> ",Cu_stat.Tra[i][1])
                       
                    exit(+1)
      
        Test_2 = Make_test_Fringe(Cu_stat)

        for i in Test_2:
            TMP_Time =  do_action(Cu_stat,i)
            TMP_Time.Tra.append(i)
            List_of_min_Stat.append(TMP_Time)