import math

class Fraction:
    """A fraction with a numerator and denominator and arithmetic operations.

    Fractions are always stored in proper form, without common factors in 
    numerator and denominator, and denominator >= 0.
    Since Fractions are stored in proper form, each value has a
    unique representation, e.g. 4/5, 24/30, and -20/-25 have the same
    internal representation.
    """
    
    def __init__(self, numerator, denominator=1):
        """Initialize a new fraction with the given numerator
           and denominator (default 1).
        """
        self.numerator = numerator
        self.denominator = denominator
        if self.denominator < 0:
            self.numerator = -1*numerator
            self.denominator = abs(denominator)
        self.gcd()

    def gcd(self):
        """Calculate the Greatest Common Divisor of numerator 
           and denominator.
        """
        gcd = math.gcd(self.numerator, self.denominator)

        if self.denominator == 0:
            self.denominator = 0
        else:
            self.numerator = int(self.numerator/gcd)
            self.denominator = int(self.denominator/gcd)

    def __add__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        numerator = (self.numerator*frac.denominator)+(self.denominator*frac.numerator)
        denominator = self.denominator*frac.denominator
        return Fraction(numerator, denominator)

    def __sub__(self, frac):
        """Return the minus result of two fractions as a new fraction.
           Use the standard formula  a/b - c/d = (ad-bc)/(b*d)
        """
        numerator = (self.numerator*frac.denominator)-(self.denominator*frac.numerator)
        denominator = self.denominator*frac.denominator
        return Fraction(numerator, denominator)

    def __mul__(self, frac):
        """Return the multiplication of two fractions as a new fraction.
           Use the standard formula  a/b * c/d = (a*c)/(b*d)
        """
        numerator = self.numerator*frac.numerator
        denominator = self.denominator*frac.denominator
        return Fraction(numerator, denominator)

    def __str__(self):
        if self.numerator == 0 and self.denominator == 0:
            return str(self.numerator)+"/"+str(self.denominator)
        if self.denominator == -1:
            return str(self.numerator)
        elif self.denominator < 0:
            self.denominator = abs(self.denominator)
        if self.denominator == 1:
            return str(self.numerator)
        return str(self.numerator)+"/"+str(self.denominator)


    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """
        return self.numerator == frac.numerator and self.denominator == frac.denominator

