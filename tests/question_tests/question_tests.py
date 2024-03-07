#write function tests here, don't add input('') statements here!
import unittest
from src.question_d.question_d import use_global

#follow this example to add questions b, c, and d for testing including their functions
from question_d.question_d import use_global

class Test_Config(unittest.TestCase):

    #def test_get_tax_assessed_1(self):
        #self.assertEqual(get_tax_assessed(6000), 43.20)
    #def test_get_tax_assessed_2(self):
        #self.assertEqual(get_tax_assessed(10000), 72)

    #def test_get_assessment_value_1(self):
        #self.assertEqual(get_assessment_value(10000), 6000)
    #def test_get_assessment_value_2(self):
        #self.assertEqual(get_assessment_value(20000), 12000)

    #def test_get_random_number(self):
        #self.assertIn(get_random_number(), range(1,6))
    
    def test_use_global(self):
        self.assertEqual(use_global)
        #Could not get the test to find module "question_d" or "src" like it did for the other 3 projects
