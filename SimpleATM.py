menu_select =0
account_flag = 0
pin_flag = 0
transaction_c = 'y'

class BankAccount:
    global menu_select
    def __init__(self):
        self.name =""
        self.AN =000000
        self.PIN = 0000
        self.current =0
    def update_account(self, new_pin):
        self.account = account
    def update_pin(self, new_pin):
        self.PIN = new_pin
    def update_name(self, new_name):
        self.name = new_name
    def update_balance(self, balance):
        if menu_select == 1:
            self.current -= balance
        elif menu_select == 2:
            self.current += balance
            
##Temporary Database        
customer1 = BankAccount()
customer1.AN=12345
customer1.PIN=1234
customer1.current = 3000
customer1.name = "Hansol"
customer2 = BankAccount()
customer2.AN=23456
customer2.PIN=2345
customer2.current = 5000
customer2.name = "Bear"
Account_Database=[customer1,customer2] #Banker will be able to modify this array remotely

acc = input("\nInput 5 digit account number")

# this would be replaced with real card reading in the ATM

for i in range (len(Account_Database)):
    if Account_Database[i].AN == int(acc):
        current_customer = Account_Database[i]
        account_flag = 1
        print("Account found")
        break
if account_flag !=1:
    print("Account not found!")
    exec(open("SimpleATM.py").read())
    
Pin = input("Input 4 digit pin")
for i in range (len(Account_Database)):
    if Account_Database[i].PIN == int(Pin):
        current_customer = Account_Database[i]
        pin_flag = 1
        print("Pin Match!")
        break
if pin_flag !=1:
    print("Wrong Pin!")
    exec(open("SimpleATM.py").read())
    
while (account_flag ==1) and (transaction_c == 'y') and (pin_flag == 1):
    print("Welcome " + Account_Database[i].name +"!!")
    print("""
    Menu Options
    1. Withdraw
    2. Deposit
    3. Check Balance""")

    menu_select = int(input())

    if menu_select == 1:
        amount = float(input("How much would you like to withdraw"))
        if amount<=current_customer.current  :
            current_customer.update_balance(amount)
            Account_Database[i] = current_customer
        else:
            print("you do not have enough minerals")
        print("balance is:"+str(customer1.current))
    elif menu_select == 2:
        amount = float(input("How much would you like to deposit"))
        current_customer.update_balance(amount)
        Account_Database[i] = current_customer
        print("balance is:"+str(Account_Database[i].current))
        
    elif menu_select ==3:
        print("balance is:"+str(Account_Database[i].current))
 
  
    else:
        print("There is no button other than 1,2,3,4 in the UI")
    transaction_c = input("more transactions? (y/n)")
else:
    print("good bye")
    exec(open("SimpleATM.py").read())
