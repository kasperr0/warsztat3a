class Customer:
    def __init__(self, first, last, kwota):
        self.first = first
        self.last = last
        self.fullname = first + ' ' + last
        self.kwota = kwota

    # Metoda klasy
    def promotion(self):
        self.bonus = self.kwota * 0.1
        return '{0}: {1}'.format(self.fullname, self.bonus)


customer_1 = Customer('Karolina', 'Nowacka', 2000)
# Wywołanie metody:
print('Wywolanie metody promotion():')
print(customer_1.promotion())

# Metoda __init__ (konstruktor):
# Metoda __init__ jest wywoływana w momencie tworzenia instancji obiektu.
# zazwyczaj jest ona używana za zainicjalizownia obiektu (np przypisania wartoci
# do pól itp.).
print('\n---------------------------------\n')


class ClassWithInitMethod:
    def __init__(self, one, two):
        self.fname = one
        self.sname = two


print('ClassWithInitMethod:')
object_1 = ClassWithInitMethod("Michał", "Ok")
print(object_1.fname, object_1.sname)


class ClassWithoutInitMethod:
    def names(self, one, two):
        self.fname = one
        self.sname = two


print('ClassWithoutInitMethod:')
object_2 = ClassWithoutInitMethod()
# print(object_2.fname, object_2.sname) # <- mentorze, odkomentuj, gdy przyjdzie pora i wytłumacz :-)
object_2.names("Michał", "Ok")
print(object_2.fname, object_2.sname)

# Modyfikacja dostępu:
print('\n---------------------------------\n')


class Customer:
    def __init__(self):
        self.name = "Adam"  # regular field
        self.__nrrachunku = "1234567890"  # "mangled" by python interpreter
        self._saldo = 10000  # (not very) private (python way of private)

    def get_nrrachunku(self):
        return self.__nrrachunku


cust = Customer()
# wypisujemy name
print('name:')
print(cust.name)

# wypisujemy saldo
print('saldo:')
cust._saldo = 9
print(cust._saldo)

# wypisujemy __nrrachunku (odkomentuj ponizsze linie i zobacz co sie stanie)
# print('__nrrachunku:')
# print(cust.__nrrachunku) # <- blad

print('cust.__dict__:')
print(cust.__dict__)
print('get_nrrachunku():')
print(cust.get_nrrachunku())

# Cechy specjalne: str , dict, repr:
print('\n---------------------------------\n')


class Client:
    # tworzymy atrybut klasy
    account_count = 0

    def __str__(self):
        return "Client class Object"

    def __repr__(self):
        return "Client class repr method."

    # tworzymy metodę klasy i atrybuty instancji klasy wewnątrz metody
    def open_account(self, name, surname, age):
        print("Rachunek otwarty")
        self.name = name
        self.surname = surname
        self.age = age
        Client.account_count += 1


client_b = Client()
print(client_b)
print(repr(client_b))

# ogolnie roznica miedzy metodami __str__ i __repr__ polega na tym, ze str powinna
# zwracac opsi obiektu w formie przystepnej dla czlowieka a repr w formie
# przystepnej dla maszyny
class Customer:
    def __init__(self, first, last, kwota):
        self.first = first
        self.last = last
        self.fullname = first + ' ' + last
        self.kwota = kwota

    # Metoda klasy
    def promotion(self):
        self.bonus = self.kwota * 0.1
        return '{0}: {1}'.format(self.fullname, self.bonus)


customer_1 = Customer('Karolina', 'Nowacka', 2000)
# Wywołanie metody:
print('Wywolanie metody promotion():')
print(customer_1.promotion())

# Metoda __init__ (konstruktor):
# Metoda __init__ jest wywoływana w momencie tworzenia instancji obiektu.
# zazwyczaj jest ona używana za zainicjalizownia obiektu (np przypisania wartoci
# do pól itp.).
print('\n---------------------------------\n')


class ClassWithInitMethod:
    def __init__(self, one, two):
        self.fname = one
        self.sname = two


print('ClassWithInitMethod:')
object_1 = ClassWithInitMethod("Michał", "Ok")
print(object_1.fname, object_1.sname)


class ClassWithoutInitMethod:
    def names(self, one, two):
        self.fname = one
        self.sname = two


print('ClassWithoutInitMethod:')
object_2 = ClassWithoutInitMethod()
# print(object_2.fname, object_2.sname) # <- mentorze, odkomentuj, gdy przyjdzie pora i wytłumacz :-)
object_2.names("Michał", "Ok")
print(object_2.fname, object_2.sname)

# Modyfikacja dostępu:
print('\n---------------------------------\n')


class Customer:
    def __init__(self):
        self.name = "Adam"  # regular field
        self.__nrrachunku = "1234567890"  # "mangled" by python interpreter
        self._saldo = 10000  # (not very) private (python way of private)

    def get_nrrachunku(self):
        return self.__nrrachunku


cust = Customer()
# wypisujemy name
print('name:')
print(cust.name)

# wypisujemy saldo
print('saldo:')
cust._saldo = 9
print(cust._saldo)

# wypisujemy __nrrachunku (odkomentuj ponizsze linie i zobacz co sie stanie)
# print('__nrrachunku:')
# print(cust.__nrrachunku) # <- blad

print('cust.__dict__:')
print(cust.__dict__)
print('get_nrrachunku():')
print(cust.get_nrrachunku())

# Cechy specjalne: str , dict, repr:
print('\n---------------------------------\n')


class Client:
    # tworzymy atrybut klasy
    account_count = 0

    def __str__(self):
        return "Client class Object"

    def __repr__(self):
        return "Client class repr method."

    # tworzymy metodę klasy i atrybuty instancji klasy wewnątrz metody
    def open_account(self, name, surname, age):
        print("Rachunek otwarty")
        self.name = name
        self.surname = surname
        self.age = age
        Client.account_count += 1


client_b = Client()
print(client_b)
print(repr(client_b))

# ogolnie roznica miedzy metodami __str__ i __repr__ polega na tym, ze str powinna
# zwracac opsi obiektu w formie przystepnej dla czlowieka a repr w formie
# przystepnej dla maszyny
