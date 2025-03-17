# tests/test_quantum_nlp.py
import pytest
import torch
from src.modules.nlp.quantum_attention import QuantumAttentionLayer, QuantumAttentionConfig


def test_quantum_attention():
    config = QuantumAttentionConfig(n_qubits=4)
    layer = QuantumAttentionLayer(config)

    # Тестовые данные с правильной размерностью [batch_size, input_size]
    embeddings = torch.randn(2, 4)  # 2 примера по 4 признака

    output = layer(embeddings)
    assert output.shape == (2, 16), f"Ожидается [2, 16], получено {output.shape}"
