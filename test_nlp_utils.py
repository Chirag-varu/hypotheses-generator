import unittest
from nlp_utils import parse_natural_language_fact

class TestNLPUtils(unittest.TestCase):
    def test_singular_plural(self):
        self.assertIn(('has_property', 'bird', 'feather'), parse_natural_language_fact('bird has property feathers'))
        self.assertIn(('has_property', 'bird', 'feather'), parse_natural_language_fact('bird has property feather'))

    def test_is_a(self):
        self.assertIn(('is_a', 'john', 'human'), parse_natural_language_fact('john is a human'))
        self.assertIn(('is_a', 'john', 'human'), parse_natural_language_fact('john is human'))

    def test_can(self):
        self.assertIn(('can', 'bird', 'fly'), parse_natural_language_fact('bird can fly'))

    def test_multiple_facts(self):
        facts = parse_natural_language_fact('bird has property feathers and can fly')
        self.assertIn(('has_property', 'bird', 'feather'), facts)
        self.assertIn(('can', 'bird', 'fly'), facts)

    def test_casing(self):
        self.assertIn(('is_a', 'John', 'human'), parse_natural_language_fact('John is human'))
        self.assertIn(('has_symptom', 'John', 'fever'), parse_natural_language_fact('John has symptom fever'))

if __name__ == '__main__':
    unittest.main()
