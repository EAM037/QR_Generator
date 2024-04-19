#Interfaz Grafica para generador de QRs con URL 
#Autores: Alfonso Garcia Yague & Emmanuel Acosta

import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

def generate_qr():
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

root = tk.Tk()
root.title("QR Generator with URL")
root.config(bg='#f0f0f0')  

title_label = tk.Label(root, text="QR Generator with URL", font=("Helvetica", 24, 'bold'), bg='#f0f0f0', fg='black')
title_label.pack(pady=(20, 10), padx=20)

url_entry = tk.Entry(root, width=40, font=('Helvetica', 14), bg='white')
url_entry.pack(pady=10, padx=20)

generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr, font=('Helvetica', 14, 'bold'), bg='black', fg='white')
generate_button.pack(pady=(10, 20), padx=20)

qr_label = tk.Label(root, bg='#f0f0f0')
qr_label.pack(pady=(10, 20), padx=20)

root.geometry('500x600')  # Width x Height

root.mainloop()
