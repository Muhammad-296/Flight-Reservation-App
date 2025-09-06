"""
home.py
-------
Defines the HomePage class, the main menu of the application.
"""

import tkinter as tk
from tkinter import ttk

class HomePage(ttk.Frame):
    """
    The home page provides navigation options to:
    - Book a new flight
    - View all reservations
    """

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Title
        ttk.Label(
            self, text="Flight Reservation System", font=("Arial", 20, "bold")
        ).pack(pady=40)

        # Navigation buttons
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=20)

        book_btn = ttk.Button(btn_frame, text="Book Flight", command=lambda: controller.show_frame("BookingPage"))
        view_btn = ttk.Button(btn_frame, text="View Reservations", command=lambda: controller.show_frame("ReservationsPage"))

        book_btn.grid(row=0, column=0, padx=20, ipadx=15, ipady=8)
        view_btn.grid(row=0, column=1, padx=20, ipadx=15, ipady=8)
