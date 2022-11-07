# Zadanie (15 minut)
#
# Studenci wybierają się na wycieczkę. Każdy ma okresloną ilość pieniędzy zapisaną jak w definicji klasy poniżej
# (ilość banknotów o nominale 5, 10 i 20). Twoim zadaniem jest napisanie funkcji most_money, która zwróci tablicę
# imion studentów z największą ilością pieniędzy.

class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties

    def __repr__(self):
        return f"Student(\"{self.name}\", {self.fives}, {self.tens}, {self.twenties})"


def most_money(student_list):
    pass


phil = Student("Phil", 2, 2, 1)
cam = Student("Cameron", 2, 2, 0)
geoff = Student("Geoff", 0, 3, 0)


# poniźsze powinno zwrócoć: ["Phil"]
print(most_money([cam, geoff, phil]))
# poniźsze powinno zwrócoć: ["Cameron", "Geoff"])
print(most_money([cam, geoff]))
# poniźsze powinno zwrócoć: ["Geoff"]
print(most_money([geoff]))
