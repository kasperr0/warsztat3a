# Modyfikatory dostępu:
#
# To konstrukcje służące do ograniczenia lub umożliwienia dostępu do pól obiektu.
# W javie mamy private, public, protected.
# Zanim pokażę jak to wygląda w pythonie zastanówmy się: Po co stosować takie konstrukcje?
# Jaki jest sens ograniczania dostępu do pól?

# Wyobraźmy sobie klasę konwertującą temperaturę ze stopni C na stopnie F.

class Celsius:
    def __init__(self, temperature):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32


# Powyższy kod działa nieźle, ale nie mamy kontroli nad polem temperature.
# Przykładowo można tam zapisać wartość mniejszą niż zero absolutne. W jaki sposób można temu zaradzić?

class Celsius:

    def __init__(self, temperature):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self.__temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self.__temperature = value


cel = Celsius(10)
# cel.__temperature=9999
print(cel.to_fahrenheit())
# print(cel.__dict__)
