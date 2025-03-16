import unittest
from src.core.genetic_code import ESNSeYGeneticCode
from src.systems.immune.security import BioFirewall, ThreatPattern

class TestImmuneSystem(unittest.TestCase):
    def setUp(self):
        self.dna = ESNSeYGeneticCode()
        self.firewall = BioFirewall(self.dna)
        self.threat = ThreatPattern(signature="malware_x", threat_level=5)

    def test_threat_detection(self):
        self.firewall.add_threat_pattern(self.threat)
        self.assertTrue(self.firewall.scan_input("data_with_malware_x"))

    def test_quantum_encryption_flag(self):
        self.assertTrue(self.firewall.quantum_encryption_enabled)
