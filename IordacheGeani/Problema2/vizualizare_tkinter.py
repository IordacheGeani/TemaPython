import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import tkinter as tk
from tkinter import ttk

file_path = r"C:\Users\Geanis\Desktop\TemaPython\data.csv"
df = pd.read_csv(file_path)

current_canvas = None

def show_plot(fig):
    global current_canvas
    if current_canvas is not None:
        current_canvas.get_tk_widget().destroy()
    current_canvas = FigureCanvasTkAgg(fig, master=root)
    current_canvas.draw()
    current_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

def plot_all_values():
    fig, ax = plt.subplots()
    df.plot(ax=ax)
    ax.set_title("Toate valorile")
    ax.set_xlabel("Index")
    ax.set_ylabel("Valori")
    show_plot(fig)

def plot_first_8_values():
    fig, ax = plt.subplots()
    df.head(8).plot(ax=ax)
    ax.set_title("Primele 8 valori")
    ax.set_xlabel("Index")
    ax.set_ylabel("Valori")
    show_plot(fig)

def plot_last_12_values():
    fig, ax = plt.subplots()
    df[['Durata', 'Puls']].tail(12).plot(ax=ax)
    ax.set_title("Ultimele 12 valori pentru Durata și Puls")
    ax.set_xlabel("Index")
    ax.set_ylabel("Valori")
    show_plot(fig)

root = tk.Tk()
root.title("Vizualizare date")
root.geometry("800x600") 

frame = ttk.Frame(root, padding="10")
frame.pack(fill=tk.BOTH, expand=True)

btn_all_values = ttk.Button(frame, text="Toate valorile", command=plot_all_values)
btn_all_values.pack(pady=5)

btn_first_8 = ttk.Button(frame, text="Primele 8 valori", command=plot_first_8_values)
btn_first_8.pack(pady=5)

btn_last_12 = ttk.Button(frame, text="Ultimele 12 valori (Durata și Puls)", command=plot_last_12_values)
btn_last_12.pack(pady=5)

root.mainloop()
