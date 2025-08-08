import tkinter as tk
from home import load_home
import database

def main():
    root = tk.Tk()
    root.title("Flight Reservation App")
    root.geometry("600x400")

    def switch_to_home():
        load_home(root, switch_to_booking, switch_to_reservations)

    def switch_to_booking():
        from booking import load_booking
        load_booking(root, switch_to_home)

    def switch_to_reservations():
        from reservations import load_reservations
        load_reservations(root, switch_to_home)

    database.connect()
    switch_to_home()

    root.mainloop()

if __name__ == "__main__":
    main()

import database
database.connect()

