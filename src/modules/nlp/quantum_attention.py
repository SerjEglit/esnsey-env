# src/modules/nlp/quantum_attention.py
from qiskit import QuantumCircuit
from qiskit_machine_learning.neural_networks import SamplerQNN
from transformers import PreTrainedModel
import torch


class QuantumAttentionConfig:
    """Конфигурация для квантового слоя внимания"""

    def __init__(self,
                 n_qubits: int = 4,
                 entanglement: str = 'linear'):
        self.n_qubits = n_qubits
        self.entanglement = entanglement


class QuantumAttentionLayer(PreTrainedModel):
    def __init__(self, config):
        super().__init__(config)
        self.config = config
        self.quantum_circuit = self._build_qattention_circuit()
        self.qnn = SamplerQNN(
            circuit=self.quantum_circuit,
            input_params=[],
            weight_params=self.quantum_circuit.parameters
        )

    def _build_qattention_circuit(self):
        """Создание параметризованной квантовой схемы"""
        qc = QuantumCircuit(self.config.n_qubits)

        # Кодирование входных данных
        for i in range(self.config.n_qubits):
            qc.h(i)

        # Создание запутанности
        for i in range(self.config.n_qubits - 1):
            qc.cx(i, i + 1)

        # Барьер для визуализации
        qc.barrier()

        return qc

    def forward(self, embeddings: torch.Tensor):
        """Интеграция с PyTorch"""
        # Конвертация тензора в numpy array
        embeddings_np = embeddings.detach().numpy()

        # Выполнение квантовых вычислений
        quantum_output = self.qnn.run(embeddings_np)

        # Конвертация обратно в тензор
        return torch.from_numpy(quantum_output)
