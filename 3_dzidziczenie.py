# Dziedziczenie
# schemat:
# class Parent:
#     <instrukcje>
# class Child(Parent):
#     <instrukcje>
# Poniżej prosty przykład, w którym klasa bazową jest klasa User, klasą dziedziczącą Programmer.
# Klasa Programmer dziedziczy wszystkie metody po klasie User, a dodatkowo ma swoją własną metodę work().

class User:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def mainInformation(self):
        dict_ = {'first name': self.fname, 'last name': self.lname}
        return dict_


class Programmer(User):
    def work(self):
        print("Programming Python")


dev = Programmer('Łukasz', 'Kowalski')
dev.mainInformation()
dev.work()

# Za pomocą metody isistance() można sprawdzić, czy obiekt dev jest instancją klasy User:
# isinstance(dev, Programmer)
isinstance(dev, User)
isinstance(dev, Programmer)

# Dodatkowe pole w klasie dziedziczące i metoda super()
print('\n---------------------------------\n')


# Chcielibyśmy, żeby klasa dziedzicząca przyjmowała dodatkowe pole language, którego nie ma w klasie User.
# Użyjemy metody super(), dzięki której będziemy mogli odwołać się do konstruktora klasy bazowej.
# Za pomocąsuper() wywołujemy medotę z klasy nadrzędnej. W klasie Programmer wykorzystamy super()
# również do zaktualizowania metody mainInformation(). Piertwotna metoda mainInformation() została
# przysłonięta przez metode o tej samej nazwie.

class User:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def mainInformation(self):
        dict_ = {'first name': self.fname, 'last name': self.lname}
        return dict_


class Programmer(User):
    def __init__(self, fname, lname, languages):
        super().__init__(fname, lname)
        self.languages = languages

    def mainInformation(self):
        dict_ = super().mainInformation()
        dict_['languages'] = self.languages
        return dict_

    def work(self):
        print(f"Programming {self.language}")


front = Programmer('Joanna', 'Kowalska', ['Python', 'Java'])
print(front.mainInformation())

# front.work()

# Dziedziczenie wielu klas
#
# schemat1:
# class Parent1:
#       <instrukcje>
# class Parent2:
#       <instrukcje>
# class Parentn:
#       <instrukcje>
# class Child(Parent1, Parent2, ..., Parentn):
#       <instrukcje>
#
# Klasa Child z powyższego schamatu odziedziczyła wszystkie metody i pola po każdej klasie Parent
# Rozbudujemy wcześniejszy przykład. Każdy z Programistów, może mieć swoje zainteresowania. Dodajmy dodatkową
# klasę bazową, po której również będą dziedziczyć Programiści
print('\n---------------------------------\n')


class User:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def mainInformation(self):
        dict_ = {'first name': self.fname, 'last name': self.lname}
        return dict_


class Hobby:
    def __init__(self, hobby, hours):
        self.hobby = hobby
        self.hours = hours

    def kind_of_hobby(self):
        dict_hobby = {'hobby': self.hobby, 'hours_spent': self.hours}
        return dict_hobby


class Programmer(User, Hobby):
    def __init__(self, fname, lname, hobby, hours, languages):
        self.fname = fname
        self.lname = lname
        self.hobby = hobby
        self.hours = hours
        self.languages = languages

    def mainInformation(self):
        dict_ = super().mainInformation()
        dict_['languages'] = self.languages
        dict_hobby = super().kind_of_hobby()
        dict_.update(dict_hobby)
        return dict_

    def work(self):
        print(f"Programming {self.languages}")


front = Programmer('Anna', 'Kowalska', 'Pacman', 10, 'JavaScript')
front.mainInformation()

print('Czy obiekt front jest obiektem klasy User:')
print(isinstance(front, User))
print('Czy obiekt front jest obiektem klasy Hobby:')
print(isinstance(front, Hobby))
print('Czy obiekt front jest obiektem klasy Programmer:')
print(isinstance(front, Programmer))


# Wielokrotne (liniowe) dziedziczenie c.d.
#
#  class GrandParent:
#         <instrukcje>
# class Parent(GrandParent):
#         <instrukcje>
# class Child(Parent):
#         <instrukcje>
#
# Klasa Child z powyższego schamatu odziedziczyła wszystkie metody i pola po klasie Parent oraz po klasie GrandParent.
print('\n---------------------------------\n')

class Dziadek:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw(self):
        print(f'Nasze nazwisko to {self.nazwisko}')


class Rodzic(Dziadek):
    def co_robi(self):
        print('Pracuje!!!')


class Dziecko(Rodzic):
    def popros_o_kieszonkowe(self):
        print('Bardzo proszę o kieszonkowe')

    def co_robi(self):
        print('Uczy się przecież')


dziecko = Dziecko('Jaś', 'Kowalski')
rodzic = Rodzic('Adam', 'Kowalski')
dziadek = Dziadek('Zygryd', 'Kowalski')

print('wywolanie metody przedstaw() na wszystkich obiektach:')
dziecko.przedstaw()
rodzic.przedstaw()
dziadek.przedstaw()

print('\nwywolanie metody co_robi na rodzicu i dziecku:')
print(dziecko.imie)
dziecko.co_robi()
rodzic.co_robi()

print('\nCzy obiekt dziecko jest obiektem klasy Dziadek:')
print(isinstance(dziecko, Dziadek))
print('Czy obiekt dziecko jest obiektem klasy Rodzic:')
print(isinstance(dziecko, Rodzic))
print('Czy obiekt rodzic jest obiektem klasy Dziadek:')
print(isinstance(rodzic, Dziadek))