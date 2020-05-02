user_input = input("Enter how many time you run these ")
temp = []
if user_input.isnumeric():
  for i in range(1, int(user_input) + 1):
    user_input_1 = input(f"Enter your {i} item ")
    if user_input_1:
      temp.append(user_input_1)
    else:
      temp.append("null")
  unique = set(temp)
  l = list(unique)
  user_input_2 = input("how you represent you input \n 1 to list 2 to line ")
  if user_input_2 and user_input_2 == "1":
    print(l)
  elif user_input_2 and user_input_2 == "2":
    for i in l:
      print(i)
  else:
    print("opps something went wrong!")
else:
  print("Opps something went wrong")
