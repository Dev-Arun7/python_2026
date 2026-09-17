avery = {
"name" : "Avery",
"acc_no" : 12455,
"bal" : 100,
"pass" : "avery@123"
}


def show_profile():
  print("User Profile")
  print(avery)

def show_bal():
    print("Show Balance")
    acc_no = int(input("Enter A/C No: "))
    if acc_no == avery["acc_no"]:
      bal = avery["bal"]
      print("Balance: ", bal)
    else:
      print("Invalid A/C No.")

def add_money():
  print("Add Money")
  acc_no = int(input("Enter A/C No: "))
  if acc_no == avery["acc_no"]:
    amount = int(input("Enter amount to add: "))
    avery["bal"] += amount
    print("New balance: ", avery["bal"])
  else:
    print("Invalid A/C No.")

def change_pass():
  print("Change Password")
  current_pass = input("Enter you current password: ")
  if current_pass == avery["pass"]:
    new_pass = input("Enter new password: ")
    avery["pass"] = new_pass
    print("Password updated", avery["pass"])
  else:
    print("wrong pass")

def quit():
  print("Quiting...")
  print("Thanks for using bank")

print("""
1. Show user profile
2. Show Balance
3. Add money
4. Change password
5. Quit
""")



while True:
  
  menu = int(input("Enter menu: "))
  
  match menu:
    case 1:
      show_profile()
    case 2:
      show_bal()
    case 3:
      add_money()
    case 4:
      change_pass()
    case 5:
      quit()
      break
    case _:
      print("Invalid entry!")