#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_b.question_b import get_assessment_value, get_tax_assessed

class Test_Config(unittest.TestCase):

    def test_get_tax_assessed_1(self):
        self.assertEqual(get_tax_assessed(6000), 43.20)
    def test_get_tax_assessed_2(self):
        self.assertEqual(get_tax_assessed(10000), 72)

    def test_get_assessment_value_1(self):
        self.assertEqual(get_assessment_value(10000), 6000)
    def test_get_assessment_value_2(self):
        self.assertEqual(get_assessment_value(20000), 12000)
