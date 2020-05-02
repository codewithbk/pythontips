user_input = input("Enter a tuple like this 1234: ")
if user_input:
  l = list(user_input)
  l.reverse()
  t=tuple(l)
  print(t)
else:
  print("Opps something gont wrong. ")
