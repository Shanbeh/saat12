
class cars:
    
    def __init__(self, Name_ = 'No name',Tupe_ = -1 ,r = -1,c =-1) :
        
        self.name_ = Name_
        
        # !type 5 ==> main car
        # type 1 and 2 : Horizontal
        # type 3 and 4 : Vertical
        self.type_ = Tupe_
        
        self.row_  = r
        self.cow_  = c

        # Front   Back
        self.move=[False , False]  # Front   Back

    def showinfo(self):

        print(" <<< SHOWINFO >>> ")

        print("Name: ",self.name_ , '   type: ',self.type_)
        print('(x,y) :  ',self.row_, ' , ',self.cow_)
        print('(F,B) : ',self.move)
        print(" <<< END_SHOWINFO >>> ")




class Stat:
    # all_car = [cars]

    def __init__(self) :
        self.bord=[
        #cow 0 1 2 3 4 5
            [0,0,0,0,0,0], # Row 0
            [0,0,0,0,0,0], # Row 1
            [0,0,0,0,0,0], # Row 2
            [0,0,0,0,0,0], # Row 3
            [0,0,0,0,0,0], # Row 4
            [0,0,0,0,0,0], # Row 5
        ]
        
        tmp_car = cars()
        self.all_car = [tmp_car]
    
    def show_Bord(self) :
        for i in range(6):
            # print('  >> ')
            for j in range(6):
                print('  ',self.bord[i][j],end = '')
            print()

    def show_cars(self) :
        index_ = 0
        for i in self.all_car:
            print('index: ', index_ ,end=' ')
            index_+=1
            i.showinfo()

    def set_car_in_Bord(self, car : cars ) :
        
        self.all_car.append(car)

        self.bord[car.row_][car.cow_] = car.type_

        # ! فقط ماشین اصلی هست که سرو تهش با ماشین های نوع یک فرق دارد
        tmp_type = car.type_ 
        if (tmp_type == 5):
            self.bord[car.row_][car.cow_ - 1] = car.type_
        
        elif(tmp_type == 1):
            self.bord[car.row_][car.cow_ + 1] = car.type_
       
        elif(tmp_type == 2):
            self.bord[car.row_][car.cow_ + 1] = car.type_
            self.bord[car.row_][car.cow_ + 2] = car.type_


        elif(tmp_type == 3):
            self.bord[car.row_ -1 ][car.cow_ ] = car.type_
        elif(tmp_type == 4):
            self.bord[car.row_ - 1][car.cow_ ] = car.type_
            self.bord[car.row_ - 2][car.cow_ ] = car.type_


    def set_move_car(self, car : cars):
        
        type_of_car_is_ = car.type_
        x_is , y_is = car.row_ , car.cow_


        # todo: می خواهیم دوتا متغییر حرکت رو به جلو و یا حرک رو به عقب هر ماشین ورودی را چک کنیم و یادمان هم هست که در بورد ها نوشتیم که چی به جی هست

        if (type_of_car_is_ == 5): # Min car

            # ! محور ایکس که ثابت هست و حرکت فقط روی محور وای است پس
            # X : x_is
            
            y_b , y_f = y_is + 1 , y_is - 2
            
            # <<  Back >>
            if (y_b <=5 and self.bord[x_is][y_b] == 0):
                car.move[1] = True
            else:
                car.move[1] = False
           
            # << Front >>
            if (y_f >=0  and self.bord[x_is][y_f] == 0):
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
            if(y_b >= 0 and self.bord[x_is][y_b] == 0):
                car.move[1] = True
            else:
                car.move[1] = False
            
            # << Front >>
            if (y_f <=5  and self.bord[x_is][y_f] == 0):
                  car.move[0] = True
            else:
                  car.move[0] = False
        
            # 3 TA
        elif(type_of_car_is_ == 2):
            #! این هم مثل نوع یک هست با این تفاوت که یک خانه بیشتر هست
             # X : X_is
            y_b , y_f = y_is - 1 , y_is + 3
            
            # <<  Back >>
            if(y_b >= 0 and self.bord[x_is][y_b] == 0):
                car.move[1] = True
            else:
                car.move[1] = False
           
            # << Front >>
            if (y_f <=5  and self.bord[x_is][y_f] == 0):
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
            if (x_f >= 0  and self.bord[x_f][y_is] == 0):
                  car.move[0] = True
            else:
                  car.move[0] = False
            
            # << Back >>
            if(x_b <= 5 and self.bord[x_b][y_is] == 0):
                  car.move[1] = True
            else:
                  car.move[1] = False

            # 3 TA
        elif(type_of_car_is_ == 4):

            #! Y= y_is
            x_b , x_f = x_is + 1, x_is - 3

            # << Front >>
            if (x_f >= 0  and self.bord[x_f][y_is] == 0):
                  car.move[0] = True
            else:
                  car.move[0] = False
            
            # << Back >>
            if(x_b <= 5 and self.bord[x_b][y_is] == 0):
                  car.move[1] = True
            else:
                  car.move[1] = False


    def set_move_of_all_car(self):
      
        for i in self.all_car:
            self.set_move_car(i)
            # i.showinfo()
            # print()

  

# !         <<  AI TIME  >>>         

#! هدف نهایی
    # def Tree_search(p,F):
    #     INT()
    #   while(1){
        #   if( len(fringe) == 0 ) { return exit(-3) Failure}
        #   cu = fringe.Remove()
        #   if( GOAL ( cu )) {retuen "Sooution"}
        #   else
        #  { fringe.push("EXPAND(cu)") }
    #   }



def is_selection(car_ : cars): # Bool >> T = yes F : No
    return car_.move[0] or car_.move[1]


def Make_test_Fringe(S : Stat):

        Test_Fringe =[] # ( i (type car) , chr = 'F' OR 'B' , index_of_car.... )

        index_of_car_in_Stat_all_car = 0        
        for i in S.all_car :
            
            if(is_selection(i)):

                if(i.move[0]):
                  
                    # i.showinfo()
                    Test_Fringe.append((i,'F',index_of_car_in_Stat_all_car))
                
                if(i.move[1]):
                    
                    # i.showinfo()
                    Test_Fringe.append((i,'B',index_of_car_in_Stat_all_car))

            index_of_car_in_Stat_all_car +=1
        
        print(len(Test_Fringe)) 
        return Test_Fringe

                        #  (  (type car) i , (char) 'F' OR 'B' , (int)  index_of_car.... )
def do_action( s:Stat , A):
    #
        # todo :قرار است همین اکشنی که به شکل یک تاپل سه تایی است را روی همین استیت اعمال کنیم
        # ! اول اون ماشین را کلا حذف کن چه تو نقشه و چه تو لیست ماشین ها و چه هرجای دیگه که یادم رفت
        # ! دوم مثل این که یک ماشین جدید وارد شده همین ماشین مه تو اکشن هست را وارد کن ولی با این تفاوت که خانه انتهای این ماشین باید بروز رسانی شود به مقدار جدید اکشنمان
        # مقدار سوم تاپل اکشن ورودی برای این است مه تو لیست ماشین های همان استیت بشود حذف کرد
        #  //پایان کد نویسی امروز 3 شنبه ساعت 12

    print('--> ',A[2])
   
    cur_car_is = A[0]
    x_  = cur_car_is.row_
    y_ = cur_car_is.cow_
    
    tmp_type =  cur_car_is.type_

    s.bord[x_][y_] = 0
    # exit(0)

    if (tmp_type == 5):
        s.bord[x_][y_ - 1] = 0

        if (A[1] == 'F'):
             cur_car_is.cow_ =  cur_car_is.cow_ - 1

        else:
             cur_car_is.cow_ =  cur_car_is.cow_ + 1

    elif(tmp_type == 1):
        s.bord[x_][y_ + 1] = 0
        
        if (A[1] == 'F'):
             cur_car_is.cow_ =  cur_car_is.cow_ + 1

        else:
             cur_car_is.cow_ =  cur_car_is.cow_ - 1


    elif(tmp_type == 2):
            s.bord[x_][y_+ 1] = 0
            s.bord[x_][y_ + 2] = 0

            if (A[1] == 'F'):
                cur_car_is.cow_ =  cur_car_is.cow_ + 1

            else:
                cur_car_is.cow_ =  cur_car_is.cow_ - 1

    # ! type 3 and 4
    elif(tmp_type == 3):
            s.bord[x_ -1 ][y_ ] = 0

            if (A[1] == 'F'):
                cur_car_is.row_ =  cur_car_is.row_ - 1

            else:
                cur_car_is.row_ =  cur_car_is.row_ + 1

    
    elif(tmp_type == 4):
        s.bord[x_ - 1][y_ ] = 0
        s.bord[x_ - 2][y_ ] = 0
        if (A[1] == 'F'):
            cur_car_is.row_ =  cur_car_is.row_ - 1

        else:
            cur_car_is.row_ =  cur_car_is.row_ + 1


    #! remot form ALl_Car
    s.all_car.pop(A[2])

    #! AdD Time
    s.set_car_in_Bord(cur_car_is)
    s.set_move_car(cur_car_is)

    # print("NOT YET")

if __name__ == '__main__':

    # // نوع دو را این که الان چه خانه ای خالی دارد را چک کن
    
    red_car = cars('red_car',5,2,4)
    car2  = cars('ali',1,0,4)
    
    car3  = cars('Reza' ,4,2,0)
    car4  = cars('Reza2',4,5,2)
    car5  = cars('Reza2',1,4,0)
    car6  = cars('Reza2',3,5,3)
    car7  = cars('Reza2',3,1,3)
    car8  = cars('Reza2',1,3,3)

    s_ = Stat()

        
    s_.set_car_in_Bord(red_car)
    s_.set_car_in_Bord(car2)

    s_.set_car_in_Bord(car3)
    s_.set_car_in_Bord(car4)
    s_.set_car_in_Bord(car5)
    s_.set_car_in_Bord(car6)
    s_.set_car_in_Bord(car7)
    s_.set_car_in_Bord(car8)



    s_.show_Bord()
    print("$$$$$$$$$$$$$$$")

    s_.set_move_of_all_car() 
    Test_1 = Make_test_Fringe(s_)
   
    
    
    print()
    foooo = 3
    Test_1[foooo][0].showinfo()
    print(Test_1[foooo][1])
    print(Test_1[foooo][2])
   
    print("****** Befor Do ACtion: ")
    s_.all_car[Test_1[foooo][2]].showinfo()

    # exit()
    # print(len(s_.all_car))

    print("$$$$$$$$$$$$")
    do_action(s_,Test_1[foooo])
    s_.show_Bord()
   


    # print("****** After Do ACtion: ")
    # Test_2 = Make_test_Fringe(s_)
    # # print('EE : ',len(Test_2))
    # s_.all_car[Test_2[foooo][2]].showinfo()
