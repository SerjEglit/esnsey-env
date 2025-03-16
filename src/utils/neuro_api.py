# src/utils/neuro_api.py
import requests
from requests import RequestException

from src.utils.config import BioConfig


class NeurotransmitterAPI:
    @staticmethod
    def send_signal(signal_type: str, data: dict):
        try:
            response = requests.post(
                f"{BioConfig.NEURO_API_BASE}/{signal_type}",
                json=data,
                headers={BioConfig.QUANTUM_AUTH_HEADER: "true"},
                timeout=5.0
            )
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            raise ConnectionError(f"Neuro API error: {str(e)}")
