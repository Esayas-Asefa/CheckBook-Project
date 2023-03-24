def myFunction():
  # When run, the application should welcome the user
  print(
"""
~~~ Welcome to your terminal checkbook! ~~~

What would you like to do?

1) view current balance
2) record a debit (withdraw)
3) record a credit (deposit)
4) exit"""
)
  def bal(float):
    float(bal)


  def deposit(acct):
    amount = float(input("Enter amount to be deposited: "))
    acct.bal += amount
 

  def withdrawal():
    amount = 1
    d = float(input("Enter mount to be withdrawn: " ))
    if d.bal >= amount or d.bal <= amount:
      print("\n You Withdrew:", amount)
    else:
      print("\n Insufficient Balance ")

  #
  # prompt them for an action to take:
  userChoice = int(input("Your choice? "))
  print(userChoice)
  # view current balance 
  while True:
    if userChoice == 1:
      print("View current balance")
      with open('my_new_file.txt', 'r') as f:
          data = f.readline()
          
          print("Your current balance is: $", data)

      break
  
  # add a debit (withdrawal) 
    elif userChoice == 2:

      user = input('Enter Desired Amount')
      with open('my_new_file.txt', 'r') as f:
          data = f.readline()
          
          print("Your current balance is: $", data)

          with open('my_new_file.txt', 'w') as f:
            print(data)
            new_value = float(data)
            new_amount = new_value - float(user)
            f.write(str(new_amount))

  
  # add a credit (deposit)
    elif userChoice == 3:
      user = input('Enter Deposit Amount')
      with open('my_new_file.txt', 'r') as f:
          data = f.readline()
          
          print("Your current balance is: $", data)

          with open('my_new_file.txt', 'w') as f:
            print(data)
            new_value = float(data)
            new_amount = new_value + float(user)
            f.write(str(new_amount))
  


  # exit
    elif userChoice == 4:
      print("Exit")
      print("Have a nice day")

    else:
      print("Please make a selection from the above options")

    break

myFunction()
