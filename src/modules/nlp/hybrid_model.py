# src/modules/nlp/hybrid_model.py
import torch
from transformers import BertModel
from src.modules.nlp.quantum_attention import QuantumAttentionLayer, QuantumAttentionConfig


class HybridQuantumBERT(torch.nn.Module):
    """
    Гибридная модель, объединяющая BERT и квантовое внимание.

    Параметры:
    - config (QuantumAttentionConfig): Конфигурация квантового слоя
    - bert_model (str): Название предобученной модели BERT
    """

    def __init__(self,
                 config: QuantumAttentionConfig = QuantumAttentionConfig(),
                 bert_model: str = 'bert-base-uncased'):
        super().__init__()

        # Инициализация BERT
        self.bert = BertModel.from_pretrained(bert_model)

        # Квантовый слой внимания
        self.quantum_attention = QuantumAttentionLayer(config)

        # Классический классификатор
        self.classifier = torch.nn.Linear(
            self.bert.config.hidden_size,
            2  # Пример для бинарной классификации
        )

    def forward(self, input_ids, attention_mask=None):
        """
        Прямой проход:
        1. BERT кодирует входные данные
        2. Квантовый слой обрабатывает эмбеддинги
        3. Классификатор возвращает логиты
        """
        # BERT Encoding
        outputs = self.bert(
            input_ids=input_ids,
            attention_mask=attention_mask
        )

        # Quantum Attention
        quantum_embeddings = self.quantum_attention(
            outputs.last_hidden_state
        )

        # Classification
        logits = self.classifier(quantum_embeddings.mean(dim=1))
        return logits
