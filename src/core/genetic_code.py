from typing import Dict, Any

from pydantic import BaseModel, ConfigDict, field_validator


class GeneticHyperparams(BaseModel):
    mutation_rate: float = 0.1
    neuroplasticity: float = 0.5
    homeostasis: dict = {"min_energy": 30.0, "recovery_rate": 0.1}

    @classmethod
    @field_validator('neuroplasticity')
    def check_neuroplasticity(cls, v):
        if not 0.0 <= v <= 1.0:
            raise ValueError("Neuroplasticity must be between 0 and 1")
        return v


class ESNSeYGeneticCode:
    def __init__(self, hyperparams: GeneticHyperparams = None):
        self.hyperparams = hyperparams or GeneticHyperparams()
        self.core_principles = {
            "security": "OAuth2_Quantum",
            "architecture": "BioDigital_Twin"
        }
        self.epigenetic_factors: Dict[str, Any] = {}

    def mutate(self, mutation_data: Dict[str, Any]):
        """Эпигенетическая модификация параметров"""
        for key, value in mutation_data.items():
            if hasattr(self.hyperparams, key):
                current = getattr(self.hyperparams, key)
                setattr(self.hyperparams, key, current * (1 + value))
            else:
                self.epigenetic_factors[key] = value

    def express_gene(self, gene_name: str) -> str:
        """Экспрессия генетической информации"""
        return self.core_principles.get(gene_name, "Unknown gene")

    def update_hyperparam(self, param: str, value: Any):
        """Безопасное обновление через создание новой модели"""
        self.hyperparams = self.hyperparams.model_copy(
            update={param: value},
            deep=True
        )
