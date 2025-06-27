import copy
import tkinter as tk
from tkinter import ttk, font
from UnitermSekwencja import UnitermSekwencja
from UnitermZrownoleglenie import UnitermZrownoleglenie

class SekZroMerge:
    def __init__(self, zrownoleglenie_uniterm, sekwencja_uniterm, a):
        # Tworzymy nowy obiekt tej samej klasy, kopiując dane:
        self.zrownoleglenie_uniterm = UnitermZrownoleglenie(
            linie=copy.deepcopy(zrownoleglenie_uniterm.linie),
            x=zrownoleglenie_uniterm.x,
            y=zrownoleglenie_uniterm.y,
            czcionka=zrownoleglenie_uniterm.czcionka,
            odstep=zrownoleglenie_uniterm.odstep,
            offset_x=zrownoleglenie_uniterm.offset_x,
            offset_y=zrownoleglenie_uniterm.offset_y
        )

        self.sekwencja_uniterm = UnitermSekwencja(
            x = sekwencja_uniterm.x,
            y = sekwencja_uniterm.y,
            czcionka = sekwencja_uniterm.czcionka,
            tekst = sekwencja_uniterm.tekst,
            wysokosc_nawiasu = sekwencja_uniterm.wysokosc_nawiasu,

        )
        self.a = a


    def draw(self, canvas,tag="Empty"):
        merged_uniterm = self.zrownoleglenie_uniterm
        merged_uniterm.odstep += 10
        merged_uniterm.offset_y += 10

        if self.a == 1:
            merged_uniterm.linie[0] = ""
            merged_uniterm.linie[2] = self.zrownoleglenie_uniterm.linie[2]
            merged_uniterm.linie[4] = self.zrownoleglenie_uniterm.linie[4]
            merged_uniterm.draw(canvas, dx=200, dy=50,tag=tag)
            self.sekwencja_uniterm.draw(canvas, dx=210, dy=60,tag=tag)
            canvas.create_line(100, 80, 220, 110, arrow=tk.LAST, width=5, fill="green",tag=tag)
        elif self.a == 2:
            merged_uniterm.linie[2] = ""
            merged_uniterm.linie[0] = self.zrownoleglenie_uniterm.linie[0]
            merged_uniterm.linie[4] = self.zrownoleglenie_uniterm.linie[4]
            merged_uniterm.draw(canvas, dx=200, dy=50,tag=tag)
            self.sekwencja_uniterm.draw(canvas, dx=210, dy=135,tag=tag)
            canvas.create_line(100, 80, 220, 180, arrow=tk.LAST, width=5, fill="blue",tag=tag)
        elif self.a == 3:
            merged_uniterm.linie[4] = ""
            merged_uniterm.linie[2] = self.zrownoleglenie_uniterm.linie[2]
            merged_uniterm.linie[0] = self.zrownoleglenie_uniterm.linie[0]
            merged_uniterm.draw(canvas, dx=200, dy=50,tag=tag)
            self.sekwencja_uniterm.draw(canvas, dx=210, dy=210,tag=tag)
            canvas.create_line(100, 80, 220, 240, arrow=tk.LAST, width=5, fill="red",tag=tag)