import tkinter as tk
def calcular():
    farenheit = float(entrada_usuari.get())
    celsius = str((farenheit - 32) * 5/9)[:6]
    resultatLabel.config(text=celsius+" ºC")



window = tk.Tk()
window.geometry("500x100")
entrada_usuari = tk.Entry(master=window)

calculateButton = tk.Button(master=window, text="Calcular", command=calcular)

resultatLabel = tk.Label(master=window, text="",width="20")

entrada_usuari.pack(side="left")
calculateButton.pack(side="left")
resultatLabel.pack(side="left")



window.mainloop()
