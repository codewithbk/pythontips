import string
import random
import time
import curses
import os
import sys

print('Hey there press \'h\' to more help \n and press any key to continue !')
time.sleep(1)

def clear():
  curses.setupterm()
  e3 = curses.tigetstr('E3') or b''
  clear_screen_seq = curses.tigetstr('clear') or b''
  os.write(sys.stdout.fileno(), e3 + clear_screen_seq)
  
def genpass(user_ask):
  lower_case_string = list(string.ascii_lowercase)
  upper_case_string = list(string.ascii_uppercase)
  digits = list(string.digits)
  hexadecimal = list(string.hexdigits)
  oct_digits = list(string.octdigits)
  punctuation = list(string.punctuation)
  
  blank = []
  
  blank.extend(digits)
  blank.extend(upper_case_string)
  blank.extend(lower_case_string)
  
  user_input_1 = input('\nYour password have punctuation ')
  if user_input_1:
    blank.extend(punctuation)
  user_input_2 = input('Your password have oct_digits ')
  if user_input_2:
    blank.extend(oct_digits)
  user_input_3 = input('Your password have hexadecimal ')
  clear()
  if user_input_3:
    blank.extend(hexadecimal)
  else:
    print('Opps something went wrong')
  user_ask = int(user_ask)
  return "".join(random.sample(blank, user_ask))
  

while True:
  user_input = input('Enter your password length: ')
  if user_input.isnumeric() and int(user_input) >= 124:
    print('YOU ENTER TWO LONG PLEASE ENTER 124 PRESS ENTER TO CONTINUE')
    input()
  elif user_input.isnumeric() and int(user_input) <= 5:
    a = '\n hey there Your password are two weak two make \nyour password strong increase your password length! \n'
    print(a.upper())
    time.sleep(2)
    print(f"Your password is this '{genpass(user_input)}'")
    break
  elif user_input == 'h':
    print("Hey there the some password tip here that help you to make a strong password ! There are 7 tip")
    time.sleep(1)
    print("1. MAKE YOUR PASSWORD LONG.")
    time.sleep(1)
    print("2. MAKE YOUR PASSWORD A NONSENSE PHRASE.")
    time.sleep(1)
    print("3. INCLUDE NUMBERS, SYMBOLS, AND UPPERCASE AND LOWERCASE LETTERS.")
    time.sleep(1)
    print("4. AVOID USING OBVIOUS PERSONAL INFORMATION.")
    time.sleep(1)
    print("5. DO NOT REUSE PASSWORDS.")
    time.sleep(1)
    print("6. START USING A PASSWORD MANAGER.")
    time.sleep(1)
    print("7. KEEP YOUR PASSWORD UNDER WRAPS.")
    time.sleep(1)
    print('press enter to continue')
    input()
    clear()
  elif user_input.isnumeric():
    print(f"Your password is this '{genpass(user_input)}'")
    break
  else:
    print('Opps something went wrong!')
    input()
