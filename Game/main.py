import random
options = ("piedra","papel","tijera")

user_option = input("piedra, papel o tijera ==>")
user_option = user_option.lower()
computer_option= random.choice(options)
print("user_option=>", user_option)
print("computer_option =>", computer_option)

if not user_option in options:
  print("No es valido")

if user_option == computer_option:
  print("Empate!!!")
elif user_option == "piedra" :
  if computer_option == "tijera" :
    print("piedra gana a tijera")
    print("gana Thiago")
  else:
    print("papel gana a piedra")
    print("computer gana")

elif user_option == "tijera" :
  if computer_option == "papel" :
    print("tijera gana a papel")
    print("gana Thiago")
  else:
    print("piedra gana a tijera")
    print("computer gana")

elif user_option == "papel":
  if computer_option == "piedra":
    print("papel gana a piedra")
    print("gana Thiago")
  else:
    print("tijera gana a papel")
    print("computer gana")