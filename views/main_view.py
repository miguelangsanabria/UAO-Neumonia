"""
main_view.py
------------

Este módulo contiene la clase App que maneja la interfaz gráfica de usuario para la herramienta de detección rápida de neumonía.
"""

from tkinter import *
from tkinter import ttk, font, filedialog
from tkinter.messagebox import askokcancel, showinfo, WARNING
from PIL import ImageTk, Image
import csv
import tkcap
from utils.file_utils import read_dicom_file, read_jpg_file
from utils.model_utils import predict
from utils.grad_cam_utils import grad_cam


class App:
    """
    Clase que representa la aplicación principal con la interfaz gráfica de usuario.

    Atributos:
        root (tk.Tk): La ventana principal de la aplicación.
        lab1, lab2, lab3, lab4, lab5, lab6 (ttk.Label): Etiquetas de la interfaz.
        ID (StringVar): Variable para almacenar el ID del paciente.
        result (StringVar): Variable para almacenar el resultado de la predicción.
        text1 (ttk.Entry): Campo de entrada para el ID del paciente.
        text_img1, text_img2 (Text): Campos de texto para mostrar las imágenes.
        text2, text3 (Text): Campos de texto para mostrar los resultados.
        button1, button2, button3, button4, button6 (ttk.Button): Botones de la interfaz.
        array (numpy.ndarray): Arreglo para almacenar la imagen cargada.
        reportID (int): Identificación del reporte para generar PDFs.
    """

    def __init__(self):
        """
        Inicializa la clase App configurando la interfaz gráfica y los widgets.
        """
        self.root = Tk()
        self.root.title("Herramienta para la detección rápida de neumonía")

        #   BOLD FONT
        fonti = font.Font(weight="bold")

        self.root.geometry("815x560")
        self.root.resizable(0, 0)

        #   LABELS
        self.lab1 = ttk.Label(self.root, text="Imagen Radiográfica", font=fonti)
        self.lab2 = ttk.Label(self.root, text="Imagen con Heatmap", font=fonti)
        self.lab3 = ttk.Label(self.root, text="Resultado:", font=fonti)
        self.lab4 = ttk.Label(self.root, text="Cédula Paciente:", font=fonti)
        self.lab5 = ttk.Label(
            self.root,
            text="SOFTWARE PARA EL APOYO AL DIAGNÓSTICO MÉDICO DE NEUMONÍA",
            font=fonti,
        )
        self.lab6 = ttk.Label(self.root, text="Probabilidad:", font=fonti)

        #   TWO STRING VARIABLES TO CONTAIN ID AND RESULT
        self.ID = StringVar()
        self.result = StringVar()

        #   TWO INPUT BOXES
        self.text1 = ttk.Entry(self.root, textvariable=self.ID, width=10)

        #   GET ID
        self.ID_content = self.text1.get()

        #   TWO IMAGE INPUT BOXES
        self.text_img1 = Text(self.root, width=31, height=15)
        self.text_img2 = Text(self.root, width=31, height=15)
        self.text2 = Text(self.root)
        self.text3 = Text(self.root)

        #   BUTTONS
        self.button1 = ttk.Button(
            self.root, text="Predecir", state="disabled", command=self.run_model
        )
        self.button2 = ttk.Button(
            self.root, text="Cargar Imagen", command=self.load_img_file
        )
        self.button3 = ttk.Button(self.root, text="Borrar", command=self.delete)
        self.button4 = ttk.Button(self.root, text="PDF", command=self.create_pdf)
        self.button6 = ttk.Button(
            self.root, text="Guardar", command=self.save_results_csv
        )

        #   WIDGETS POSITIONS
        self.lab1.place(x=110, y=65)
        self.lab2.place(x=545, y=65)
        self.lab3.place(x=500, y=350)
        self.lab4.place(x=65, y=350)
        self.lab5.place(x=122, y=25)
        self.lab6.place(x=500, y=400)
        self.button1.place(x=220, y=460)
        self.button2.place(x=70, y=460)
        self.button3.place(x=670, y=460)
        self.button4.place(x=520, y=460)
        self.button6.place(x=370, y=460)
        self.text1.place(x=200, y=350)
        self.text2.place(x=610, y=350, width=90, height=30)
        self.text3.place(x=610, y=400, width=90, height=30)
        self.text_img1.place(x=65, y=90)
        self.text_img2.place(x=500, y=90)

        #   FOCUS ON PATIENT ID
        self.text1.focus_set()

        #  se reconoce como un elemento de la clase
        self.array = None

        #   NUMERO DE IDENTIFICACIÓN PARA GENERAR PDF
        self.reportID = 0

        #   RUN LOOP
        self.root.mainloop()

    #   METHODS
    def load_img_file(self):
        """
        Abre un cuadro de diálogo para seleccionar una imagen y carga la imagen seleccionada.

        Permite seleccionar archivos DICOM, JPEG, JPG y PNG. La imagen cargada se muestra en la interfaz.
        """
        filepath = filedialog.askopenfilename(
            initialdir="/",
            title="Select image",
            filetypes=(
                ("DICOM", "*.dcm"),
                ("JPEG", "*.jpeg"),
                ("jpg files", "*.jpg"),
                ("png files", "*.png"),
            ),
        )
        if filepath:
            file_extension = filepath.split(".")[-1].lower()
            if file_extension == "dcm":
                self.array, img2show = read_dicom_file(filepath)
            elif file_extension in ["jpg", "jpeg", "png"]:
                self.array, img2show = read_jpg_file(filepath)
            self.img1 = img2show.resize((250, 250), Image.Resampling.LANCZOS)
            self.img1 = ImageTk.PhotoImage(self.img1)
            self.text_img1.image_create(END, image=self.img1)
            self.button1["state"] = "enabled"

    def run_model(self):
        """
        Ejecuta el modelo de predicción sobre la imagen cargada y muestra los resultados en la interfaz.

        La predicción incluye una etiqueta y una probabilidad, además de generar un heatmap.
        """
        self.label, self.proba, self.heatmap = predict(self.array)
        self.img2 = Image.fromarray(self.heatmap)
        self.img2 = self.img2.resize((250, 250), Image.Resampling.LANCZOS)
        self.img2 = ImageTk.PhotoImage(self.img2)
        print("OK")
        self.text_img2.image_create(END, image=self.img2)
        self.text2.insert(END, self.label)
        self.text3.insert(END, "{:.2f}".format(self.proba) + "%")

    def save_results_csv(self):
        """
        Guarda los resultados de la predicción en un archivo CSV.

        Los datos guardados incluyen el ID del paciente, la etiqueta de la predicción y la probabilidad.
        """
        with open("historial.csv", "a") as csvfile:
            w = csv.writer(csvfile, delimiter="-")
            w.writerow(
                [self.text1.get(), self.label, "{:.2f}".format(self.proba) + "%"]
            )
            showinfo(title="Guardar", message="Los datos se guardaron con éxito.")

    def create_pdf(self):
        """
        Captura la pantalla de la aplicación y genera un archivo PDF con la captura.

        El archivo PDF se guarda en el directorio actual con un nombre basado en el ID del reporte.
        """
        cap = tkcap.CAP(self.root)
        ID = "Reporte" + str(self.reportID) + ".jpg"
        img = cap.capture(ID)
        img = Image.open(ID)
        img = img.convert("RGB")
        pdf_path = r"Reporte" + str(self.reportID) + ".pdf"
        img.save(pdf_path)
        self.reportID += 1
        showinfo(title="PDF", message="El PDF fue generado con éxito.")

    def delete(self):
        """
        Borra todos los datos y restablece la interfaz de usuario a su estado inicial.

        Solicita confirmación antes de borrar los datos.
        """
        answer = askokcancel(
            title="Confirmación", message="Se borrarán todos los datos.", icon=WARNING
        )
        if answer:
            self.text1.delete(0, "end")
            self.text2.delete(1.0, "end")
            self.text3.delete(1.0, "end")
            self.text_img1.delete(self.img1, "end")
            self.text_img2.delete(self.img2, "end")
            showinfo(title="Borrar", message="Los datos se borraron con éxito")
