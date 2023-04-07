# investment app
# user adds Name
# application return 50% profit on capital
# user enter withdrawal amount
# user get a failed transaction if input amount is higher than amount balance
# user get credited if input amount is lower than account balance
# application get 7% services charge from account balance.

# investment app
profit_percentage = 50
vat_percentage = 7

def investment():
    Account_name = (input('enter your account name: '))
    print('Welcome', Account_name, 'to cohort4 investment application')
    wallet =  int(input('enter your investment amount here: N'))
    wallet_balance = wallet * (1 + (profit_percentage / 100))
    print(Account_name, 'your wallet have been credited with the sum of: ','N', wallet_balance, 'with  a 50% interest on your capital')
    withdrawal_amount = int(input('enter amount you want to withdraw: N'))
    if withdrawal_amount >= wallet_balance:
       print(Account_name, 'your transaction failed due to insufficient fund')
    else:
        final_wallet_balance = wallet_balance - withdrawal_amount
        final_balance = final_wallet_balance * (1 + (vat_percentage /100))
        print(Account_name, 'your withdrwal transaction was succesful and your account has been debited with:', 'N', withdrawal_amount, 'and a 7% service charge has been deducted and ','your final_balance is:', 'N', final_balance )



investment()