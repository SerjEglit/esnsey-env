from typing import Dict, Any
from pydantic import BaseModel
from src.core.genetic_code import ESNSeYGeneticCode

class ThreatPattern(BaseModel):
    signature: str
    threat_level: int = 1

class BioFirewall:
    def __init__(self, dna: ESNSeYGeneticCode):
        self.dna = dna
        self.threat_database: Dict[str, ThreatPattern] = {}
        self.quantum_encryption_enabled = "Quantum" in self.dna.core_principles["security"]

    def add_threat_pattern(self, pattern: ThreatPattern):
        """Добавление паттерна угрозы (аналог выработки антител)"""
        self.threat_database[pattern.signature] = pattern

    def scan_input(self, data: Any) -> bool:
        """Сканирование данных на наличие угроз"""
        if self.quantum_encryption_enabled:
            return self._quantum_threat_detection(data)
        return self._classic_threat_detection(data)

    def _quantum_threat_detection(self, data) -> bool:
        """Квантовый алгоритм распознавания угроз"""
        return any(pattern in str(data) for pattern in self.threat_database)
