while True:
  user_input = input("Enter a number ")
  if user_input.isnumeric():
    print(f'{user_input} square root is {int(user_input)**2}\n')
  else:
    print('opps try again\n')
    user_input = input("Try again "u
    print(f'{user_input} square root is {int(user_input)**2}\n')if user_input.isnumeric() else print('opp you enter w rong !\n')
