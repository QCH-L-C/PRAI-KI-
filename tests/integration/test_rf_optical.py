# test_rf_optical.py

import unittest
import numpy as np
from rf_optical_module import generate_rf_signal, simulate_optical_interaction, analyze_signal_properties

class TestRFOpticalIntegration(unittest.TestCase):

    def test_generate_and_simulate_interaction(self):
        """
        Testet, ob ein generiertes RF-Signal korrekt mit einem optischen Medium interagiert.
        """
        # Testdaten für RF-Signal
        frequency = 1e6  # 1 MHz
        amplitude = 1.0
        duration = 0.01  # 10 Millisekunden
        sampling_rate = 1e6  # 1 MS/s

        # Generiere RF-Signal
        time, rf_signal = generate_rf_signal(frequency, amplitude, duration, sampling_rate)

        # Überprüfen der Dimension des Signals
        self.assertEqual(len(time), len(rf_signal), "Zeit und Signal sollten die gleiche Länge haben.")

        # Simuliere Wechselwirkung mit optischem Medium
        optical_constant = 1.5  # Beispiel-Brechungsindex
        modified_signal = simulate_optical_interaction(rf_signal, optical_constant)

        # Überprüfen, ob das modifizierte Signal korrekt angepasst ist
        expected_signal = rf_signal * optical_constant
        np.testing.assert_array_almost_equal(modified_signal, expected_signal, decimal=5, 
                                             err_msg="Das modifizierte Signal sollte korrekt skaliert sein.")

    def test_signal_analysis(self):
        """
        Testet, ob die Analyse grundlegender Signal-Eigenschaften korrekt ist.
        """
        # Testdaten: Beispielsignal
        signal = np.array([0.5, -0.2, 0.8, 0.0, 1.2])

        # Analysiere Signal
        properties = analyze_signal_properties(signal)

        # Überprüfen der berechneten Eigenschaften
        self.assertAlmostEqual(properties["mean"], np.mean(signal), places=5, "Der Mittelwert sollte korrekt berechnet sein.")
        self.assertAlmostEqual(properties["std_dev"], np.std(signal), places=5, "Die Standardabweichung sollte korrekt berechnet sein.")
        self.assertEqual(properties["max"], np.max(signal), "Das Maximum sollte korrekt sein.")
        self.assertEqual(properties["min"], np.min(signal), "Das Minimum sollte korrekt sein.")

    def test_integration_workflow(self):
        """
        Führt eine komplette Integration von RF-Signal-Erzeugung, optischer Simulation und Analyse aus.
        """
        # Testdaten für RF-Signal
        frequency = 2e6  # 2 MHz
        amplitude = 0.5
        duration = 0.005  # 5 Millisekunden
        sampling_rate = 1e6  # 1 MS/s

        # Generiere RF-Signal
        time, rf_signal = generate_rf_signal(frequency, amplitude, duration, sampling_rate)

        # Simuliere Wechselwirkung mit optischem Medium
        optical_constant = 1.2
        modified_signal = simulate_optical_interaction(rf_signal, optical_constant)

        # Analysiere modifiziertes Signal
        properties = analyze_signal_properties(modified_signal)

        # Überprüfen, ob Eigenschaften korrekt sind
        self.assertTrue("mean" in properties, "Der Workflow sollte die Eigenschaft 'mean' berechnen.")
        self.assertTrue("std_dev" in properties, "Der Workflow sollte die Eigenschaft 'std_dev' berechnen.")
        self.assertTrue("max" in properties, "Der Workflow sollte die Eigenschaft 'max' berechnen.")
        self.assertTrue("min" in properties, "Der Workflow sollte die Eigenschaft 'min' berechnen.")

if __name__ == "__main__":
    unittest.main()
