"""
preprocess_utils.py
-------------------

Este módulo contiene la función `preprocess` para preprocesar imágenes antes de su uso en modelos de aprendizaje profundo.
"""

import cv2
import numpy as np


def preprocess(array):
    """
    Preprocesa una imagen para que esté lista para ser utilizada en un modelo de aprendizaje profundo.

    Realiza los siguientes pasos:
    1. Redimensiona la imagen a 512x512 píxeles.
    2. Convierte la imagen a escala de grises.
    3. Aplica el método de ecualización del histograma adaptativo (CLAHE).
    4. Normaliza los valores de píxeles al rango [0, 1].
    5. Expande las dimensiones para que coincidan con el formato esperado por el modelo.

    Args:
        array (numpy.ndarray): La imagen de entrada en formato de matriz numpy.

    Returns:
        numpy.ndarray: La imagen preprocesada lista para el modelo.
    """
    array = cv2.resize(array, (512, 512))
    array = cv2.cvtColor(array, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(4, 4))
    array = clahe.apply(array)
    array = array / 255
    array = np.expand_dims(array, axis=-1)
    array = np.expand_dims(array, axis=0)
    return array
