from re import X
from turtle import update
from colorama import Fore, Back, Style 
from os import system
import random

from getinput import get_input
from time import sleep,time
import math



class king():

     def __init__(self,x,y):
         self.k_x=x
         self.k_y=y
        #  print(self.k_x)
        #  print(self.k_y)
         self.rr=0
         self.ff=[]
         for i in range(51):
             self.ff.append(0)

         self.i_pixel = Back.BLUE+' '+Style.RESET_ALL
         self.g_pixel = Back.GREEN+' '+Style.RESET_ALL
         self.y_pixel = Back.YELLOW+' '+Style.RESET_ALL

         self.kar=[]
         for i in range(63):
             self.kar.append(1)
         


     def update(self,x,y):
         self.k_x=x
         self.k_y=y

    


     def move(self,board):
        d=get_input()

    
        if(d == 'd'):

            if(self.k_y<board.cols-4):
                self.k_y += 1
                for i in range(0,51):
                    if(self.kar[i]==1):
                        if(math.sqrt(((self.k_x - board.arrx[i])**2)+((self.k_y - board.arry[i])**2))<1):
                            self.k_y -=1

                for i in range(0,12):
                    if(self.kar[51+i]==1):
                        if(math.sqrt(((self.k_x - board.gib[i])**2)+((self.k_y - board.big[i])**2))<1):
                            self.k_y -=1

                    


               

                
                

        elif(d=='a'):

            if(self.k_y>0):
                self.k_y -= 1
                for i in range(0,51):
                    if(self.kar[i]==1):
                        if(math.sqrt(((self.k_x - board.arrx[i])**2)+((self.k_y - board.arry[i])**2))<1):
                            self.k_y +=1


                for i in range(0,12):
                    if(self.kar[51+i]==1):
                        if(math.sqrt(((self.k_x - board.gib[i])**2)+((self.k_y - board.big[i])**2))<1):
                            self.k_y +=1

        elif(d=='s'):

            if(self.k_x<board.rows-6):
                self.k_x += 1
                for i in range(0,51):
                    if(self.kar[i]==1):
                        if(math.sqrt(((self.k_x - board.arrx[i])**2)+((self.k_y - board.arry[i])**2))<1):
                            self.k_x -=1


                for i in range(0,12):
                    if(self.kar[51+i]==1):
                        if(math.sqrt(((self.k_x - board.gib[i])**2)+((self.k_y - board.big[i])**2))<1):
                            self.k_x -=1

 
        elif(d=='w'):

            if(self.k_x>2):
                self.k_x -= 1
                for i in range(0,51):
                    if(self.kar[i]==1):
                        if(math.sqrt(((self.k_x - board.arrx[i])**2)+((self.k_y - board.arry[i])**2))<1):
                            self.k_x +=1

                for i in range(0,12):
                    if(self.kar[51+i]==1):
                        if(math.sqrt(((self.k_x - board.gib[i])**2)+((self.k_y - board.big[i])**2))<1):
                            self.k_x +=1


        # elif(d =='x'):
        #     self.ff[i]=self.ff[i]+1
        #       for i in range(0,5):
        #         if(math.sqrt(((self.k_x - board.arrx[i])**2)+((self.k_y - board.arry[i])**2))<1):
        #             if(self.ff[i]==3):
        #                 self.kar[i]=-1
        #             if(self.ff[i]<3):
                        

        return d
        



     def attack(self,board):
          d=get_input()
           


          if(d =='x'):
              
              for i in range(0,51):
                if(math.sqrt(((self.k_x - board.arrx[i])**2)+((self.k_y - board.arry[i])**2))==1):
                   
                    if(self.ff[i]<3):
                        self.ff[i]=self.ff[i]+1
                    if(self.ff[i]==3):
                        self.kar[i]=-1
                        continue

              for i in range(12):
                  if(math.sqrt(((self.k_x - board.gib[i])**2)+((self.k_y - board.big[i])**2))==1):
                      
                      if(self.rr<3):
                          self.rr=self.rr+1

                      if(self.rr==3):
                          for j in range(12):
                              self.kar[51+j]=-1
                          
                          continue





                       
                    


    
          


                  








        


            

        


            
            

            
            # self.board[self.k_x][self.k_y+10]=self.g_pixel
            # self.board[self.k_x][self.k_y+1]=self.i_pixel
        




    

