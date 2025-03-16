import pytest

from src.core.genetic_code import ESNSeYGeneticCode
from src.systems.endocrine.regulation import NeuroEndocrineRegulator


def test_hormonal_adjustment():
    regulator = NeuroEndocrineRegulator(ESNSeYGeneticCode())
    initial_params = {"learning_rate": 0.5, "risk_tolerance": 0.7}

    cortisol = regulator.hormones["cortisol"]
    cortisol.current_level = 0.8

    adjusted = regulator.adjust_system_params(initial_params)

    expected = {
        "learning_rate": 0.5 - 0.3 * 0.8,
        "risk_tolerance": 0.7 - 0.4 * 0.8,
        "energy_consumption": 0.0 + 0.2 * 0.8
    }

    for param, value in expected.items():
        assert adjusted[param] == pytest.approx(value, abs=0.001)
