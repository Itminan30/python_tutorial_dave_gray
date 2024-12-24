class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, account_name, initial_balance):
        self.name = account_name
        self.balance = initial_balance
        print(f"\nAccount '{self.name}' has been created.\nBalance: ${self.balance:.2f}")

    def get_balance(self):
        print(f"\nAccount '{self.name}' balance: ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print("\nDeposit complete.")
        self.get_balance()

    def viable_transaction(self, amount):
        if amount > self.balance:
            raise BalanceException(f"\nAccount '{self.name}' only has balance of ${self.balance:.2f}.")
        else:
            return

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance -= amount
            print("\nWithdraw complete.")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")

    def transfer(self, amount, account):
        try:
            print("\n**********")
            print("\n\nTransfer started.. 🚀")

            self.viable_transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)

            print("\nTransfer complete! ✅")
            print("\n\n**********")
            self.get_balance()
        except BalanceException as error:
            print(f"\nTransfer interrupted: ❌ {error}")

class InterestRewardsAccount(BankAccount):
    def deposit(self, amount):
        self.balance += (amount * 1.05)
        print("\nDeposit complete.")
        self.get_balance()

class SavingsAccount(InterestRewardsAccount):
    def __init__(self, account_name, initial_balance):
        super().__init__(account_name, initial_balance)
        self.fee = 5

    def viable_transaction(self, amount):
        if (amount + self.fee) > self.balance:
            raise BalanceException(f"\nAccount '{self.name}' only has balance of ${self.balance:.2f}.")
        else:
            return

    def withdraw(self, amount):
        try:
            self.viable_transaction((amount + self.fee))
            self.balance -= (amount + self.fee)
            print("\nWithdraw complete.")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")