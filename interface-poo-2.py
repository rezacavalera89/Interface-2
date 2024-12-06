from tkinter import *
from tkinter import messagebox


def somar():
    try:
        v1 = int(campo1.get())
        v2 = int(campo2.get())
        resultado = v1 + v2
        campo_total['state'] = 'normal'
        campo_total.delete(0, END)
        campo_total.insert(0, str(resultado))
        campo_total['state'] = 'readonly'  
    except ValueError:
        messagebox.showerror("Erro", "Insira valores válidos!")


janela = Tk()
janela.title("Somador")
janela.geometry("250x120")

Label(janela, text="Valor 1:").grid(row=0, column=0, padx=5, pady=5)
campo1 = Entry(janela)
campo1.grid(row=0, column=1)

Label(janela, text="Valor 2:").grid(row=1, column=0, padx=5, pady=5)
campo2 = Entry(janela)
campo2.grid(row=1, column=1)

Label(janela, text="Total:").grid(row=2, column=0, padx=5, pady=5)
campo_total = Entry(janela, state='readonly')  
campo_total.grid(row=2, column=1)

Button(janela, text="Somar", command=somar).grid(row=3, column=1, pady=10)

janela.mainloop()
