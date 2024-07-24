<h1 align="center">Proyecto Neumonía 💻</h1>

<h4 align="center">Proyecto realizado por <a href="https://github.com/miguelangsanabria" target="_blank">Miguel Angel Sanabria</a> - Código 2240373 para la asignatura de Desarrollo de Proyectos de Inteligencia Artificial.</h4>

> Deep Learning aplicado en el procesamiento de imágenes radiográficas de tórax en formato `DICOM` con el fin de clasificarlas en 3 categorías diferentes:
> 1. Neumonía Bacteriana
> 2. Neumonía Viral
> 3. Sin Neumonía
> 
> Aplicación de una técnica de explicación llamada `Grad-CAM` para resaltar con un mapa de calor las regiones relevantes de la imagen de entrada.

## 📂 Estructura del Proyecto

```
UAO-neumonia/
│
├── main.py             # Archivo principal para ejecutar la aplicación
├── requirements.txt    # Dependencias del proyecto
├── README.md           # Descripción del proyecto
├── Dockerfile          # Archivo de configuración de la imagen de Docker
├── pytest.ini          # Archivo de configuración para las pruebas
├── utils/              # Módulos de utilidad
│   └── __init__.py
│   └── file_utils.py
│   └── grad_cam_utils.py
│   └── model_utils.py
│   └── preprocess_utils.py
├── views/              # Definición de las vistas (ventanas, frames, etc.)
│   └── __init__.py
│   └── main_view.py
├── images/             # Imagenes de ejemplo
│   └── *.dcm
│   └── *.jpeg
└── tests/              # Pruebas del proyecto
    └── __init__.py
    └── test_predict.py
    └── test_preprocess.py
```

## 🔧 Requisitos

- Anaconda ([Instrucciones para Windows]( https://docs.anaconda.com/anaconda/install/windows/))
- [Docker](https://docs.docker.com/get-docker/)
- [Xserver para Windows](https://sourceforge.net/projects/vcxsrv/) (Opcional)

## 🚀 Uso

1. Abrir una terminal (preferiblemente `Powershell` en Windows) y ejecutar el comando para crear un entorno virtual:
   
   ```sh
   conda create -n tf tensorflow
   ```
   
3. Activa el entorno virtual:
   
   ```sh
   conda activate tf
   ```
   
3. Ve a la carpeta del proyecto
   
   ```sh
   cd UAO-Neumonia
   ```

4. Descarga el modelo de https://drive.google.com/file/d/1aVHdgd4yKJn2C92eqqKS0TW3GKq3QjWd/view?usp=sharing y colocalo en la carpeta del proyeco
   
5. Instala las dependencias necesarias
   
   ```sh
   pip install -r requirements.txt
   ```

6. Ejecuta la Aplicación
   
   ```sh
   python main.py
   ```
   
## 📲 Uso de la Interfaz Gráfica 

- Ingrese la cédula del paciente en la caja de texto
- Presione el botón 'Cargar Imagen', seleccione la imagen del explorador de archivos del computador (Imagenes de prueba en https://drive.google.com/drive/folders/1WOuL0wdVC6aojy8IfssHcqZ4Up14dy0g?usp=drive_link)
- Presione el botón 'Predecir' y espere unos segundos hasta que observe los resultados
- Presione el botón 'Guardar' para almacenar la información del paciente en un archivo excel con extensión .csv
- Presione el botón 'PDF' para descargar un archivo PDF con la información desplegada en la interfaz
- Presión el botón 'Borrar' si desea cargar una nueva imagen

## ✅ Pruebas

Se realizaron dos pruebas unitarias utilizando `pytest`: 
- **Prueba para la función `preprocess`:** Esta prueba verificará que la imagen se procese correctamente y se convierta en el formato esperado.
- **Prueba para la función `predict`:** Esta prueba verificará que la predicción se realice correctamente y devuelva las etiquetas y probabilidades esperadas.

Se pueden ejecutar las pruebas por medio del comando:
```sh
pytest
```

## 🐳 Instrucciones utilizando Docker

1. El proyecto ya tiene la imagen de Docker configurada en el `Dockerfile` para construirla utiliza el comando dentro de la carpeta del proyecto:

   ```sh
   docker build -t pneumonia-app .
   ```

2. Ejecuta la imagen utilizando: (Para que ejecute correctamente se requiere tener un [Xserver](https://sourceforge.net/projects/vcxsrv/)

   ```sh
   docker run -it pneumonia-app
   ```
   Al momento de cargar imagenes se pueden utilizar las que se encuentran de ejemplo en el Proyecto en la ruta `home/src/images`

3. También se pueden ejecutar las pruebas en el contenedor con:

   ```sh
   docker run -it pneumonia-app pytest
   ```

## 🤖 Acerca del Modelo

La red neuronal convolucional implementada (CNN) es basada en el modelo implementado por F. Pasa, V.Golkov, F. Pfeifer, D. Cremers & D. Pfeifer
en su artículo Efcient Deep Network Architectures for Fast Chest X-Ray Tuberculosis Screening and Visualization.

Está compuesta por 5 bloques convolucionales, cada uno contiene 3 convoluciones; dos secuenciales y una conexión 'skip' que evita el desvanecimiento del gradiente a medida que se avanza en profundidad.
Con 16, 32, 48, 64 y 80 filtros de 3x3 para cada bloque respectivamente.

Después de cada bloque convolucional se encuentra una capa de max pooling y después de la última una capa de Average Pooling seguida por tres capas fully-connected (Dense) de 1024, 1024 y 3 neuronas respectivamente.

Para regularizar el modelo utilizamos 3 capas de Dropout al 20%; dos en los bloques 4 y 5 conv y otra después de la 1ra capa Dense.

## 🩻 Acerca de Grad-CAM

Es una técnica utilizada para resaltar las regiones de una imagen que son importantes para la clasificación. Un mapeo de activaciones de clase para una categoría en particular indica las regiones de imagen relevantes utilizadas por la CNN para identificar esa categoría.

Grad-CAM realiza el cálculo del gradiente de la salida correspondiente a la clase a visualizar con respecto a las neuronas de una cierta capa de la CNN. Esto permite tener información de la importancia de cada neurona en el proceso de decisión de esa clase en particular. Una vez obtenidos estos pesos, se realiza una combinación lineal entre el mapa de activaciones de la capa y los pesos, de esta manera, se captura la importancia del mapa de activaciones para la clase en particular y se ve reflejado en la imagen de entrada como un mapa de calor con intensidades más altas en aquellas regiones relevantes para la red con las que clasificó la imagen en cierta categoría.

## 🧑‍💻 Proyecto original realizado por:

Isabella Torres Revelo - https://github.com/isa-tr
Nicolas Diaz Salazar - https://github.com/nicolasdiazsalazar
