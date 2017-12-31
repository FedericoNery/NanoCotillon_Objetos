from tkinter import Tk, Label, Button

class GUIAgregarArticulo:
    def __init__(self, master):
        self.master = master
        master.title("AGREGAR ARTICULO")
        master.geometry("565x500+400+50")

        self.greet_button = Button(self.master, text="Greet", command=self.hola)
        self.greet_button.pack()

        self.close_button = Button(self.master, text="Close", command=master.quit)
        self.close_button.pack()

    def hola(self):
        pass

    def chau(self):
        pass

    def crearVentana(self):
        self.root = Tk()
        self.my_gui = GUIAgregarArticulo(self.root)
        self.root.mainloop()