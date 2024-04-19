# Generador de Códigos QR con URL

Esta es una aplicación de escritorio simple que genera códigos QR basados en URLs proporcionadas por el usuario. Está construida utilizando Python y tkinter, y está diseñada para ser amigable y minimalista.

## Prerrequisitos

Antes de ejecutar esta aplicación, asegúrate de tener Python instalado en tu computadora. Esta aplicación ha sido probada con Python 3.8, pero debería funcionar con cualquier versión de Python 3.x.

Puedes descargar Python desde [python.org](https://www.python.org/downloads/).

## Instalación

Para ejecutar esta aplicación, necesitarás instalar un par de bibliotecas de Python: `qrcode` y `Pillow`. Aquí están los pasos para configurar tu entorno:

1. **Clona o Descarga el Repositorio**

   Primero, clona el repositorio en tu máquina local o descarga el código fuente como un archivo zip y extrae los archivos.

   ```bash
   git clone https://tu-url-del-repositorio.git
   cd generador-codigo-qr
Crea un Entorno Virtual (Opcional)Es una buena práctica crear un entorno virtual para proyectos de Python. Esto mantiene las dependencias de tu proyecto separadas del entorno global de Python.
bash
Copy code
python -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
Instala las DependenciasInstala las bibliotecas de Python requeridas usando pip:
bash
Copy code
pip install qrcode[pil]
Ejecutando la Aplicación

Para ejecutar la aplicación, navega al directorio del proyecto en tu terminal y ejecuta el script de Python:

bash
Copy code
python qr_generator.py
Uso

Iniciar la AplicaciónEjecuta el script como se mencionó anteriormente. Se abrirá la ventana de la aplicación.
Ingresa una URLEscribe o pega la URL para la cual deseas generar un código QR en el campo de entrada.
Genera el Código QRHaz clic en el botón "Generar Código QR". El código QR aparecerá debajo del botón en la ventana de la aplicación.
Guardar el Código QR (Opcional)Puedes hacer clic derecho en la imagen del código QR generado en la aplicación y guardarla en tu computadora.
