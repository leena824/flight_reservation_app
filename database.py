import sqlite3
def connect():
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            flight_number TEXT NOT NULL,
            departure TEXT NOT NULL,
            destination TEXT NOT NULL,
            date TEXT NOT NULL,
            seat_number TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
def insert(name, flight_number, departure, destination, date, seat_number):
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, flight_number, departure, destination, date, seat_number))
    conn.commit()
    conn.close()

def fetch():
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservations")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update(res_id, name, flight_number, departure, destination, date, seat_number):
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE reservations
        SET name=?, flight_number=?, departure=?, destination=?, date=?, seat_number=?
        WHERE id=?
    """, (name, flight_number, departure, destination, date, seat_number, res_id))
    conn.commit()
    conn.close()

def delete(res_id):
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM reservations WHERE id=?", (res_id,))
    conn.commit()
    conn.close()

