from tkinter import Tk, Label, Button

class GUIAgregarArticulo:
    def __init__(self, master):
        self.master = master
        master.title("AGREGAR ARTICULO")

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def crearVentana(self):
        self.root = Tk()
        self.my_gui = GUIAgregarArticulo(self.root)
        self.root.mainloop()