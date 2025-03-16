from src.core.genetic_code import ESNSeYGeneticCode
from src.systems.nervous.neural_network import NeuralLayer, QuantumNeuron


class MentalityCore:
    def __init__(self, dna: ESNSeYGeneticCode):
        self.dna = dna
        self.neural_layers = self._build_neural_architecture()

    def _build_neural_architecture(self):
        """Создание нейронной структуры на основе ДНК"""
        return [
            NeuralLayer([QuantumNeuron([0.5, -0.5])])
            for _ in range(int(1 / self.dna.hyperparams.mutation_rate))
        ]

    def process_input(self, data: dict):
        """Обработка входящих сигналов"""
        processed = []
        for layer in self.neural_layers:
            processed = layer.process(processed or list(data.values()))
        return processed
