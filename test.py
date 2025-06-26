import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Tworzymy wykres matplotlib
fig, ax = plt.subplots(figsize=(4, 2))
ax.axis('off')  # bez osi

# Rysujemy nawias nad tekstem
ax.text(0.5, 0.3, r"$\overbrace{\text{a + b + c}}^{\text{grupa}}$",
        fontsize=18, ha='center')

# Tworzymy okno Tkinter
root = tk.Tk()
root.title("Wygładzony nawias")

# Wstawiamy matplotlib do okna Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()

root.mainloop()
