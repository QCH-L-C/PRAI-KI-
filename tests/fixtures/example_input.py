import json

# Testressourcen laden
with open("example_input.json", "r") as file:
    test_data = json.load(file)

# Zugriff auf RF-Signalparameter
rf_params = test_data["rf_signal_params"]
print(rf_params)

# Zugriff auf erwartete Analyseergebnisse
expected_analysis = test_data["expected_analysis"]
print(expected_analysis)
