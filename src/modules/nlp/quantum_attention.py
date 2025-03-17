import numpy as np
import torch
from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from qiskit.primitives import StatevectorSampler
from qiskit_machine_learning.neural_networks import SamplerQNN


class QuantumAttentionConfig:
    def __init__(self, n_qubits: int = 4):
        self.n_qubits = n_qubits
        self.input_size = n_qubits  # Явное указание размера входа


class QuantumAttentionLayer(torch.nn.Module):
    def __init__(self, config: QuantumAttentionConfig):
        super().__init__()
        self.config = config

        # Создаем параметризованную схему
        self.params = [Parameter(f'θ{i}') for i in range(config.input_size)]
        self.circuit = self._build_circuit()

        # Инициализируем квантовую нейронную сеть с использованием V2-примитива
        self.qnn = SamplerQNN(
            circuit=self.circuit,
            input_params=self.params,  # Параметры для входа
            weight_params=[],
            sampler=StatevectorSampler()
        )

    def _build_circuit(self):
        """Схема с параметризованным кодированием данных"""
        qc = QuantumCircuit(self.config.n_qubits)
        # Кодирование входных данных через параметры
        for i, param in enumerate(self.params):
            qc.rx(param, i)
        # Создание запутанности
        for i in range(self.config.n_qubits - 1):
            qc.cx(i, i + 1)
        return qc

    def forward(self, embeddings: torch.Tensor):
        # Подготовка данных для QNN
        inputs = embeddings.detach().numpy().reshape(-1, self.config.input_size)
        # Нормализация
        inputs = inputs / np.linalg.norm(inputs, axis=1, keepdims=True)
        # Выполнение квантовых вычислений
        results = []
        for x in inputs:
            result = self.qnn.forward(x, None)
            # Убираем лишнее измерение, если оно есть
            result = np.squeeze(result, axis=0)
            results.append(result)
        return torch.tensor(np.array(results), dtype=torch.float32)
