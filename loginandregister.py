import random
import os
import time
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
current_year = now.strftime("%A / %B / %A")
files = os.listdir()
path = os.getcwd()

def number():
  dirPath = path + '/' + 'User Information' + '/'
  take = os.listdir(dirPath)
  for i in len(take):
    print(str(i))


if not os.path.exists('User Information'):
  print('ERROR DATABASE BROKEN \n ! WE MAKE A DATABASE "User Information"')
  time.sleep(1)
  os.mkdir('User Information')
else:
  pass
print('You are a new member press "r"')
time.sleep(2)
print('You are a already a member press "l"')
time.sleep(1)
print('And see all memberb score press "z"')
time.sleep(2)
user_ask = input('Enter your options ')
if user_ask.lower() == 'r':
  print('\n.........Register Form :) !........\n')
  i = False
  while not i:
    user_input_1 =  input('Enter your name ')
    if len(user_input_1) < 9 and len(user_input_1) > 3:
      user_input_2 = input('Enter you password ')
      r = random.randrange(1, 700000)
      t = open(path + '/' + 'User Information' + '/' + f'{r}.txt' , 'w+')
      time.sleep(1)
      print('\n Your request are sumit we generate your PIN !')
      time.sleep(2)
      print(f"\nHey {user_input_1} You pin is {r} !")
      user = str(user_input_1) + str(user_input_2) + str(r)
      t.write(f'{len(user_input_1)}{len(user.strip())}{user_input_1.strip().lower()}{user_input_2.strip().lower()}{r} \n') 
      t.close()
      print('NOW YOU CABLE TO LOGIN :)')
      # t = open(path + '/' + 'User Information' + '/' + 'U.txt' , "r")
      # print(t.read())
      break
    else:
      print('Enter only 9 digit in name !')
      input()
elif user_ask.lower() == 'l':
  dir_path = path + '/' + 'User Information' + '/'
  i = False
  while not i:
    print('\n....LOGIN FORM..... :)\n')
    user_input_3 = input('Enter your pin and "q" to exit ! ')
    dir_path = path + '/' + 'User Information' + '/'
    total_path = os.listdir(dir_path) 
    user_input_3 = user_input_3 + '.txt'
    if user_input_3.lower().strip() == 'q.txt':
      break
    elif user_input_3.strip() in total_path:
      f = open(path + '/' + 'User Information' + '/' + f'{user_input_3}' , 'r+') 
      n = f.read()
      name = n[0]
      name = int(name) + 3 
      print(f'\nHey {n[3:name].title()}!\n')
      data = n[1:3]
      data = int(data) + 3
      # print(len(n) , data)
      
      print('\nWE LOAD YOUR DATA.....\n')
      time.sleep(2)
      print(f'\tYou win {n.count("SOURCE:  6")} Time')
      print(n[data:])
      print('\nALL DATA LOAD..')
      o = False
      print('Hey are you ready to playing game ! press any key and "q" to exit! ')
      while not o:
        user_input_4 = input('Enter any key ')
        ran = random.randrange(1, 7)   
        if user_input_4.lower().strip() == 'q':
          print('Bye')
          break
        elif user_input_4:
          if ran == 6:
            print(f'You win in game ! {ran}')
            f = open(path + '/' + 'User Information' + '/' + f'{user_input_3}' , 'a+') 
            tot = '\tSOURCE:  ' + str(ran) + '\tTIME:  ' + str(current_time) + '\tDAY:  ' + str(current_year) + '\n'
            f.write(tot)
            f.close()
            o = True
          else:
            print(f'{ran} You dice number raun again !') 
        else:
          print('Opp"s something gont wrong !')
    else:
      print('PIN WAS WRONG')



elif user_ask.lower() == 'z':
  dirPath = path + '/' + 'User Information' + '/'
  take = os.listdir(dirPath)
  for i in take:
    d = open(dirPath + '/' + i)
    g = d.read()
    d.close()
    name = g[0]
    name = int(name) + 3
    print(f'\n{g[3:name].title()}! Scource {g.count("SOURCE:  6")} ')
    if g.count("SOURCE:  6") <= 5:
      print('Brown')
    elif g.count("SOURCE:  6") <= 15:
      print('Sliver')
    elif g.count("SOURCE:  6") <= 25:
      print('Gold')
    elif g.count("SOURCE:  6") <= 35:
      print('Dimond ')
    elif g.count("SOURCE:  6") <= 55:
      print('King')
    else:
      print('No awrads')
else:
  print('Opps something gont wrong !')








