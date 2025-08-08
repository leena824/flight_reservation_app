import tkinter as tk
from tkinter import messagebox
import database

def load_edit_reservation(root, back_to_home, reservation_data):
    for widget in root.winfo_children():
        widget.destroy()

   
    res_id, name_val, flight_val, dep_val, dest_val, date_val, seat_val = reservation_data

    
    title = tk.Label(root, text="Edit Reservation", font=("Helvetica", 18))
    title.pack(pady=10)

    
    form_frame = tk.Frame(root)
    form_frame.pack(pady=20)


    labels = ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"]
    values = [name_val, flight_val, dep_val, dest_val, date_val, seat_val]
    entries = []

    for i, (label_text, default_val) in enumerate(zip(labels, values)):
        label = tk.Label(form_frame, text=label_text)
        label.grid(row=i, column=0, padx=10, pady=5, sticky="e")

        entry = tk.Entry(form_frame)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entry.insert(0, default_val)
        entries.append(entry)

    
    def save_changes():
        new_values = [e.get() for e in entries]

        if any(not val.strip() for val in new_values):
            messagebox.showwarning("Input Error", "Please fill in all fields.")
            return

        database.update(res_id, *new_values)
        messagebox.showinfo("Success", "Reservation updated successfully.")
        back_to_home()

    
    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=10)

    save_btn = tk.Button(btn_frame, text="Save Changes", command=save_changes)
    save_btn.grid(row=0, column=0, padx=10)

    cancel_btn = tk.Button(btn_frame, text="Cancel", command=back_to_home)
    cancel_btn.grid(row=0, column=1, padx=10)
