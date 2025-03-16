# src/systems/nervous/plasticity.py
import warnings
import numpy as np
from pydantic import BaseModel
from qiskit import transpile, QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)

class QuantumSynapseConfig(BaseModel):
    base_weight: float = 0.5
    plasticity_factor: float = 0.1


class NeuroPlasticityEngine:
    def __init__(self, dna):
        self.backend = AerSimulator(method='statevector')
        self.basis_gates = ['u3', 'cx', 'reset']

    def _pad_weights(self, weights):
        """Дополнение весов до степени двойки с обработкой пустого списка"""
        if len(weights) == 0:
            return np.array([1.0, 0.0]), 1  # Вектор для 1 кубита (|0⟩)

        n = len(weights)
        next_pow2 = 2 ** int(np.ceil(np.log2(n)))
        return np.resize(weights, next_pow2), int(np.log2(next_pow2))

    def _apply_quantum_shift(self, weights):
        """Квантовая трансформация весов"""
        padded_weights, num_qubits = self._pad_weights(weights)
        norm = np.linalg.norm(padded_weights)

        if norm == 0:
            return np.zeros_like(weights).tolist()

        normalized = padded_weights / norm

        qc = QuantumCircuit(num_qubits)
        qc.initialize(normalized)
        qc.save_statevector()

        transpiled_qc = transpile(qc, self.backend, optimization_level=1)
        result = self.backend.run(transpiled_qc).result()

        state = Statevector(result.get_statevector())
        denormalized = (state.data.real * norm)[:len(weights)]
        return np.clip(denormalized, -1, 1).tolist()

    def adjust_weights(self, weights, hormone_levels):
        if not isinstance(weights, (list, np.ndarray)):
            raise TypeError("Weights must be list or numpy array")
        if len(weights) == 0:
            raise ValueError("Weights list cannot be empty")  # Явное исключение

        return self._apply_quantum_shift(np.array(weights))
