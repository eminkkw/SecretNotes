from tkinter import *
from tkinter import messagebox
import base64

# Window
window = Tk()
window.title("Secret Notes")
window.minsize(width=400, height=600)

def dosyaya_kayit_1():
    veri = entry_1.get()
    metin = text_1.get("1.0", END)

    if veri == "" or metin == "":
        messagebox.showerror("Hata", "Başlık veya Metin boş bırakılamaz!")
    else:
        encoded_metin = base64.b64encode(metin.encode('utf-8'))

        with open("bilgiler.txt", "a") as dosya:
            dosya.write(veri + encoded_metin.decode('utf-8') + "\n")

def dosyadan_oku():
    with open("bilgiler.txt", "r") as dosya:
        veriler = dosya.readlines()

    for veri in veriler:
        # Başlık ve encoded metin arasındaki boşluğu bul
        bosluk_indeksi = veri.find(" ")
        baslik = veri[:bosluk_indeksi]
        encoded_metin = veri[bosluk_indeksi + 1:]

        # Decode edilmiş metni al
        decoded_metin = base64.b64decode(encoded_metin.encode('utf-8')).decode('utf-8')

        # Başlık ve metni ekrana yazdır
        print("Başlık:", baslik)
        print("Metin:", decoded_metin)
        print("-----------")

# Image
resim = PhotoImage(file="indir.png")

# Label_Image
label_image = Label(image=resim)
label_image.config(width=90, height=90)
label_image.pack()

# Label_1
label_1 = Label(text="Enter your title")
label_1.config(font=("normal", 14))
label_1.place(x=130, y=135)

# Entry_1
entry_1 = Entry(width=35)
entry_1.place(x=90, y=170)

# Label_2
label_2 = Label(text="Enter your secret")
label_2.config(font=("normal", 14))
label_2.place(x=120, y=200)

# Text_1
text_1 = Text(width=35, height=10)
text_1.place(x=50, y=240)

# Label_3
label_3 = Label(text="Enter master key")
label_3.config(font=("normal", 14))
label_3.place(x=110, y=410)

# Entry_2
entry_2 = Entry(width=35)
entry_2.place(x=90, y=450)

# Button_1
button_1 = Button(text="Save & Encrypt", command=dosyaya_kayit_1)
button_1.config(width=12, height=2)
button_1.place(x=130, y=490)

# Button_2
button_2 = Button(text="Decrypt", command=dosyadan_oku)
button_2.config(width=8, height=1)
button_2.place(x=145, y=540)

window.mainloop()
