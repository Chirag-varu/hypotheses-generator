import unittest
from rule_engine import apply_forward_chaining
from knowledge_base import rules

class TestRuleEngine(unittest.TestCase):
    def test_bird_hypothesis(self):
        facts = [
            ('has_property', 'bird', 'feather'),
            ('can', 'bird', 'fly'),
            ('is_a', 'bird', 'animal')
        ]
        inferred = apply_forward_chaining(facts, rules)
        self.assertIn(('hypothesis', 'bird', 'might_be_a_bird'), inferred)

    def test_photosynthesizing(self):
        facts = [
            ('is_a', 'plant', 'plant'),
            ('has_property', 'plant', 'green'),
            ('can', 'plant', 'use_sunlight')
        ]
        inferred = apply_forward_chaining(facts, rules)
        self.assertIn(('hypothesis', 'plant', 'might_be_photosynthesizing'), inferred)

if __name__ == '__main__':
    unittest.main()
