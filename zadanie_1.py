# Zadanie (10 minut)
# Wykorzystując dziedziczenie po klasie bazowej Solid, stwórz klasy potomne reprezentujące poszczególne bryły: (prostopadłościan, kula, ostożek). W każdej z klas potomnych zaimplementuj metodę obliczającą objętość danej bryły.
#
# Wzory na objętość ... powinniście znać :-)
#
# A dla tych co nie pamiętają, oto wzory:
# - prostopadłościan (cuboid) `a * b * H`
# - kula (sphere) `4/3 [pi] r ** 3`
# - stożek (cone) `1/3 [pi] r**2 * H`

class Solid:
    def __init__(self, name):
        self.name = name

    def volume:
        pass

    def __str__(self):
        return f"Specific geometric solid :{self.name}"
