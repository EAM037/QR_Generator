# Generador de Códigos QR

## Descripción
Esta aplicación permite a los usuarios generar códigos QR a partir de una URL o de datos introducidos manualmente. La interfaz gráfica está desarrollada utilizando `tkinter`, haciendo que la aplicación sea fácil de usar y accesible para cualquier usuario con conocimientos básicos de computación.

## Autores
- Alfonso Garcia Yague
- Emmanuel Acosta

## Dependencias
Para ejecutar esta aplicación, necesitarás Python y algunas bibliotecas externas. Asegúrate de tener instalado Python en tu sistema. Esta aplicación ha sido probada con Python 3.8, pero debería ser compatible con versiones posteriores.

### Bibliotecas necesarias:
- `tkinter`: Para la interfaz gráfica de usuario. `tkinter` suele venir preinstalado con Python.
- `qrcode`: Para la generación de códigos QR.
- `Pillow` (PIL Fork): Para manejar imágenes dentro de la aplicación.

Puedes instalar las dependencias necesarias mediante el siguiente comando:
pip install qrcode Pillow

Nota: `tkinter` generalmente viene incluido en la instalación estándar de Python. Si tu instalación de Python no lo incluye, puedes necesitar instalarlo siguiendo las instrucciones específicas para tu sistema operativo.

## Ejecución del Programa
Para ejecutar esta aplicación, simplemente navega hasta el directorio del archivo y ejecuta el script `main.py` usando Python. Por ejemplo:
python main.py


## Funcionalidades
- **Generar QR desde URL**: Permite a los usuarios introducir una URL para generar un código QR correspondiente.
- **Generar QR desde Datos de Entrada**: Permite a los usuarios introducir cualquier texto o dato para generar un código QR.

## Interfaz Gráfica
La interfaz gráfica cuenta con un campo de entrada para los datos o URL, botones para generar el código QR y un área donde se muestra el código QR generado.
