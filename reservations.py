"""
reservations.py
---------------
Defines the ReservationsPage class where all reservations are displayed in a table.
"""

import tkinter as tk
from tkinter import ttk
import database

class ReservationsPage(ttk.Frame):
    """
    Displays all reservations in a Treeview table.
    Allows editing or deleting of selected reservations.
    """

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Title
        ttk.Label(self, text="Reservations", font=("Arial", 18, "bold")).pack(pady=15)

        # Table setup
        cols = ("id", "name", "flight_number", "departure", "destination", "date", "seat_number")
        self.tree = ttk.Treeview(self, columns=cols, show="headings", height=12)

        # Configure column headings
        for col in cols:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, width=120, anchor="center")

        self.tree.pack(fill="both", expand=True, padx=20, pady=10)

        # Buttons below the table
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=15)

        edit_btn = ttk.Button(btn_frame, text="Edit", command=self.edit_selected)
        delete_btn = ttk.Button(btn_frame, text="Delete", command=self.delete_selected)
        back_btn = ttk.Button(btn_frame, text="Back", command=lambda: controller.show_frame("HomePage"))

        edit_btn.grid(row=0, column=0, padx=10, ipadx=8, ipady=5)
        delete_btn.grid(row=0, column=1, padx=10, ipadx=8, ipady=5)
        back_btn.grid(row=0, column=2, padx=10, ipadx=8, ipady=5)

    def refresh(self, **kwargs):
        """Refresh table with latest reservation data."""
        for row in self.tree.get_children():
            self.tree.delete(row)
        for res in database.get_reservations():
            self.tree.insert("", "end", values=res)

    def edit_selected(self):
        """Open the edit page for the selected reservation."""
        selected = self.tree.focus()
        if not selected:
            return
        values = self.tree.item(selected, "values")
        self.controller.show_frame("EditReservationPage", reservation=values)

    def delete_selected(self):
        """Delete the selected reservation from the database."""
        selected = self.tree.focus()
        if not selected:
            return
        res_id = self.tree.item(selected, "values")[0]
        database.delete_reservation(res_id)
        self.refresh()
