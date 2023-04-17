from django.test import SimpleTestCase
from app import calc


class CalcTest(SimpleTestCase):
    def test_add(self):
        res = calc.add(4,5)

        self.assertEqual(res,9)

    def test_substract(self): 
        """test driven development"""
        """create unit test first, and then add funcionality"""
        res=calc.substract(15,10)
        self.assertEqual(res,5)