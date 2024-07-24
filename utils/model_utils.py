"""
model_utils.py
--------------

Este módulo contiene funciones para cargar un modelo de CNN, predecir la clase de una imagen y generar un mapa de calor utilizando Grad-CAM.
"""

import tensorflow as tf
import numpy as np


def model_fun():
    """
    Carga un modelo CNN preentrenado desde un archivo.

    Returns:
        tensorflow.keras.Model: El modelo CNN cargado.
    """
    model_cnn = tf.keras.models.load_model("conv_MLP_84.h5")
    return model_cnn


def predict(array):
    """
    Predice la clase de una imagen y genera un mapa de calor (heatmap) utilizando Grad-CAM.

    Args:
        array (numpy.ndarray): La imagen de entrada en formato de matriz numpy.

    Returns:
        tuple: Una tupla que contiene:
            - label (str): La etiqueta de la clase predicha (bacteriana, normal, viral).
            - proba (float): La probabilidad de la clase predicha en porcentaje.
            - heatmap (numpy.ndarray): La imagen original superpuesta con el mapa de calor.
    """
    from utils.preprocess_utils import preprocess
    from utils.grad_cam_utils import grad_cam

    #   1. call function to pre-process image: it returns image in batch format
    batch_array_img = preprocess(array)
    #   2. call function to load model and predict: it returns predicted class and probability
    model = model_fun()
    prediction = np.argmax(model.predict(batch_array_img))
    proba = np.max(model.predict(batch_array_img)) * 100
    label = ""
    if prediction == 0:
        label = "bacteriana"
    if prediction == 1:
        label = "normal"
    if prediction == 2:
        label = "viral"
    #   3. call function to generate Grad-CAM: it returns an image with a superimposed heatmap
    heatmap = grad_cam(array)
    return (label, proba, heatmap)
