from src.systems.endocrine.hormones import HormonalBalance, Hormone
from src.systems.nervous.neural_network import NeuralLayer
from src.core.genetic_code import ESNSeYGeneticCode


class NeuroEndocrineRegulator:
    def __init__(self, dna: ESNSeYGeneticCode):
        self.dna = dna
        self.hormones = HormonalBalance()
        self._validate_hormones()

    def _validate_hormones(self):
        """Проверка целостности гормонального баланса"""
        for name, hormone in self.hormones.items():
            if not isinstance(hormone, Hormone):
                raise TypeError(f"Invalid hormone type: {type(hormone)}")

    def adjust_system_params(self, current_params: dict) -> dict:
        """Динамическая регуляция с инициализацией параметров"""
        # Инициализация всех возможных параметров
        all_params = {
            "learning_rate": 0.5,
            "risk_tolerance": 0.7,
            "energy_consumption": 0.0,
            "exploration_rate": 0.5,
            "creativity": 0.3
        }
        params = {**all_params, **current_params}  # Объединяем с переданными

        for hormone in self.hormones.values():
            for param, effect in hormone.target_params.items():
                params[param] += hormone.current_level * effect
                params[param] = max(0.0, min(1.0, params[param]))

        return params

