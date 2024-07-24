"""
file_utils.py
-------------

Este módulo contiene funciones para leer archivos de imágenes en formato DICOM y JPG.
"""

from PIL import Image
import cv2
import numpy as np
import pydicom as dicom


def read_dicom_file(path):
    """
    Lee un archivo DICOM y convierte la imagen a formato RGB y a un formato compatible con PIL.

    Args:
        path (str): La ruta del archivo DICOM.

    Returns:
        tuple: Una tupla que contiene:
            - img_RGB (numpy.ndarray): La imagen convertida a formato RGB.
            - img2show (PIL.Image.Image): La imagen en un formato compatible con PIL.
    """
    img = dicom.dcmread(path)
    img_array = img.pixel_array
    img2show = Image.fromarray(img_array)
    img2 = img_array.astype(float)
    img2 = (np.maximum(img2, 0) / img2.max()) * 255.0
    img2 = np.uint8(img2)
    img_RGB = cv2.cvtColor(img2, cv2.COLOR_GRAY2RGB)
    return img_RGB, img2show


def read_jpg_file(path):
    """
    Lee un archivo JPG y convierte la imagen a un formato compatible con PIL.

    Args:
        path (str): La ruta del archivo JPG.

    Returns:
        tuple: Una tupla que contiene:
            - img2 (numpy.ndarray): La imagen en formato numpy.
            - img2show (PIL.Image.Image): La imagen en un formato compatible con PIL.
    """
    img = cv2.imread(path)
    img_array = np.asarray(img)
    img2show = Image.fromarray(img_array)
    img2 = img_array.astype(float)
    img2 = (np.maximum(img2, 0) / img2.max()) * 255.0
    img2 = np.uint8(img2)
    return img2, img2show
