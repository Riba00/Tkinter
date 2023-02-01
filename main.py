import tkinter as tk
def sumar():
    numero = int(numeroLabel.cget("text")) + 1
    numeroLabel.config(text=str(numero))
def restar():
    numero = int(numeroLabel.cget("text")) - 1
    numeroLabel.config(text=str(numero))


window = tk.Tk()
window.geometry("400x300")

sumarButton = tk.Button(master=window, text="+", command=sumar)
numeroLabel = tk.Label(master=window, text="0", width="20")
restarButton = tk.Button(master=window, text="-", command=restar)

restarButton.pack(side="left", expand=True)
numeroLabel.pack(side="left", expand=True)
sumarButton.pack(side="left", expand=True)

window.mainloop()
