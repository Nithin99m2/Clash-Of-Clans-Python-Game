from colorama import Fore, Back, Style 
from os import system
import random
from time import sleep,time
import math
from King import king
from getinput import get_input



class Board():

    def __init__(self):
        self.cols = 200
        self.rows = 40
       
        self.bg_pixel = Back.BLACK+' '+Style.RESET_ALL
        self.tw_pixel = Back.RED+' '+Style.RESET_ALL
        self.wa_pixel = Back.YELLOW+' '+Style.RESET_ALL
        self.hu_pixel = Back.MAGENTA+' '+Style.RESET_ALL
        self.ca_pixel = Back.GREEN+' '+Style.RESET_ALL
        self.ki_pixel = Back.BLUE+' '+Style.RESET_ALL
        self.ij_pixel = Back.CYAN+' '+Style.RESET_ALL
        self.v1x=random.randint(11,13)
        self.v1y=random.randint(60,70)
        self.v2x=random.randint(11,13)
        self.v2y=random.randint(130,150)
        self.v3x=random.randint(25,27)
        self.v3y=random.randint(60,70)
        self.v4x=random.randint(25,27)
        self.v4y=random.randint(130,150)
        self.v5x=random.randint(6,10)
        self.v5y=random.randint(99,105)
        self.c1x=random.randint(6,7)
        self.c1y=random.randint(50,52)
        self.c2x=random.randint(6,7)
        self.c2y=random.randint(160,161)
        self.w1x=int((self.rows/2)-4)
        self.w1y=int((self.cols/2)-9)
        self.w2x=int((self.rows/2)-4)
        self.w2y=int((self.cols/2)+4)
        self.w3x=int((self.rows/2)-5)
        self.w3y=int((self.cols/2)-9)
        self.w4x=int((self.rows/2)+4)
        self.w4y=int((self.cols/2)-9)
        self.k1y=100
        self.gib=[]
        self.big=[]
        self.arrx=[self.v1x,self.v2x,self.v3x,self.v4x,self.v5x,self.c1x,self.c2x]
        self.arry=[self.v1y,self.v2y,self.v3y,self.v4y,self.v5y,self.c1y,self.c2y]
        self.temp=[self.ca_pixel,self.wa_pixel, self.tw_pixel,self.bg_pixel]
        self.hehe=[self.tw_pixel,self.wa_pixel,self.hu_pixel,self.bg_pixel]
        self.temp1=[self.ij_pixel,self.wa_pixel, self.tw_pixel,self.bg_pixel]
        self.bb=[]
        self.bb1=[]
        for i in range(51):
            self.bb.append(self.temp)
            self.bb1.append(self.temp1)



        


       

        self.k1x=35
        self.king=king(self.k1x,self.k1y)

        
        self.render()

    
    def render(self):
        system('clear')
        self.board = [[self.bg_pixel for i in range(self.cols)] for j in range(self.rows)]
        

        
    
        # print("\n".join(["".join(row) for row in self.board]))
        # print("\n")

        li=[]

        townhallx=self.rows/2
        townhallx=townhallx-2
        townhallx=int(townhallx)
        # print(townhallx)


        townhally=self.cols/2
        townhally=int(townhally-4)
        # print(townhally)

        for i in range(4):
            for j in range(3):
                self.board[townhallx+i][townhally+j]=self.hehe[self.king.rr]
                self.gib=self.gib+[townhallx+i]
                self.big=self.big+[townhally+j]
                
                
        for i in range(8):
            for j in range(1):
                self.board[self.w1x+i][self.w1y+j]=self.bb[7+i][self.king.ff[7+i]]
                self.arrx=self.arrx+[self.w1x+i]
                self.arry=self.arry+[self.w1y+j]




        for i in range(8):
            for j in range(1):
                self.board[self.w2x+i][self.w2y+j]=self.bb[15+i][self.king.ff[15+i]]
                self.arrx=self.arrx+[self.w2x+i]
                self.arry=self.arry+[self.w2y+j]



        for i in range(1):
            for j in range(14):
                self.board[self.w3x+i][self.w3y+j]=self.bb[23+j][self.king.ff[23+j]]
                self.arrx=self.arrx+[self.w3x+i]
                self.arry=self.arry+[self.w3y+j]

            
        

       

        for i in range(1):
            for j in range(14):
                self.board[self.w4x+i][self.w4y+j]=self.bb[37+j][self.king.ff[37+j]]
                self.arrx=self.arrx+[self.w4x+i]
                self.arry=self.arry+[self.w4y+j]



        for i in range(1):
            for j in range(1):
                self.board[self.v1x+i][self.v1y+j]=self.bb[0][self.king.ff[0]]
                self.board[self.v2x+i][self.v2y+j]=self.bb[1][self.king.ff[1]]
                self.board[self.v3x+i][self.v3y+j]=self.bb[2][self.king.ff[2]]
                self.board[self.v4x+i][self.v4y+j]=self.bb[3][self.king.ff[3]]
                self.board[self.v5x+i][self.v5y+j]=self.bb[4][self.king.ff[4]]
                self.board[self.c1x+i][self.c1y+j]=self.bb1[0][self.king.ff[5]]
                self.board[self.c2x+i][self.c2y+j]=self.bb1[1][self.king.ff[6]]
                
    
        
        for i in range(1):
            for j in range(1):
                self.board[self.king.k_x+i][self.king.k_y+j]=self.king.i_pixel
                
        

        
       


               
                

        print("\n".join(["".join(row) for row in self.board]))
        print("\n")




        # for i in range(10):
        #     li.append(self.bg_pixel)
            
        
        # print("\n".join(["".join(row) for row in li]))


    

   