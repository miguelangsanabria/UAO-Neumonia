"""
test_predict.py
---------------

Este módulo contiene pruebas unitarias para las funciones del módulo `model_utils` utilizando pytest.
"""

import pytest
import numpy as np
from utils.model_utils import predict, model_fun


def test_predict():
    """
    Prueba la función `predict` del módulo `model_utils`.

    Esta prueba verifica:
    1. Que la función `predict` retorna la etiqueta correcta.
    2. Que la función `predict` retorna la probabilidad correcta.
    3. Que el mapa de calor generado tiene las dimensiones correctas.
    """
    # Crear una imagen de prueba
    test_image = np.random.randint(0, 256, (512, 512, 3), dtype=np.uint8)

    # Simular el modelo para asegurar que siempre devuelve una predicción conocida
    model = model_fun()

    # Forzar una predicción controlada
    def mock_predict(input_image):
        return np.array([[0.1, 0.1, 0.8]])

    model.predict = mock_predict

    # Hacer la predicción
    label, proba, heatmap = predict(test_image)

    # Verificar la etiqueta y la probabilidad
    assert label == "viral", "La etiqueta predicha no es la esperada."
    assert proba == 100.0, "La probabilidad predicha no es la esperada."

    # Verificar que el heatmap tenga las dimensiones esperadas
    assert heatmap.shape == (
        512,
        512,
        3,
    ), "Las dimensiones del heatmap no son las esperadas."
