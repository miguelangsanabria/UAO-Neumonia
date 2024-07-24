#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
main.py
-------

Este archivo es el punto de entrada principal de la aplicación para la detección rápida de neumonía.
Inicializa y ejecuta la aplicación utilizando la clase App definida en views.main_view.
"""

from views.main_view import App

def main():
    """
    Función principal que inicializa y ejecuta la aplicación.
    Crea una instancia de la clase App y la inicia.

    Returns:
        int: Código de salida del programa (0 si se ejecuta correctamente).
    """

    my_app = App()
    return 0

if __name__ == "__main__":
    main()
