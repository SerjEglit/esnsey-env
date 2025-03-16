import numpy as np
from typing import List, Optional

class QuantumNeuron:
    def __init__(self, weights: List[float]):
        self.weights = np.array(weights)
        self.quantum_state: Optional[np.ndarray] = None

    def activate(self, inputs: List[float]) -> float:
        """Активация нейрона с квантовой суперпозицией"""
        input_vector = np.array(inputs)
        return np.dot(self.weights, input_vector)

class NeuralLayer:
    def __init__(self, neurons: List[QuantumNeuron]):
        self.neurons = neurons

    def process(self, inputs: List[float]) -> List[float]:
        return [neuron.activate(inputs) for neuron in self.neurons]
