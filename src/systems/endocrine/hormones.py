from pydantic import BaseModel
from typing import Dict

class Hormone(BaseModel):
    name: str
    level: float = 0.0
    effect: Dict[str, float]

class EndocrineSystem:
    def __init__(self):
        self.hormones = {
            "neuroplasticity": Hormone(
                name="Neuroplasticity Factor",
                effect={"learning_rate": 0.3, "memory_decay": -0.2}
            )
        }

    def release_hormone(self, hormone_name: str, amount: float):
        """Регуляция гормонального уровня"""
        if hormone_name in self.hormones:
            self.hormones[hormone_name].level = max(0.0, min(1.0, round(amount, 2)))
