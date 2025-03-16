from typing import Any
from pydantic import BaseModel, Field, field_validator
from src.core.genetic_code import ESNSeYGeneticCode


class ThreatPattern(BaseModel):
    signature: str
    threat_level: int = Field(ge=1, le=10)

    @classmethod
    @field_validator('signature')
    def validate_signature(cls, v: str) -> str:
        """Нормализация и валидация сигнатуры"""
        if len(v) < 3:
            raise ValueError("Signature must be at least 3 characters")
        return v.lower()


class BioFirewall:
    def __init__(self, dna: ESNSeYGeneticCode):
        self.dna = dna
        self.threat_database = {}
        self.quantum_encryption_enabled = "Quantum" in self.dna.core_principles.get("security", "")

    def add_threat_pattern(self, pattern: ThreatPattern):
        """Добавление паттерна с автоматической нормализацией"""
        normalized_signature = pattern.signature.lower()
        self.threat_database[normalized_signature] = normalized_signature

    def _classic_threat_detection(self, data) -> bool:
        """Поиск угроз в нормализованных данных"""
        processed_data = str(data).lower()
        return any(
            pattern in processed_data
            for pattern in self.threat_database.values()
        )

    def scan_input(self, data: Any) -> bool:
        if self.quantum_encryption_enabled:
            return self._quantum_threat_detection(data)
        return self._classic_threat_detection(data)

    def _quantum_threat_detection(self, data) -> bool:
        return any(
            pattern in str(data).lower()  # Добавить lower() для согласованности
            for pattern in self.threat_database.values()
        )
