"""
booking.py
----------
Defines the BookingPage class where users can enter flight details and submit a reservation.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import database

class BookingPage(ttk.Frame):
    """
    Page for booking a flight.
    Contains input fields for passenger details and a submit button.
    """

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Page title
        ttk.Label(self, text="Book Flight", font=("Arial", 18, "bold")).pack(pady=15)

        # Input form frame
        form = ttk.Frame(self, padding=20)
        form.pack(pady=10, fill="x", expand=True)

        # Define input labels
        labels = ["Name", "Flight Number", "Departure", "Destination", "Date (YYYY-MM-DD)", "Seat Number"]
        self.entries = {}

        # Create input fields dynamically
        for i, lab in enumerate(labels):
            ttk.Label(form, text=lab).grid(row=i, column=0, sticky="e", padx=10, pady=8)
            ent = ttk.Entry(form, width=35)
            ent.grid(row=i, column=1, sticky="w", padx=10, pady=8)
            self.entries[lab] = ent

        # Action buttons
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=20)

        submit = ttk.Button(btn_frame, text="Submit", command=self.submit)
        back = ttk.Button(btn_frame, text="Back", command=lambda: controller.show_frame("HomePage"))
        submit.grid(row=0, column=0, padx=15, ipadx=10, ipady=5)
        back.grid(row=0, column=1, padx=15, ipadx=10, ipady=5)

    def submit(self):
        """Validate inputs and save a reservation to the database."""
        vals = [self.entries[l].get().strip() for l in self.entries]
        if not all(vals):
            messagebox.showerror("Error", "All fields are required")
            return
        name, flight_number, departure, destination, date, seat_number = vals
        database.add_reservation(name, flight_number, departure, destination, date, seat_number)
        messagebox.showinfo("Success", "Reservation added")

        # Clear fields
        for e in self.entries.values():
            e.delete(0, "end")

        # Redirect to reservations list
        self.controller.show_frame("ReservationsPage")

    def refresh(self, **kwargs):
        """Clear form when page is reopened."""
        for e in self.entries.values():
            e.delete(0, "end")
