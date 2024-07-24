"""
test_preprocess.py
------------------

Este módulo contiene pruebas unitarias para la función `preprocess` del módulo `preprocess_utils` utilizando pytest.
"""

import pytest
import numpy as np
import cv2
from utils.preprocess_utils import preprocess


def test_preprocess():
    """
    Prueba la función `preprocess` del módulo `preprocess_utils`.

    Esta prueba verifica:
    1. Que la imagen procesada tenga las dimensiones esperadas (1, 512, 512, 1).
    2. Que los valores de la imagen procesada estén en el rango [0, 1].
    """
    # Imagen de prueba: una matriz 3D de 512x512x3
    test_image = np.random.randint(0, 256, (512, 512, 3), dtype=np.uint8)

    # Procesar la imagen
    processed_image = preprocess(test_image)

    # Verificar que la imagen procesada tenga las dimensiones esperadas
    assert processed_image.shape == (
        1,
        512,
        512,
        1,
    ), "Las dimensiones de la imagen procesada no son las esperadas."

    # Verificar que los valores de la imagen procesada estén en el rango [0, 1]
    assert (
        np.max(processed_image) <= 1.0 and np.min(processed_image) >= 0.0
    ), "Los valores de la imagen procesada no están en el rango [0, 1]."
