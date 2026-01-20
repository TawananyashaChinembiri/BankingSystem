# For a sample banking system in Python using classes and functions, here are some possible features you might consider implementing:
#
# ### Core Features
#
# 1. **Account Management**:
#    - Create an account (e.g., `create_account` function).
#    - View account details (e.g., `view_account` function).
#    - Close an account (e.g., `close_account` function).
#
# 2. **Transaction Management**:
#    - Deposit funds (e.g., `deposit` function).
#    - Withdraw funds (e.g., `withdraw` function). NB Withdrawals have 2% tax
#    - Transfer funds between accounts (e.g., `transfer` function).
#
# 3. **Balance Inquiry**:
#    - Check account balance (e.g., `check_balance` function).
#
# 4. **Authentication**:
#    - User login/logout functionality.
#    - Validate user credentials before performing transactions.
#
# ### Additional Features
#
# 1. **Account Types**:
#    - Saving accounts with interest calculations.
#    - Checking accounts with overdraft facilities.
#
# 2. **Transaction History**:
#    - Record all transactions for an account (e.g., `transaction_history` method).
#
# 3. **Interest Calculation**:
#    - Calculate interest on savings accounts periodically.
#
# 4. **User Interface**:
#    - Command-line interface for user interactions.
#    - Menu-driven options for easy navigation.
#
# 5. **Error Handling**:
#    - Handle insufficient funds for withdrawals.
#    - Handle invalid account operations.
#
# 6. **Admin Features** (Optional):
#    - View all accounts and their balances.
#    - Generate reports on banking activities.
#
# 7. **Data Persistence**:
#    - Save account details and transaction history to a file (e.g., CSV or JSON) for
#       persistence.
#    - Load data from the file when the system starts.
#
# ### Example Class Structure

# this class is responsible for managing the user accounts of the account holders
import time
class UserAccounts():
    accounts_count = 0
    def __init__(self, first_name, last_name, password, balance=0):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.balance = round(balance, 2)
        self.acc_id = self.generate_acc()


    def __repr__(self):
        return print(F'\nAccount ID: {self.acc_id} \nFirst Name: {self.first_name} \nLast Name: {self.last_name} \nBalance: {self.balance} \n')

    # generating an account number
    def generate_acc(self):
        UserAccounts.accounts_count += 1
        return f'BS{UserAccounts.accounts_count:05d}'

    def delete_account(self):
        pass

    def changePassword(self):
        pass

    def aunthentication(self):
        pass

# this class is responsible for the transactions in that happen within the banking system
class Transactions(UserAccounts):

    def __init__(self, transaction_id, balance, acc_id):
        super().__init__(balance, acc_id)
        self.transaction_id = transaction_id

    def __repr__(self):
        return print(f'\nTransaction ID: {self.transaction_id} \n Balance: ${self.balance} \nAccount ID: {self.acc_id}')
    def deposit(self):
        deposit_amount = float(input('Enter the deposit amount: $'))
        self.balance += deposit_amount
        return f'Your current balance is ${self.balance}'

    def withdraw(self):
        withdraw_amount = float(input('Enter withdrawal amount: $'))
        withdrawal_tax = (0.02 * withdraw_amount)
        if withdraw_amount > (self.balance + withdrawal_tax):
            print('Insufficient Funds!')
        else:
            self.balance -= (withdraw_amount + withdrawal_tax)

        return f'Your current balance is {self.balance}\n You have paid ${withdrawal_tax} tax'

    def check_balance(self):
        return f'Your current balance is ${self.balance}'

    def transfer_funds(self):
        pass

def mainMenu():
    time.sleep(2)
    print('_____________________________________________________________________________________')
    print("\n Welcome to Our Banking system")
    print('_____________________________________________________________________________________')

    print('\nPlease select option')
    print('1. Check Bank Balance\n2. Deposit Amount\n3. Withdraw Amount \n4. Tranfer Amount')
    time.sleep(1)
    option = int(input('\nPlease select option: '))

    if option == 1:
        Transactions.check_balance()
    elif option == 2:
        Transactions.deposit()
    elif option == 3:
        Transactions.withdraw()
    elif option == 4:
        Transactions.transfer_funds()
    else:
        print('Invalid option!')

mainMenu()
