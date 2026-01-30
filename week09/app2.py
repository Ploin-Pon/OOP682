from models.bankaccount import BankAccount

my_account = BankAccount(1000)
your_account = BankAccount(1500)

our_account = your_account + my_account

print(our_account)