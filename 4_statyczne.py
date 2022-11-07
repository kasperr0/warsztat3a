# Metody i atrybuty statyczne
#
# Metoda statyczna, to taka metoda, która może być wywołana bez tworzenia instancji obiektu.
# Taka metoda nie ma oczywiście dostępu do pól instancji (bo instancja nie istnieje!).
# Atrybut statyczny, to atrybut przypisany do klasy a nie do
# instancji klasy.
#
# Przykład użycia:

class Account:
    account_number_length = 10

    def __init__(self, number, initial_balance):
        self.number = number
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    @staticmethod
    def print_info():
        print("Account is an arrangement made with a bank whereby one may deposit and withdraw money")

# powołujemy nowy obiekt klasy Account
new_account = Account(123467890, 666)

# zwróć uwagę, że w poniższych przykładach nie używamy obiektu new_account, a odwołujemy sie bezpośrednio do klasy
print(Account.account_number_length)
Account.print_info()
