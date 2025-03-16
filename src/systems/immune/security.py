# src/systems/immune/security.py
from typing import Any
from pydantic import BaseModel, Field, validator
from src.core.genetic_code import ESNSeYGeneticCode


class ThreatPattern(BaseModel):
    signature: str
    threat_level: int = Field(ge=1, le=10)

    @validator('signature')
    def validate_signature(cls, v):
        if len(v) < 3:
            raise ValueError("Signature too short")
        return v.lower()


class BioFirewall:
    def __init__(self, dna: ESNSeYGeneticCode):
        self.dna = dna
        self.threat_database = {}
        self.quantum_encryption_enabled = "Quantum" in self.dna.core_principles["security"]

    def add_threat_pattern(self, pattern: ThreatPattern):
        """Храним сигнатуры в нижнем регистре"""
        self.threat_database[pattern.signature] = pattern.signature.lower()

    def _classic_threat_detection(self, data) -> bool:
        """Проверка с учетом регистра"""
        return any(
            pattern in str(data).lower()
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
