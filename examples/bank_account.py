class BankAccount:
    def __init__(self, bank_name=None, balance=0):
        self.bank_name = bank_name or "bank 0"
        self.balance = balance

    def __str__(self):
        return f"{self.__class__.__name__} instance ({self.bank_name}, {self.balance})"


ba = BankAccount()
print(ba.bank_name, ba.balance)

ba1 = BankAccount("Banca mea", 163653)
print(ba1.bank_name, ba1.balance)

ba1.bank_name = "New Bank Name"
print(ba1.bank_name, ba1.balance)

print(ba)
str_representation = str(ba)
print(str_representation)

# ba += 100
