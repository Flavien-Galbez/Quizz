from tkinter import * 

fenetre = Tk()
l = LabelFrame(fenetre, text="Titre de la frame", padx=20, pady=20)
l.pack(fill="both", expand="yes")

Label(l, text="A l'intérieure de la frame").pack()
fenetre.mainloop()
