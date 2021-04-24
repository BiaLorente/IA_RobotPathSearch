from tkinter import *

def run():
    print("Chama funcao A*")


screen = Tk()
screen.title("Buscas - IA")
screen.geometry("300x200")
screen.configure(bg='black')

welcome_text = Label(text = "| Buscas |", fg = "blue", bg= "gray")
welcome_text.pack()

click_me = Button(text = "Busca A*", fg = "blue", bg= "gray", command = run, width = 20)
click_me.place(x = 75, y = 50)
click_me = Button(text = "Busca BCCU", fg = "blue", bg= "gray", command = run, width = 20)
click_me.place(x = 75, y = 75)
click_me = Button(text = "Mapa", fg = "blue", bg= "gray", command = run, width = 20)
click_me.place(x = 75, y = 100)
click_me = Button(text = "Fechar", fg = "red", bg= "gray", command = run, width = 20)
click_me.place(x = 75, y = 150)
screen.mainloop()
