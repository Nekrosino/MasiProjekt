import sqlite3

# Połącz się z bazą (jeśli plik bazy nie istnieje, zostanie utworzony)
conn = sqlite3.connect('moja_baza.db')

# Utwórz kursor do wykonywania zapytań
cursor = conn.cursor()

# Utwórz tabelę
cursor.execute('''
CREATE TABLE IF NOT EXISTS uzytkownicy (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    imie TEXT,
    wiek INTEGER
)
''')

# Zatwierdź zmiany
conn.commit()

# Zamknij połączenie
conn.close()
