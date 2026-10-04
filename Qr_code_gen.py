# Qr code generator
import qrcode
import tkinter as tk
from PIL import Image,ImageTk
def generate_qr():
            url=entry.get()
            qr=qrcode.QRCode()
            qr.add_data(url)
            img=qr.make_image(fill_color="blue",back_color="white")
            img.save("qrcode.png")
            img.show()
            label.config(text="QR Code Generated Successfully !!")
root = tk.Tk()
root.title("Qr Code Generator")
bg_image = Image.open("your_image.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)
root.geometry("400x400")
entry = tk.Entry(root)
entry.pack()
button =  tk.Button(root,text="Generate",command=generate_qr)
button.pack()
label = tk.Label(root,text="")
label.pack()
bg_label=tk.Label(root,image=bg_photo)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)
bg_label.lower()
root.mainloop()