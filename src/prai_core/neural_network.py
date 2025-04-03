# neural_network.py
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation
from tensorflow.keras.optimizers import Adam

def create_neural_network(input_shape):
    """
    Erstellt die Architektur des neuronalen Netzwerks für RF Optical Futuristics-Physics.
    
    :param input_shape: Tuple, das die Eingabegröße beschreibt (z.B. Anzahl der Features).
    :return: Ein kompiliertes Modell.
    """
    model = Sequential()

    # Eingabeschicht
    model.add(Dense(128, input_shape=input_shape, activation='relu'))
    model.add(Dropout(0.2))  # Regulierung der Überanpassung

    # Versteckte Schichten
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.2))

    model.add(Dense(32, activation='relu'))
    model.add(Dropout(0.2))

    # Ausgangsschicht
    model.add(Dense(1, activation='sigmoid'))  # Sigmoid für binäre Klassifikation

    # Kompilieren des Modells
    model.compile(optimizer=Adam(learning_rate=0.001),
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    return model

def train_model(model, X_train, y_train, epochs=50, batch_size=32):
    """
    Trainiert das neuronale Netzwerk mit den übergebenen Trainingsdaten.
    
    :param model: Das neuronale Netzwerkmodell.
    :param X_train: Eingabedaten für das Training.
    :param y_train: Zielwerte (Labels) für das Training.
    :param epochs: Anzahl der Epochen.
    :param batch_size: Batch-Größe für das Training.
    :return: Das trainierte Modell.
    """
    history = model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, validation_split=0.2)
    return history

if __name__ == "__main__":
    # Beispiel-Daten (Platzhalter für tatsächliche RF Optical-Daten)
    import numpy as np

    # Generierung von Dummy-Daten
    X_train = np.random.random((1000, 10))  # 1000 Beispiele, 10 Features
    y_train = np.random.randint(0, 2, 1000)  # Binäre Zielwerte (0 oder 1)

    # Netzwerk erstellen
    input_shape = (X_train.shape[1],)
    model = create_neural_network(input_shape)

    # Netzwerk trainieren
    print("Training des neuronalen Netzwerks...")
    history = train_model(model, X_train, y_train)

    # Modellzusammenfassung ausgeben
    model.summary()
