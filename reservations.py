import tkinter as tk
from tkinter import ttk, messagebox
import database
from edit_reservation import load_edit_reservation

def load_reservations(root, back_to_home):
    for widget in root.winfo_children():
        widget.destroy()

    title = tk.Label(root, text="Reservations List", font=("Helvetica", 18))
    title.pack(pady=10)

    
    table_frame = tk.Frame(root)
    table_frame.pack(pady=10)

    
    columns = ("id", "name", "flight_number", "departure", "destination", "date", "seat_number")
    tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)

    for col in columns:
        tree.heading(col, text=col.replace("_", " ").title())
        tree.column(col, width=100)

    tree.pack(side="left")


    scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    
    def load_data():
        for row in tree.get_children():
            tree.delete(row)
        for row in database.fetch():
            tree.insert("", "end", values=row)

    load_data()

    
    def delete_selected():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a reservation to delete.")
            return

        item = tree.item(selected_item)
        res_id = item["values"][0]

        confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this reservation?")
        if confirm:
            database.delete(res_id)
            load_data()

    
    def edit_selected():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a reservation to edit.")
            return

        item = tree.item(selected_item)
        reservation_data = item["values"]
        load_edit_reservation(root, back_to_home, reservation_data)

    
    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=10)

    delete_btn = ttk.Button(btn_frame, text="Delete Selected", command=delete_selected)
    delete_btn.grid(row=0, column=0, padx=10)

    edit_btn = ttk.Button(btn_frame, text="Edit Selected", command=edit_selected)
    edit_btn.grid(row=0, column=1, padx=10)

    back_btn = ttk.Button(btn_frame, text="Back to Home", command=back_to_home)
    back_btn.grid(row=0, column=2, padx=10)
