import time
from random import randint
import random
from time import sleep
import curses
import os
import sys
def clear():
  curses.setupterm()
  e3 = curses.tigetstr('E3') or b''
  clear_screen_seq = curses.tigetstr('clear') or b''
  os.write(sys.stdout.fileno(), e3 + clear_screen_seq)



#

bright_black = "\033[0;90m"
bright_red = "\033[0;91m"
bright_green = "\033[0;92m"
bright_yellow = "\033[0;93m"
bright_blue = "\033[0;94m"
bright_magenta = "\033[0;95m"
bright_cyan = "\033[0;96m"
bright_white = "\033[0;97m"



def r1():
  print(""" 
  
  
  
  
                /\   
               (  )   
               (  )   
              /|/\|\   
             /_||||_\ """)



def r2():
  print(""" 


                
                /\   
               (  )   
               (  )   
              /|/\|\   
             /_||||_\  
                      """)





def r3():
  print(""" 


                /\   
               (  )   
               (  )   
              /|/\|\   
             /_||||_\ 
                      
                      """)



def r4():
  print(""" 

                /\   
               (  )   
               (  )   
              /|/\|\   
             /_||||_\
              
              
                   """)


def r5():
  print(""" 
                /\   
               (  )   
               (  )   
              /|/\|\   
             /_||||_\ 


                      
                      """)


def r6():
  print(bright_yellow + """     
         \         .  ./
      \      .:";'.:.."   /
           (M^^.^~~:.'").
      -   (/  .    . . \ \)  -    *BOOM!
         ((| :. ~ ^  :. .|))
     -   (\- |  \ /  |  /)  -
          -\  \     /  /-
            \  \   /  /
 


                      
                      """)




def countdown(n) :
  while n > 0:
    print(n)
    time.sleep(1)
    n -= 1
    if n == 0:
      clear()



countdown(10)
r1()
sleep(1)
clear()
r2()
sleep(0.9)
clear()
r3()
sleep(0.8)
clear()
r4()
sleep(0.7)
clear()
r5()
sleep(0.6)
clear()
r6()



