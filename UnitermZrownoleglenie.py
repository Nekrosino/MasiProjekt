from Uniterm import Uniterm


class UnitermZrownoleglenie(Uniterm):

    def __init__(self, linie, x, y, czcionka, odstep=5, offset_x = 10, offset_y = 0):
        super().__init__(x,y, czcionka)
        self.linie = linie
        self.odstep = odstep
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.wysokosc_tekstu = czcionka.metrics("linespace")

    def draw(self, canvas,dx=0,dy=0,tag="Empty"):
        x = self.x + dx
        y = self.y + dy
        wysokosc_bloku = len(self.linie) * (self.wysokosc_tekstu + self.odstep)
        y_start = y
        y_end = y + wysokosc_bloku + self.offset_y

        #Nawias
        # Nawias z lewej (z haczykami)
        canvas.create_line(x + self.offset_x, y_start, x, y_start, width=2, fill="blue", tags=tag)
        canvas.create_line(x, y_start, x, y_end - self.odstep, width=2, fill="blue", tags=tag)
        canvas.create_line(x, y_end - self.odstep, x + self.offset_x, y_end - self.odstep, width=2, fill="blue",
                           tags=tag)

        # Linie tekstu
        for idx, linia in enumerate(self.linie):
            yy = y + idx * (self.wysokosc_tekstu + self.odstep)
            canvas.create_text(x + self.offset_x + 5, yy, text=linia, anchor="nw", font=self.czcionka, tags=tag)
