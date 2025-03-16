import unittest
from src.core.genetic_code import ESNSeYGeneticCode


class TestGeneticCode(unittest.TestCase):
    def setUp(self):
        self.dna = ESNSeYGeneticCode()

    def test_initial_hyperparams(self):
        self.assertAlmostEqual(self.dna.hyperparams.mutation_rate, 0.05)

    def test_mutation(self):
        initial = self.dna.hyperparams.neuroplasticity
        self.dna.mutate({"neuroplasticity": 0.1})
        self.assertNotEqual(initial, self.dna.hyperparams.neuroplasticity)


if __name__ == "__main__":
    unittest.main()
