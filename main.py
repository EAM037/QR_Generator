#Interfaz Grafica para generador de QRs con URL o INPUT
#Autores: Alfonso Garcia Yague & Emmanuel Acosta

import tkinter as tk
from tkinter import messagebox, simpledialog, Frame
import qrcode
from PIL import Image, ImageTk
import os

def generate_qr_from_url():
    url = url_entry.get().strip()
    if url:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        
        photo = ImageTk.PhotoImage(image=img)
        qr_label.config(image=photo)
        qr_label.image = photo  
    else:
        messagebox.showinfo("Error", "Please enter a URL first!")

def generate_qr_from_input():
    data = simpledialog.askstring("Input", "Enter the data you want to encode:")
    filename = simpledialog.askstring("Input", "Enter the filename for the QR code (without extension):")
    if data and filename:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        directory = os.path.dirname(os.path.realpath(__file__))
        full_path = os.path.join(directory, filename + '.png')
        img.save(full_path)
        messagebox.showinfo("Success", f"QR code saved as {full_path}")
    else:
        messagebox.showinfo("Error", "Please provide both data and a filename.")

root = tk.Tk()
root.title("QR Generator")
root.config(bg='#f0f0f0')  

header_frame = Frame(root, bg='#333333')
header_frame.pack(fill='x', pady=(0, 20))

title_label = tk.Label(header_frame, text="QR Code Generator", font=("Helvetica", 24, 'bold'), bg='#333333', fg='white')
title_label.pack(pady=20)

url_entry = tk.Entry(root, width=40, font=('Helvetica', 14), bg='white')
url_entry.pack(pady=10, padx=20)

generate_button = tk.Button(root, text="Generate QR Code from URL", command=generate_qr_from_url, font=('Helvetica', 14, 'bold'), bg='#4CAF50', fg='white')
generate_button.pack(pady=(10, 10), padx=20)

input_button = tk.Button(root, text="Generate QR Code from Input", command=generate_qr_from_input, font=('Helvetica', 14, 'bold'), bg='#008CBA', fg='white')
input_button.pack(pady=(10, 20), padx=20)

qr_label = tk.Label(root, bg='#f0f0f0')
qr_label.pack(pady=(10, 20), padx=20)

root.geometry('500x600')  # Width x Height

root.mainloop()
