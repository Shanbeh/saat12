
import copy

class Stat:

    # /.////////////////////// variable ////////////////
    tr=[]

    board_ = []
          #  X,Y
    pwd  = (-1,-1) # wher am i ?  :) #!print working directory 

    Goal = (5,5)

            #  Up    Right   Down     Left
    move_ = [False , False  , False , False]

    # /.////////////////////// INT() ////////////////

    def __init__(self) -> None:
       
        #! 0 ==> MT
        #! 1 ==> Full
        #! 2 ==> Goal
        #! 3 --> sina
       
        self.board_ = [
            #col 0 1 2 3 4 5
                [3,0,0,1,0,0], # Row 0
                [0,1,0,1,0,0], # Row 1
                [0,1,0,0,0,1], # Row 2
                [0,1,1,0,1,0], # Row 3
                [0,0,0,0,0,0], # Row 4
                [1,1,1,1,1,2], # Row 5
             ]
        
        self.tr = []

        # self.pwd = (0,0)
        self.Set_of_pwa()


    def INT_Set_board(self,b:list,  ) -> None:
        
        self.board_ =  b
        self.tr = []
        self.Set_of_pwa()

        return


    # /.///////////////////// main def() ////////////////

    def Set_of_pwa(self) -> None:
        for i in range(len(self.board_)):
            for j in range(len(self.board_[0])):
                if(self.board_[i][j]==3):
                    self.pwd = (i,j)
                    return

    def wher_can_i_move(self) -> None:
        self.move_ = [False,False,False,False]
        x = self.pwd[0]
        y = self.pwd[1]
        
        #! Up 0
        if(x-1>=0):

            if(self.board_[x-1][y] != 1):
                self.move_[0] = True
                
            else:
                self.move_[0] = False
        
        #! Right 1
        if(y+1<=5):
            if(self.board_[x][y+1] != 1):
                self.move_[1] = True
            else:
                self.move_[1] = False

        #! Down 2
        if(x+1 <= 5):
            if(self.board_[x+1][y] != 1):
                self.move_[2] = True
            else:
                self.move_[2] = False

        #! Left 3
        if(y-1>= 0):
            if(self.board_[x][y-1] != 1):
                self.move_[3] = True
            else:
                self.move_[3] = False

    def action_in_this_stat(self) -> list : # list Of Stat 
        x , y = self.pwd[0] , self.pwd[1]

        if(self.move_[0]): # can move Up so
            self.board_[x][y] = 0
            self.board_[x-1][y] = 3
            self.Set_of_pwa()

        if(self.move_[1]) : #  Right is ok
            self.board_[x][y] = 0
            self.board_[x][y+1] = 3
            self.Set_of_pwa()

        if(self.move_[2]) : #  Down is True
            self.board_[x][y] = 0
            self.board_[x+1][y] = 3
            self.Set_of_pwa()


        if(self.move_[2]) : #  Now go Left
            self.board_[x][y] = 0
            self.board_[x][y-1] = 3
            self.Set_of_pwa()



    # /.////////////////////// Test Time ////////////////

    def show_(self) -> None:
        
        print()
        
        for i in range(len(self.board_)):
            print('\t',end='')
            for j in range(len(self.board_[0])):
                print(self.board_[i][j],' ',end='')
            print()
        
        print()

        print('pwd: ',self.pwd)
        print('move: ',self.move_)

    def Is_goal_stat(self) -> bool:
        return (self.pwd == self.Goal)

def action_in_this_stat(s : Stat) -> list : # list Of Stat 
    A = []
    tmp_s = copy.deepcopy(s)
    
    x , y = tmp_s.pwd[0] , tmp_s.pwd[1]

    if(s.move_[0]  == True ): # can move Up so
        tmp_s.board_[x][y] = 0
        tmp_s.board_[x-1][y] = 3
        tmp_s.Set_of_pwa()
        
        tmp_s.wher_can_i_move()
        
        tmp_s.tr.append('U')

        A.append(tmp_s)
        tmp_s = copy.deepcopy(s)

    if(s.move_[1]  == True ) : #  Right is ok
        
        # tmp_s.show_()
        # s.show_()
        tmp_s.board_[x][y] = 0
        
        tmp_s.board_[x][y+1] = 3
        tmp_s.Set_of_pwa()
        
        tmp_s.wher_can_i_move()
        tmp_s.tr.append('R')

        A.append(tmp_s)
        tmp_s = copy.deepcopy(s)

    if(s.move_[2]  == True) : #  Down is True
        tmp_s.board_[x][y] = 0
        tmp_s.board_[x+1][y] = 3
        tmp_s.Set_of_pwa()
        
        tmp_s.wher_can_i_move()
        tmp_s.tr.append('D')

        A.append(tmp_s)
        tmp_s = copy.deepcopy(s)

    if(s.move_[3]  == True ) : #  Now go Left
        tmp_s.board_[x][y] = 0
        tmp_s.board_[x][y-1] = 3
        tmp_s.Set_of_pwa()

        tmp_s.wher_can_i_move()
        tmp_s.tr.append('L') 

        A.append(tmp_s)
        tmp_s = copy.deepcopy(s)

    return A

class Tree_Search:


    # def __init__(self) -> None:
    #     pass
        
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

    def BFS_(self,A:Stat) -> None: #  BFS ==> fringe : Queue
        
        # INT the Stat 
        A.wher_can_i_move()
        
        A.show_()
        print()

        # 'F' is INT(first) fringe
        F = action_in_this_stat(A) 
        fring = F
       
        while(True):
            
            #!(Stap 1)
            if(len(fring) == 0):
                
                print('): No solo :(')
                return 
                
            else:
                
                #!(Stap 2)
                cur_stat = fring.pop(0)
                
                #!(Stap 3)
                if(cur_stat.Is_goal_stat()):
                    print(" ^__^ < yes > ^__^ : ",end='')
                    print(cur_stat.tr)
                    print('len(tr): ',len(cur_stat.tr) )
                    return
               
                #!(Stap 4)
                else:
                    gg = action_in_this_stat(cur_stat)
                    for j in gg:
                        fring.append(j)

    # ! (: Can use it ? :)
    def DFS_(self,A:Stat)-> None:#  BFS ==> fringe : Stack
         
        # INT the Stat 
        A.wher_can_i_move()
        
        A.show_()
        print()

        # 'F' is INT(first) fringe
        F = action_in_this_stat(A) 
        fring = F
       
        while(True):
            
            #!(Stap 1)
            if(len(fring) == 0):
                
                print('): No solo :(')
                return 
                
            else:
                
                #!(Stap 2)
                cur_stat = fring.pop(0)
                
                #!(Stap 3)
                if(cur_stat.Is_goal_stat()):
                    print(" ^__^ < yes > ^__^ : ",end='')
                    print(cur_stat.tr)
                    print('len(tr): ',len(cur_stat.tr) )
                    return
               
                #!(Stap 4)
                else:
                    gg = action_in_this_stat(cur_stat)
                    for j in gg:
                        fring.insert(0,j)


if __name__ == '__main__':

    B = [
            #col 0 1 2 3 4 5
                [3,0,0,1,0,0], # Row 0
                [0,1,0,1,0,0], # Row 1
                [0,1,0,0,0,0], # Row 2
                [0,1,1,1,1,1], # Row 3
                [0,0,0,0,0,0], # Row 4
                [1,1,1,1,1,2], # Row 5
             ]

    Start_stat = Stat()

    Start_stat.INT_Set_board(B)

    A = Tree_Search()
    A.BFS_(Start_stat)
