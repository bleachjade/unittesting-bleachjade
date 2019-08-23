import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    def  test_init(self):
        """Test __init__ method"""
        f = Fraction(1,2)
        self.assertEqual(1, f.numerator)
        self.assertEqual(2, f.denominator)
        g = Fraction(2,-4)
        self.assertEqual(-1, g.numerator)
        self.assertEqual(2, g.denominator)
        h = Fraction(5,-2)
        self.assertEqual(-5, h.numerator)
        self.assertEqual(2, h.denominator)
        i = Fraction(20,2)
        self.assertEqual(10, i.numerator)
        self.assertEqual(1, i.denominator)
        j = Fraction(-100,-2)
        self.assertEqual(50, j.numerator)
        self.assertEqual(1, j.denominator)
        k = Fraction(-5)
        self.assertEqual(-5, k.numerator)
        self.assertEqual(1, k.denominator)
        l = Fraction(0, 0)
        self.assertEqual(0, l.numerator)
        self.assertEqual(0, l.denominator)

    def test_str(self):
        """Test __str__ method"""
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())
        f = Fraction(99)
        self.assertEqual("99", f.__str__())
        f = Fraction(0, 0)
        self.assertEqual("0/0", f.__str__())


    def test_add(self):
        """Test __add__ method"""
        # 3/4 = 2/3 + 1/12
        self.assertEqual(Fraction(3,4), Fraction(1,12)+Fraction(2,3))
        self.assertEqual(Fraction(1,2), Fraction(1,12)+Fraction(5,12))
        self.assertEqual(Fraction(1), Fraction(1,10)+Fraction(18,20))
        self.assertEqual(Fraction(0), Fraction(2,3)+Fraction(-2,3))
        self.assertEqual(Fraction(-4), Fraction(-5,1)+Fraction(1))

    def test_sub(self):
        """Test __sub__ method"""
        # 1/2 = 2 - 3/2
        self.assertEqual(Fraction(-7,12), Fraction(1,12)-Fraction(2,3))
        self.assertEqual(Fraction(1,2), Fraction(2)-Fraction(3,2))
        self.assertEqual(Fraction(1), Fraction(-1)-Fraction(-2))
        self.assertEqual(Fraction(0), Fraction(2,3)-Fraction(2,3))
        self.assertEqual(Fraction(-6), Fraction(-5,1)-Fraction(1))

    def test_mul(self):
        """Test __mul__ method"""
        # 3/4 = 1/2 * 3/2
        self.assertEqual(Fraction(3,4), Fraction(1,2)*Fraction(3,2))
        self.assertEqual(Fraction(1,2), Fraction(1,12)*Fraction(6,1))
        self.assertEqual(Fraction(1), Fraction(1,10)*Fraction(10,1))
        self.assertEqual(Fraction(0), Fraction(0)*Fraction(-2,3))
        self.assertEqual(Fraction(-20), Fraction(-5,1)*Fraction(4))
        self.assertEqual(Fraction(-4), Fraction(-5,1)*Fraction(4,5))



    def test_eq(self):
        """Test __eq__ method"""
        f = Fraction(1,2)
        g = Fraction(-40,-80)
        h = Fraction(10000,20001) # not quite 1/2
        i = Fraction(-50)
        NaN = Fraction(0, 0)
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))
        self.assertFalse(i == g)
        self.assertFalse(i.__eq__(g))
        self.assertFalse(NaN == f)
