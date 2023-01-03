from multiprocessing.reduction import duplicate
from struct import unpack
import sys
from cgi import test
from ctypes import sizeof
import re
from turtle import width
import numpy as np
import tkinter
import collections
import scipy.linalg as la


#amount number generated for each difficulty
easy=38
meduim=32
hard=25 
expert=22
difficulty=easy
def system_exit():
    sys.exit()

pick=int(input("1 for easy, 2 for meduim,3 for hard ,4 for expert ,5 to exit program : "))
if pick==1:
    difficulty=easy
elif pick==2:
    difficulty=meduim
elif pick==3:
    difficulty=hard
elif pick==4:
    difficulty=expert
elif pick==5:
    system_exit()



def gui_logic():
    window = tkinter.Tk()
    window.title("9x9 grid")
    window.geometry("420x465")
    entries=[]
    c=0
    for a in range(0, 420, 47):
        for b in range(0, 840, 47):
            text1=tkinter.Button(window,text="tba",activebackground="blue",background="white")
            text1.place(x=a,y=b,width=47,height=47)
            entries.append(text1)
        c = c+1
        bttn1=tkinter.Button(window,text=c,activebackground="blue",background="white")
        bttn1.place(x=a,y=425,width=47,height=47)
        entries.append(bttn1)
    #failsafe test phase ie check numbers in check for duplcates in a row or column
    window.mainloop()

#fill x amount of text  for each difficulty 
#ie easy =38 numbers,meduim =32,hard =25 ,expert =22 
def define_numbers_in_grid(level):
    #ask the user what difficulty they wat
    #for i in range 0,4 

    difficulty = level
  

    grid = np.random.randint(1, 10, (9, 9))
    for i in range(9):
        row = grid[i, :]
        while check_for_duplicates(row):
            row = np.random.randint(1, 10)
            grid[i, :]

        column = grid[:,i]
        while check_for_duplicates(column):
           
            column[i] = np.random.choice(np.random.randint(1, 10,9))
            grid[:,i]= column
 
    return grid.flatten()
     
            



    
def check_for_duplicates(listofelems):
    # Make sure that listofelems is always a list
    if type(listofelems) != list:
        listofelems = [listofelems]

    # Call the check_for_duplicates function with the modified list
    if len(listofelems) == len(set(listofelems)):
        return False
    else:
        return True


def main():
   
    problem=[]
    define_numbers_in_grid(difficulty)
    positions = np.random.choice(81, difficulty, replace=False)
    for i in range(81): 
        if i in positions:
            print(answer[i], end=' ')
            problem.append(answer[i])
        else:
            print('_', end=' ')
    print(problem)
    print(answer)
        
    gui_logic()
while(1):
    main()