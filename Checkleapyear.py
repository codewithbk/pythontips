year = input("Enter your year ")
if year.isnumeric() and year:
  year = int(year)
  if (year % 4) == 0:
    if (year % 100) == 0:
      if (year % 400) == 0:
        print("{0} is a leap year".format(year))
      else:
        print("{0} is not a leap year".format(year))
    else:
      print("{0} is a leap year".format(year))
  else:
    print("{0} is not a leap year".format(year))
else:
  print("Opp,s something went wrong")
