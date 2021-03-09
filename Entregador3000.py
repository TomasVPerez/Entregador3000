import glob
import os
from docx import Document
from docx.shared import Inches

document = Document()

header = document.sections[0].header
header.paragraphs[0].text = input("Materia-NombreyApellido(nroAlumno)-Fecha: ")

nombreEntrega = input("Nombre del entregable: ") 
carpetaDeFotos = input("Nombre de la carpeta de fotos: ")

nuevaCarpeta = (f"C:/Users/Tomas/Desktop/{nombreEntrega}")
os.mkdir(nuevaCarpeta)

fotos = glob.glob(f"C:/Users/Tomas/Desktop/{carpetaDeFotos}/*.jpeg")
for foto in fotos:
    document.add_picture(foto, width=Inches(4.5))

document.save(f"{nuevaCarpeta}/{nombreEntrega}.docx")


