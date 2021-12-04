def ATMFunc():
    print("Select a function: ")
    print("1. Withdrawal")
    print("2. Balance")
    
    function_select=int(input("Enter your number: "))

    balance=10000
    if function_select == 1:
        withdrawal_amount= int(input("How much will you like to withdraw : "))
        print("You are have withdrawed",withdrawal_amount,"Your current balance is",balance-withdrawal_amount)
    elif function_select == 2:
        print("You have",balance,"in your account")

card_number=int(input("Enter your Card Number: "))
pin_number=int(input("Enter your Pin Number: "))

if card_number == 5 & pin_number == 4:
    ATMFunc()
else:
    ATMFunc()
 
