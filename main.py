import copy
import sqlite3
import json
import tkinter as tk
from tkinter import ttk, font, messagebox

from SekZroMerge import SekZroMerge
from UnitermZrownoleglenie import UnitermZrownoleglenie
from UnitermSekwencja import UnitermSekwencja
from database import *
DB_PATH = "unitermy.db"

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
    canvas.delete("Merged")
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
    value = tk.IntVar()
    def on_radio_change():
        global last_merged_choice
        last_merged_choice = value.get()
        print(f"Zmieniono merge na: {last_merged_choice}")  # dla sprawdzenia


    radio_frame = ttk.Frame(frame)
    radio_frame.grid(row=2, column=1, sticky="e", padx=5, pady=5)

    ttk.Radiobutton(radio_frame, text="A", variable= value, value=1, command=on_radio_change).pack(side="left", padx=5, pady=5)
    ttk.Radiobutton(radio_frame, text="B", variable =value, value=2, command=on_radio_change).pack(side="left", padx=5, pady=5)
    ttk.Radiobutton(radio_frame, text="C", variable = value, value=3, command=on_radio_change).pack(side="left", padx=5, pady=5)

    last_merged_choice = value.get()

    ttk.Button(frame, text="Zamien", command=lambda: (merge(canvas,value.get()),okno3.destroy())).grid(row=3, column=1, padx=5, pady=5)



def dodaj_do_listy():
    nazwa = name_entry.get().strip()
    opis = desc_entry.get().strip()
    global last_merged_choice
    if last_merged_choice is None:
        messagebox.showwarning(
            "UWAGA!",
            "Nie wybrano opcji Merge! Przed zapisaniem proszę wybrać opcję merge!"
        )
        return
    if nazwa:
        listbox.insert(tk.END, nazwa)
        opisy[nazwa] = opis

        data_zrownoleglenie = {
            "linie": zrownoleglenie_uniterm.linie,
            "x": zrownoleglenie_uniterm.x,
            "y": zrownoleglenie_uniterm.y,
            "odstep": zrownoleglenie_uniterm.odstep,
            "offset_x": zrownoleglenie_uniterm.offset_x,
            "offset_y": zrownoleglenie_uniterm.offset_y,
            "czcionka": (zrownoleglenie_uniterm.czcionka.actual()["family"],
                         zrownoleglenie_uniterm.czcionka.actual()["size"]),

        }

        data_sekwencja = {
            "x": sekwencja_uniterm.x,
            "y": sekwencja_uniterm.y,
            "tekst": sekwencja_uniterm.tekst,
            "wysokosc_nawiasu": sekwencja_uniterm.wysokosc_nawiasu,
            "czcionka": (sekwencja_uniterm.czcionka.actual()["family"], sekwencja_uniterm.czcionka.actual()["size"])
        }

        with sqlite3.connect(DB_PATH) as conn:
            c = conn.cursor()
            c.execute("""
                INSERT OR REPLACE INTO unitermy (nazwa, opis, data_zrownoleglenie, data_sekwencja, merged_choice)
                VALUES (?, ?, ?, ?, ?)
            """, (
                nazwa,
                opis,
                json.dumps(data_zrownoleglenie),
                json.dumps(data_sekwencja),
                last_merged_choice
            ))
            conn.commit()
            last_merged_choice = None

        name_entry.delete(0, tk.END)
        desc_entry.delete(0, tk.END)

def odswiez_liste():
    listbox.delete(0, tk.END)
    opisy.clear()

    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("SELECT nazwa, opis FROM unitermy")
        for nazwa, opis in c.fetchall():
            listbox.insert(tk.END, nazwa)
            opisy[nazwa] = opis


def wczytaj_z_listy(nazwa,canvas):
    clear_all()
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("SELECT data_zrownoleglenie, data_sekwencja, merged_choice FROM unitermy WHERE nazwa=?", (nazwa,))
        row = c.fetchone()

    if row:
        dane = {
            "zrownoleglenie": json.loads(row[0]),
            "sekwencja": json.loads(row[1]),
            "merged_choice": row[2]
        }
    if dane:
        # Stworz obiekt
        czcionka_zrow = font.Font(family=dane["zrownoleglenie"]["czcionka"][0],
                                  size=dane["zrownoleglenie"]["czcionka"][1])
        global zrownoleglenie_uniterm,sekwencja_uniterm
        zrownoleglenie_uniterm = UnitermZrownoleglenie(
            linie=dane["zrownoleglenie"]["linie"],
            x=dane["zrownoleglenie"]["x"],
            y=dane["zrownoleglenie"]["y"],
            czcionka=czcionka_zrow,
            odstep=dane["zrownoleglenie"]["odstep"],
            offset_x=dane["zrownoleglenie"]["offset_x"],
            offset_y=dane["zrownoleglenie"]["offset_y"],
        )

        czcionka_seq = font.Font(family=dane["sekwencja"]["czcionka"][0], size=dane["sekwencja"]["czcionka"][1])
        sekwencja_uniterm = UnitermSekwencja(
            x=dane["sekwencja"]["x"],
            y=dane["sekwencja"]["y"],
            czcionka=czcionka_seq,
            tekst=dane["sekwencja"]["tekst"],
            wysokosc_nawiasu=dane["sekwencja"]["wysokosc_nawiasu"]
        )

        # Wyswietlenie na canvas
        zrownoleglenie_uniterm.draw(canvas, dx=0, dy=200, tag="Uniterm2")
        sekwencja_uniterm.draw(canvas, dx=0, dy=0, tag="Uniterm1")
        current_merged_choice = dane["merged_choice"]
        merge(canvas, current_merged_choice)

def on_lisbox_select(event):
    indeks = event.widget.curselection()
    if indeks:
        nazwa = event.widget.get(indeks[0])
        wczytaj_z_listy(nazwa, center_canvas)

def pokaz_opis(event):
    try:
        indeks = listbox.curselection()[0]
        nazwa = listbox.get(indeks)
        opis = opisy.get(nazwa)
        if not opis.strip():
            opis = "Brak opisu"

        okno_opis = tk.Toplevel(root)
        okno_opis.title(f"Opis: {nazwa}")
        ttk.Label(okno_opis,text=opis, wraplength=300).pack(padx=10,pady=10)
        okno_opis.geometry("300x150")

        def usun():
            if messagebox.askyesno("Potwierdzenie",
                                   f"Czy na pewno chcesz usunąć uniterm  '{nazwa}'?"):
                with sqlite3.connect(DB_PATH) as conn:
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM unitermy WHERE nazwa=?",(nazwa,))
                    conn.commit()

                okno_opis.destroy()
                odswiez_liste()

        button_frame = ttk.Frame(okno_opis)
        button_frame.pack(side='bottom', fill='x', pady=10)

        btn_usun = tk.Button(button_frame, text="Usuń", command=usun, bg="red", fg="white", font=("Arial", 10, "bold"))
        btn_usun.pack(padx=10, pady=5, fill='x')

    except IndexError:
        pass

def clear_all():
    center_canvas.delete("all")

#Dane
opisy = {}
uniterm_data = {}
global last_merged_choice
last_merged_choice = None


# Inicjalizacja głównego okna
root = tk.Tk()
root.title("Unitermy")
width = 1200
height = 600
root.geometry(f"{width}x{height}")

# ===== GŁÓWNA RAMKA =====
main_frame = ttk.Frame(root)
main_frame.pack(fill='both', expand=True, padx=5, pady=5)

# Lewy panel
left_panel = ttk.Frame(main_frame, width=100)
left_panel.pack(side='left', fill='y')
label = ttk.Label(left_panel, text="Lista Unitermów", font=("Arial", 12, "bold"))
label.pack(padx=5, pady=(5, 0))

listbox = tk.Listbox(left_panel)
listbox.pack(fill = "both", expand = True, padx = 5, pady = 5)

listbox.bind("<Double-Button-1>",pokaz_opis)
listbox.bind("<<ListboxSelect>>",on_lisbox_select)


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
ttk.Button(right_panel, text="Zrównoleglenie", command=lambda: zrownoleglenie_window_open(center_canvas)).pack(pady=10)
ttk.Button(right_panel, text="Merge", command=lambda: openMergeWindow(center_canvas)).pack(pady=10)

# Dodatkowe przyciski
ttk.Button(right_panel, text="Wyczyść",command=clear_all).pack( side= "bottom",pady=5)

# ===== DOLNY PANEL =====
bottom_frame = ttk.Frame(root)
bottom_frame.pack(fill='x', padx=5, pady=5)

ttk.Label(bottom_frame, text="Nazwa:").pack(side='left')
name_entry = ttk.Entry(bottom_frame, width=20)
name_entry.pack(side='left', padx=5)

ttk.Label(bottom_frame, text="Opis:").pack(side='left')
desc_entry = ttk.Entry(bottom_frame, width=40)
desc_entry.pack(side='left', padx=5)

ttk.Button(bottom_frame, text="Dodaj", command = dodaj_do_listy).pack(side='left')

# ===== START PĘTLI APLIKACJI =====
init_db()
odswiez_liste()
root.mainloop()
