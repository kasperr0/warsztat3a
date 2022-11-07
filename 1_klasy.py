# Tworzymy klasę Client
class Client:
    # tworzymy atrybuty klasy
    name = "Adam"
    surname = "Kowalski"
    age = 25

    # tworzymy metody klasy
    def open_account(self):
        print("Otwieram rachunek")

    def cloese_account(self):
        print("Zamykam rachunek")


# Klasa vs Instancja klasy

# Client jest klasą (typem obiektu), client1 jest instancją klasy:
client1 = Client()
print('Obiekt client1 jest instancja klasy:')
print(type(client1))

# Wszystkie atrybuty i metody obiektu client1:
print('Wszystkie atrybuty i metody obiektu client1:')
print(dir(client1))


# Atrybuty klasy vs atrybytu obiektu
class Client:
    # tworzymy atrybut klasy
    account_count = 0

    # tworzymy metodę klasy i atrybuty instancji klasy wewnątrz metody
    def open_account(self, name, surname, age):
        print("Rachunek otwarty")
        self.name = name
        self.surname = surname
        self.age = age
        Client.account_count += 1


# Wszystkie atrybuty i metody obiektu client1:
print('Wszystkie atrybuty i metody obiektu client1:')
print(dir(client1))


# Atrybuty klasy vs atrybytu obiektu
class Client:
    # tworzymy atrybut klasy
    account_count = 0

    # tworzymy metodę klasy i atrybuty instancji klasy wewnątrz metody
    def open_account(self, name, surname, age):
        print("Rachunek otwarty")
        self.name = name
        self.surname = surname
        self.age = age
        Client.account_count += 1


print('\n---------------------------------\n')
# Tworzymy dwa obiekty klasy Client i wypisujemy ich atrybuty obiektu oraz atrybut klasy: account_count
client_a = Client()
client_a.open_account("Jan", "Nowak", 35)
print(client_a.name)
print(client_a.account_count)

client_b = Client()
client_b.open_account("Agnieszka", "Nowak", 34)
print(client_b.name)
print(client_b.account_count)
