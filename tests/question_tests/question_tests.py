#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import use_local_variable

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(10, 10, use_local_variable(100))
