"""
edit_reservation.py
-------------------
Defines the EditReservationPage class for updating reservation details.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import database

class EditReservationPage(ttk.Frame):
    """
    Page for editing an existing reservation.
    Pre-fills form with selected reservation data.
    """

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.res_id = None  # Reservation ID being edited

        ttk.Label(self, text="Edit Reservation", font=("Arial", 18, "bold")).pack(pady=15)

        form = ttk.Frame(self, padding=20)
        form.pack(pady=10, fill="x", expand=True)

        labels = ["Name", "Flight Number", "Departure", "Destination", "Date (YYYY-MM-DD)", "Seat Number"]
        self.entries = {}

        # Create entry fields
        for i, lab in enumerate(labels):
            ttk.Label(form, text=lab).grid(row=i, column=0, sticky="e", padx=10, pady=8)
            ent = ttk.Entry(form, width=35)
            ent.grid(row=i, column=1, sticky="w", padx=10, pady=8)
            self.entries[lab] = ent

        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=20)

        update_btn = ttk.Button(btn_frame, text="Update", command=self.update_reservation)
        back_btn = ttk.Button(btn_frame, text="Back", command=lambda: controller.show_frame("ReservationsPage"))
        update_btn.grid(row=0, column=0, padx=15, ipadx=10, ipady=5)
        back_btn.grid(row=0, column=1, padx=15, ipadx=10, ipady=5)

    def refresh(self, reservation=None, **kwargs):
        """Load reservation details into form for editing."""
        if reservation:
            self.res_id = reservation[0]
            fields = ["Name", "Flight Number", "Departure", "Destination", "Date (YYYY-MM-DD)", "Seat Number"]
            for i, f in enumerate(fields):
                self.entries[f].delete(0, "end")
                self.entries[f].insert(0, reservation[i+1])

    def update_reservation(self):
        """Save updated reservation back to database."""
        vals = [self.entries[l].get().strip() for l in self.entries]
        if not all(vals):
            messagebox.showerror("Error", "All fields are required")
            return
        name, flight_number, departure, destination, date, seat_number = vals
        database.update_reservation(self.res_id, name, flight_number, departure, destination, date, seat_number)
        messagebox.showinfo("Success", "Reservation updated")
        self.controller.show_frame("ReservationsPage")
