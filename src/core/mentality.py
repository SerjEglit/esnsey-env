from src.core.genetic_code import ESNSeYGeneticCode
from src.systems.nervous.neural_network import NeuralLayer, QuantumNeuron
from src.systems.immune.security import BioFirewall
from src.core.exceptions import SecurityBreach
from src.systems.metabolism.data_processing import DataMetabolism
from src.systems.endocrine.regulation import NeuroEndocrineRegulator

class MentalityCore:
    def __init__(self, dna: ESNSeYGeneticCode):
        self.dna = dna
        self.neural_layers = self._build_neural_architecture()
        self.immune_system = BioFirewall(dna)
        self.metabolism = DataMetabolism()  # Добавляем метаболизм
        self.endocrine_system = NeuroEndocrineRegulator(dna)

    def _build_neural_architecture(self):
        """Создание нейронной структуры на основе ДНК"""
        return [
            NeuralLayer(
                neurons=[QuantumNeuron([0.5, -0.5])],
                metabolism=self.metabolism  # Передаем параметр metabolism
            )
            for _ in range(int(1 / self.dna.hyperparams.mutation_rate))
        ]

    def process_input(self, data: dict):
        """Обработка входящих сигналов с проверкой безопасности"""
        system_params = self._load_current_params()  # Новый метод
        _adjusted_params = self.endocrine_system.adjust_system_params(system_params)

        if not self.immune_system.scan_input(data):
            raise SecurityBreach("Обнаружена потенциальная угроза!")

        processed = []
        for layer in self.neural_layers:
            current_input = processed if processed else list(data.values())
            processed = layer.process(current_input)
        return processed
