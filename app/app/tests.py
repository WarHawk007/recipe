
from django.test import SimpleTestCase

from app.calc import add

class CalcTestCase(SimpleTestCase):
    
    def test_add_numbers(self):
        res = add(2, 3)
        self.assertEqual(res, 5)