from bank_accounts import BankAccount, InterestRewardsAccount, SavingsAccount

Itminan = BankAccount("Itminan", 10000)
Mafi = BankAccount("Mafi", 15000)

Itminan.deposit(5000)
Mafi.withdraw(20000)
Mafi.withdraw(300)

Itminan.transfer(300, Mafi)
Mafi.transfer(20000, Itminan)
Mafi.transfer(20000, Mafi)
Mafi.transfer(10000, Mafi)

Fuad = InterestRewardsAccount("Fuad", 10000)
Fuad.get_balance()
Fuad.deposit(10000)
Fuad.transfer(1000, Itminan)

Anik = SavingsAccount("Anik", 10000)
Anik.transfer(10000, Fuad)
Anik.get_balance()
