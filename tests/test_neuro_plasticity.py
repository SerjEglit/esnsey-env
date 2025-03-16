import warnings
import numpy as np
from src.core.genetic_code import ESNSeYGeneticCode, GeneticHyperparams
from src.systems.nervous.plasticity import NeuroPlasticityEngine


def test_quantum_plasticity():
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")

    hyperparams = GeneticHyperparams(
        mutation_rate=0.05,
        neuroplasticity=0.7,
        homeostasis={"min_energy": 30.0, "recovery_rate": 0.1}
    )

    dna = ESNSeYGeneticCode(hyperparams=hyperparams)
    engine = NeuroPlasticityEngine(dna)

    # Тест с длиной 3
    weights = [0.5, -0.3, 0.8]
    adjusted = engine.adjust_weights(weights, {"neuroplasticity": 0.9})
    assert len(adjusted) == 3
    assert all(-1 <= w <= 1 for w in adjusted)

    # Тест с пустым списком
    try:
        engine.adjust_weights([], {"neuroplasticity": 0.9})
        assert False
    except ValueError:
        assert True

"""
pytest tests/test_neuro_plasticity.py -v

git add .
git commit -m "fix(quantum): Add power-of-two padding for weights
- Implement automatic weights padding
- Use Statevector for proper simulation
- Update tests for different lengths"
git push origin feature/neuro-plasticity

"""