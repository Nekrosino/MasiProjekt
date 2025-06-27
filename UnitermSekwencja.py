from Uniterm import Uniterm


class UnitermSekwencja(Uniterm):
    def __init__(self,x,y,czcionka,tekst,wysokosc_nawiasu):
        super().__init__(x,y,czcionka)
        self.tekst = tekst
        self.wysokosc_nawiasu = wysokosc_nawiasu
        self.szerokosc_tekstu = self.czcionka.measure(self.tekst)

    def draw(self,canvas, dx=0, dy=0, tag="Empty"):
            x = self.x +dx
            y = self.y + dy
            canvas.create_text(x, y, text=self.tekst, anchor="nw", font=self.czcionka, tags=tag)
            canvas.create_arc(x, y - self.wysokosc_nawiasu,
                              x + self.szerokosc_tekstu, y + 5,
                              start=0, extent=180, style='arc', width=2, outline="blue", tags=tag)
