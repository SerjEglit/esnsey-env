import numpy as np
from typing import List

class DataMetabolism:
    def __init__(self, metabolic_rate: float = 0.1):
        self.metabolic_rate = metabolic_rate  # Скорость "переваривания" данных
        self.atp_level = 100.0  # Энергетический уровень системы

    def digest_data(self, raw_data: List[float]) -> np.ndarray:
        """Преобразование данных в биологически совместимый формат"""
        self._consume_energy(len(raw_data))
        return np.array(raw_data) * self.metabolic_rate

    def _consume_energy(self, data_size: int):
        """Потребление энергии на обработку данных"""
        self.atp_level -= data_size * 0.05
        if self.atp_level < 20:
            self._trigger_energy_alert()

    def _trigger_energy_alert(self):
        """Активация режима энергосбережения"""
        self.metabolic_rate *= 0.5
