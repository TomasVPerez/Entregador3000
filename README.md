# Entregador 3000
## Automatizador de entregas virtuales
Creación de documento Word automatizado ya que en las pruebas online no nos dan tiempo extra para sacar fotos a lo que hicimos y prepararlo.
### ¿Cómo funciona?

-Se sacan las fotos a la entrega y se pasan por WppWeb para descargarlas desde la pc

-Se inicia el programa e ingresamos el nombre que queremos ponerle al documento y un encabezado para el mismo.

-El programa busca todas las imagenes descargadas desde WppWeb en la ultima hora y las agrega al documento por orden de descarga.

-Finalmente crea una carpeta en el escritorio con el documento dentro.
 
 Para crear un ejecutable abrir cmd e instalar pyinstaller:
 
 ```
 pip install pyinstaller
 ```
 
 Abrir powershell en el directorio donde se encuentra el programa y escribir:
 ```
 pyinstaller --onefile -i rayo.ico Entregador3000.py #-i para usar el icono para el ejecutable (el icono debe estar en el mismo directorio que el programa).
 ```
 
### Restricciones (por ahora):

-Solo funciona para Windows en inglés.

-Las imagenes deben mandarse a WppWeb de a una. Si se seleccionan todas y se envían desde un solo mensaje, Windows detecta como si se descargaran todas a la misma hora exacta por lo que no se subirán en orden al documento.
