import copy
import tkinter as tk
from tkinter import ttk, font

from SekZroMerge import SekZroMerge
from UnitermZrownoleglenie import UnitermZrownoleglenie
from UnitermSekwencja import UnitermSekwencja


def sekwencja_window_open(canvas):

        def dodaj():
            canvas.delete("Uniterm1")
            a = entry_a.get()
            b = entry_b.get()
            sep = separator_var.get()
            tekst = f"{a} {sep} {b}"
            x = 30
            y = 50
            czcionka = font.Font(family="Arial", size=16)
            wysokosc_nawiasu = 10
            global sekwencja_uniterm
            sekwencja_uniterm = UnitermSekwencja(x,y,czcionka, tekst,wysokosc_nawiasu)
            sekwencja_uniterm.draw(canvas, dx=0, dy=0,tag="Uniterm1")

            okno.destroy()

        okno = tk.Toplevel()
        okno.title("AddUniterm")
        x = 300
        y = 200
        root.update_idletasks()
        main_x = root.winfo_x()
        main_y = root.winfo_y()
        main_width = root.winfo_width()
        main_height = root.winfo_height()

        pos_x = main_x + (main_width // 2) - (x // 2)
        pos_y = main_y + (main_height // 2) - (y // 2)

        # Ustaw rozmiar i pozycję
        okno.geometry(f"{x}x{y}+{pos_x}+{pos_y}")


        #Etykiety
        frame = ttk.Frame(okno, padding=10)
        frame.pack(expand=True, fill ="both")

        #Wyrazenie A
        ttk.Label(frame,text="Wyrazenie A").grid(row=0, column=0, sticky="e",padx=5,pady=5)
        entry_a = ttk.Entry(frame, width=25)
        entry_a.grid(row=0, column=1, pady=5)

        #Wyrazenie B
        ttk.Label(frame, text="Wyrazenie B").grid(row=1, column=0, sticky="e",padx=5,pady=5)
        entry_b = ttk.Entry(frame, width=25)
        entry_b.grid(row=1, column=1, pady=5)

        ttk.Label(frame,text="Operacja").grid(row=2, column=0, sticky="e",padx=5,pady=5)
        separator_var = tk.StringVar(value=";")

        radio_frame =ttk.Frame(frame)
        radio_frame.grid(row=2, column=1, sticky="e",padx=5,pady=5)

        ttk.Radiobutton(radio_frame, text=";", variable=separator_var,value=";").pack(side="left",padx=5,pady=5)
        ttk.Radiobutton(radio_frame,text=",",variable=separator_var,value=",").pack(side="left",padx=5,pady=5)

        ttk.Button(frame,text="Dodaj", command=dodaj).grid(row=3,column=1,padx=5,pady=5)
def wyswietl_uniterm_sekwencja(canvas, uniterm,dx = 0, dy = 0):
                x = uniterm["x"]+dx
                y = uniterm["y"]+dy
                tekst = uniterm["tekst"]
                czcionka = uniterm["czcionka"]
                szerokosc_tekstu = uniterm["szerokosc_tekstu"]
                wysokosc_nawiasu = uniterm["wysokosc_nawiasu"]

                canvas.create_text(x,y, text=tekst, anchor="nw", font=czcionka, tags="uniterm1")
                canvas.create_arc(x, y - wysokosc_nawiasu,
                                         x + szerokosc_tekstu, y + 5,
                                         start=0, extent=180, style='arc', width=2, outline="blue",tags="uniterm1")


def zrownoleglenie_window_open(canvas):

        def dodaj():
            canvas.delete("Uniterm2")
            a = entry_a.get()
            b = entry_b.get()
            c = entry_c.get()
            sep = separator_var.get()
            czcionka = font.Font(family="Arial", size=16)
            linie = [a, sep, b, sep, c]
            odstep = 5

            global zrownoleglenie_uniterm
            zrownoleglenie_uniterm = UnitermZrownoleglenie(
                linie=linie,
                x=30,
                y=50,
                czcionka=czcionka,
                odstep=odstep,
                offset_x=10,
                offset_y=5
            )

            zrownoleglenie_uniterm.draw(canvas, dx=0, dy=200,tag="Uniterm2")
            okno2.destroy()

        okno2 = tk.Toplevel()
        okno2.title("AddUniterm")
        x = 300
        y = 200
        root.update_idletasks()
        main_x = root.winfo_x()
        main_y = root.winfo_y()
        main_width = root.winfo_width()
        main_height = root.winfo_height()

        pos_x = main_x + (main_width // 2) - (x // 2)
        pos_y = main_y + (main_height // 2) - (y // 2)

        # Ustaw rozmiar i pozycję
        okno2.geometry(f"{x}x{y}+{pos_x}+{pos_y}")

        #Etykiety
        frame = ttk.Frame(okno2, padding=10)
        frame.pack(expand=True, fill ="both")

        #Wyrazenie A
        ttk.Label(frame,text="Wyrazenie A").grid(row=0, column=0, sticky="e",padx=5,pady=5)
        entry_a = ttk.Entry(frame, width=25)
        entry_a.grid(row=0, column=1, pady=5)

        #Wyrazenie B
        ttk.Label(frame, text="Wyrazenie B").grid(row=1, column=0, sticky="e",padx=5,pady=5)
        entry_b = ttk.Entry(frame, width=25)
        entry_b.grid(row=1, column=1, pady=5)

        #Wyrazenie C
        ttk.Label(frame, text="Wyrazenie C").grid(row=2, column=0, sticky="e",padx=5,pady=5)
        entry_c = ttk.Entry(frame, width=25)
        entry_c.grid(row=2, column=1, pady=5)

        ttk.Label(frame,text="Operacja").grid(row=3, column=0, sticky="e",padx=5,pady=5)
        separator_var = tk.StringVar(value=";")

        radio_frame =ttk.Frame(frame)
        radio_frame.grid(row=3, column=1, sticky="e",padx=5,pady=5)

        ttk.Radiobutton(radio_frame, text=";", variable=separator_var,value=";").pack(side="left",padx=5,pady=5)
        ttk.Radiobutton(radio_frame,text=",",variable=separator_var,value=",").pack(side="left",padx=5,pady=5)

        ttk.Button(frame,text="Dodaj", command=dodaj).grid(row=4,column=1,padx=5,pady=5)

def merge(canvas, a):

    mergedUniterm = SekZroMerge(zrownoleglenie_uniterm, sekwencja_uniterm,a)
    mergedUniterm.draw(canvas,tag="Merged")


def openMergeWindow(canvas):
    canvas.delete("Merged")
    okno3 = tk.Toplevel()
    okno3.title("MergeUniterm")
    x = 300
    y = 200
    root.update_idletasks()
    main_x = root.winfo_x()
    main_y = root.winfo_y()
    main_width = root.winfo_width()
    main_height = root.winfo_height()

    pos_x = main_x + (main_width // 2) - (x // 2)
    pos_y = main_y + (main_height // 2) - (y // 2)

    # Ustaw rozmiar i pozycję
    okno3.geometry(f"{x}x{y}+{pos_x}+{pos_y}")

    # Etykiety
    frame = ttk.Frame(okno3, padding=10)
    frame.pack(expand=True, fill="both")

    # Wyrazenie A

    ttk.Label(frame, text="Operacja").grid(row=2, column=0, sticky="e", padx=5, pady=5)
    separator_var = tk.StringVar(value=";")

    radio_frame = ttk.Frame(frame)
    radio_frame.grid(row=2, column=1, sticky="e", padx=5, pady=5)
    value = tk.IntVar(value=1)
    ttk.Radiobutton(radio_frame, text="A", variable= value, value=1).pack(side="left", padx=5, pady=5)
    ttk.Radiobutton(radio_frame, text="B", variable =value, value=2).pack(side="left", padx=5, pady=5)
    ttk.Radiobutton(radio_frame, text="C", variable = value, value=3).pack(side="left", padx=5, pady=5)
    ttk.Button(frame, text="Zamien", command=lambda: (merge(canvas,value.get()),okno3.destroy())).grid(row=3, column=1, padx=5, pady=5)


# Inicjalizacja głównego okna

root = tk.Tk()
root.title("Unitermy")
width = 1200
height = 600
root.geometry(f"{width}x{height}")

# ===== MENU GÓRNE =====
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Otwórz")
file_menu.add_command(label="Zapisz")
file_menu.add_separator()
file_menu.add_command(label="Zamknij", command=root.quit)
menu_bar.add_cascade(label="Plik", menu=file_menu)
root.config(menu=menu_bar)

# ===== GŁÓWNA RAMKA =====
main_frame = ttk.Frame(root)
main_frame.pack(fill='both', expand=True, padx=5, pady=5)

# Lewy panel (np. lista lub pusta kolumna)
left_panel = ttk.Frame(main_frame, width=100)
left_panel.pack(side='left', fill='y')

# Centrum - przestrzeń robocza
center_canvas = tk.Canvas(
        main_frame,
        bg="white",
        highlightthickness=1,
        highlightbackground="black",)
center_canvas.pack(side='left', fill='both', expand=True)

# Prawy panel z kontrolkami
right_panel = ttk.Frame(main_frame, width=150)
right_panel.pack(side='right', fill='y', padx=5)

# Przyciski
ttk.Button(right_panel, text="Sekwencjonuj", command=lambda: sekwencja_window_open(center_canvas)).pack(pady=5)
ttk.Button(right_panel, text="Zrównoleglenie", command=lambda: zrownoleglenie_window_open(center_canvas)).pack(pady=5)
ttk.Button(right_panel, text="Merge", command=lambda: openMergeWindow(center_canvas)).pack(pady=5)

# Czcionka i rozmiar
ttk.Label(right_panel, text="Czcionka").pack(pady=(10, 0))
font_box = ttk.Combobox(right_panel, values=sorted(font.families()))
font_box.set("Arial")
font_box.pack()

ttk.Label(right_panel, text="Rozmiar czcionki").pack(pady=(10, 0))
size_box = ttk.Combobox(right_panel, values=[8, 10, 12, 14, 16, 18, 20])
size_box.set("12")
size_box.pack()

# Dodatkowe przyciski
ttk.Button(right_panel, text="Odśwież").pack(pady=10)
ttk.Button(right_panel, text="Wyczyść").pack(pady=5)

# ===== DOLNY PANEL (Nazwa + Opis) =====
bottom_frame = ttk.Frame(root)
bottom_frame.pack(fill='x', padx=5, pady=5)

ttk.Label(bottom_frame, text="Nazwa:").pack(side='left')
name_entry = ttk.Entry(bottom_frame, width=20)
name_entry.pack(side='left', padx=5)

ttk.Label(bottom_frame, text="Opis:").pack(side='left')
desc_entry = ttk.Entry(bottom_frame, width=40)
desc_entry.pack(side='left', padx=5)

# ===== START PĘTLI APLIKACJI =====
root.mainloop()
