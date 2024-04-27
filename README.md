# Generador de Códigos QR

## Descripción
Este proyecto incluye dos componentes principales:
1. Una API construida con FastAPI que permite generar códigos QR desde datos enviados a través de HTTP.
2. Una aplicación de escritorio con interfaz gráfica, desarrollada con `tkinter`, que permite a los usuarios generar códigos QR a partir de una URL o de datos introducidos manualmente.

## Autores
- Alfonso Garcia Yague
- Emmanuel Acosta

---

## API de Generación de Códigos QR con FastAPI

### Descripción de la API
La API permite a los usuarios enviar datos a través de un endpoint y recibir como respuesta un código QR generado basado en esos datos.

### Instalación y Ejecución
Para instalar y ejecutar la API, necesitarás Python y algunas dependencias.

#### Dependencias
- `fastapi`
- `uvicorn`
- `qrcode`
- `Pillow`

Instala las dependencias usando:
```bash
pip install fastapi uvicorn qrcode Pillow
```

#### Ejecución
Para ejecutar la API:
```bash
uvicorn main:app --reload
```
Esto iniciará el servidor en `http://127.0.0.1:8000`.

### Uso
#### Endpoint `/generate-qr/`
- Método: POST
- Enviar JSON: `{"data": "Texto o URL a convertir en QR"}`
- Retorna: Imagen del código QR como respuesta directa.

---

## Aplicación GUI para Generación de Códigos QR

### Descripción de la Aplicación GUI
La aplicación de escritorio permite a los usuarios generar códigos QR desde una interfaz simple y amigable.

### Instalación y Ejecución
#### Dependencias
- `tkinter` (generalmente incluido con Python)
- `qrcode`
- `Pillow`

Instala las dependencias necesarias (excepto `tkinter` que ya debería estar instalado):
```bash
pip install qrcode Pillow
```

#### Ejecución
Para ejecutar la aplicación GUI:
```bash
python main.py
```

### Funcionalidades
- **Generar QR desde URL**: Introduce una URL para generar un código QR.
- **Generar QR desde Datos de Entrada**: Introduce cualquier texto para generar un código QR.

### Interfaz
La aplicación cuenta con campos de entrada para los datos o URL, botones para generar el QR, y un área para mostrar el QR generado.
