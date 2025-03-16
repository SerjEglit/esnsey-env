import numpy as np
from typing import List, Optional
from src.systems.metabolism.data_processing import DataMetabolism

class QuantumNeuron:
    def __init__(self, weights: List[float]):
        self.weights = np.array(weights)
        self.quantum_state: Optional[np.ndarray] = None

    def activate(self, inputs: List[float]) -> float:
        """Активация нейрона с квантовой суперпозицией"""
        input_vector = np.array(inputs)
        return np.dot(self.weights, input_vector)

class NeuralLayer:
    def __init__(self, neurons: list, metabolism: DataMetabolism):
        self.neurons = neurons
        self.metabolism = metabolism

    def process(self, inputs: List[float]) -> List[float]:
        processed_data = self.metabolism.digest_data(inputs)
        return [n.activate(processed_data) for n in self.neurons]
