# src/systems/endocrine/hormones.py
class HormonalRegulator:
    def __init__(self):
        self.hormones = {
            'dopamine': 0.0,
            'cortisol': 0.0
        }

    def release_hormone(self, name: str, amount: float):
        """Регуляция систем через гормональный фон"""
        self.hormones[name] = max(0, min(1, amount))
