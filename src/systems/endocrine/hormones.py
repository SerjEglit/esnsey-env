from pydantic import BaseModel, Field
from typing import Dict
from collections import UserDict

class Hormone(BaseModel):
    """Базовый класс биологически инспирированного гормона"""
    name: str = Field(..., min_length=3)
    current_level: float = Field(0.0, ge=0.0, le=1.0)
    target_params: Dict[str, float]

    @classmethod
    def cortisol(cls):
        """Гормон стресс-реакции"""
        return cls(
            name="Digital Cortisol",
            target_params={
                "learning_rate": -0.3,
                "risk_tolerance": -0.4,
                "energy_consumption": 0.2
            }
        )

class HormonalBalance(UserDict):
    def __init__(self):
        super().__init__()
        self.data = {
            "cortisol": Hormone.cortisol(),
            "dopamine": Hormone(
                name="Reward Dopamine",
                target_params={
                    "exploration_rate": 0.5,
                    "creativity": 0.3
                }
            )
        }


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
