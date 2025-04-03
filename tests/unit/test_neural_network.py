# test_neural_network.py

import unittest
import numpy as np
from prai_core.neural_network import create_neural_network

class TestNeuralNetwork(unittest.TestCase):

    def test_model_creation(self):
        """
        Testet die Erstellung des neuronalen Netzwerks, um sicherzustellen,
        dass es ohne Fehler kompiliert wird.
        """
        input_shape = (10,)  # Beispielhafte Eingabegröße mit 10 Features
        model = create_neural_network(input_shape)

        # Überprüfen, ob das Modell Schichten enthält
        self.assertGreater(len(model.layers), 0, "Das Modell sollte mindestens eine Schicht enthalten.")

        # Überprüfen, ob das Modell kompiliert ist
        self.assertTrue(model._is_compiled, "Das Modell sollte erfolgreich kompiliert werden.")

    def test_model_prediction_shape(self):
        """
        Testet, ob das Modell Vorhersagen in der richtigen Form ausgibt.
        """
        input_shape = (10,)  # Beispielhafte Eingabegröße
        model = create_neural_network(input_shape)

        # Erstelle Dummy-Daten für Vorhersagen
        test_input = np.random.random((5, 10))  # 5 Beispiele mit 10 Features
        predictions = model.predict(test_input)

        # Überprüfen, ob die Ausgabedimension korrekt ist
        self.assertEqual(predictions.shape, (5, 1), "Die Vorhersagen sollten die Form (5, 1) haben.")

    def test_model_training(self):
        """
        Testet, ob das Modell erfolgreich trainiert werden kann.
        """
        input_shape = (10,)
        model = create_neural_network(input_shape)

        # Erstelle Dummy-Daten für das Training
        X_train = np.random.random((100, 10))  # 100 Beispiele mit 10 Features
        y_train = np.random.randint(0, 2, 100)  # Binäre Zielwerte (0 oder 1)

        # Trainiere das Modell und überprüfe, ob der Trainingsprozess durchläuft
        history = model.fit(X_train, y_train, epochs=1, batch_size=10, verbose=0)

        # Überprüfen, ob Trainingshistorie existiert
        self.assertIn("accuracy", history.history, "Das Training sollte einen Accuracy-Wert liefern.")
        self.assertIn("loss", history.history, "Das Training sollte einen Loss-Wert liefern.")

if __name__ == "__main__":
    unittest.main()
