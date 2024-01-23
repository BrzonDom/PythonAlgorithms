
"""
Objekt komlexní číslo

Třídy pro komplexní čísla:

    Třída obsahuje dvě proměnné real a imag
    Konstruktor (metoda _init_()) nastavuje tyto proměnné defaultně na 0
    Pro přímý výpis funkcí print je vhodné definovat metodu _repr_, která vrací string
    Pozor: init a repr má v názvu dvě podtržítka!!!

"""


class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def amplitude(self):
        return (self.real * self.real + self.imag * self.imag) ** (1 / 2)

    def add(self, rhs):
        self.real += rhs.real
        self.imag += rhs.imag

    def sub(self, rhs):
        self.real -= rhs.real
        self.imag -= rhs.imag

    def __repr__(self):
        sign = "+";
        if (self.imag < 0):
            sign = "-";
        return str(self.real) + sign + str(abs(self.imag)) + "i"

    def mul(self, rhs):
        r = self.real * rhs.real - self.imag * rhs.imag;
        i = self.real * rhs.imag + self.imag * rhs.real;
        self.real = r
        self.imag = i


a = Complex()
print("a=", a)

b = Complex(1, -1)
print("b=", b)

a.add(b)
print("a=", a)

a.mul(b)
print("a=", a)

print("|a|=", a.amplitude())
print("|b|=", b.amplitude())