import datetime
k = datetime.date.today().day
print(k)

def orac():
  fates = ["money", "love", "happiness", "hardship", "peace"]

  r = int(input("What is the date of your birthday? "))
  q = int(input("How many letters are in your name? "))

  print("You will encounter "+fates[(r+q+k)%5])

allow = ["yes", "yeah", "y", "yup", "yep"]

consent = input("do you want a fortune? ")

def tellme():
  orac()
  cont = input("do you want another? ")
  if cont in allow:
    tellme()
  else:
    print(":(")


if consent in allow:
  tellme()
else:
  print(":(")