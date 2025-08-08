import tkinter as tk
from tkinter import ttk 

def load_home(root ,switch_to_booking , switch_to_reservations):
   for widget in root.winfo.children():
      widget.destroy()

   title = tk.Label(root, text="Flight Reservation System", font=("Helvetica", 20))
   title.pack(pady=20)
   
   book_btn = ttk.Button(root, text="Book Flight", command=switch_to_booking)
   book_btn.pack(pady=10)

   view_btn = ttk.Button(root, text="View Reservations", command=switch_to_reservations)
   view_btn.pack(pady=10)
   
   
   

