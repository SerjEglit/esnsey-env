import unittest
from src.core.genetic_code import ESNSeYGeneticCode, GeneticHyperparams
from src.systems.endocrine.regulation import NeuroEndocrineRegulator


class TestGeneticCode(unittest.TestCase):
    def setUp(self):
        self.dna = ESNSeYGeneticCode()

    def test_initial_hyperparams(self):
        hyperparams = GeneticHyperparams(
            mutation_rate=0.05,
            neuroplasticity=0.7,
            homeostasis={"min_energy": 30.0, "recovery_rate": 0.1}
        )
        regulator = NeuroEndocrineRegulator(ESNSeYGeneticCode(hyperparams))

    def test_mutation(self):
        initial = self.dna.hyperparams.neuroplasticity
        self.dna.mutate({"neuroplasticity": 0.1})
        self.assertNotEqual(initial, self.dna.hyperparams.neuroplasticity)


if __name__ == "__main__":
    unittest.main()
