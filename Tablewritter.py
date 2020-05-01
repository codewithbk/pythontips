user_input_1 = input("Enter you number ")
user_input_2 = input("Enter how many time you run this ")
if user_input_1.isnumeric() and user_input_2.isnumeric():
  for i in range(1, int(user_input_2) + 1):
    print(f'{user_input_1} * {i} = {int(user_input_1) * i}')
else:
  print("Opps something went wrong!")
