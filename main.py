"""
main.py
-------
Entry point for the flight reservation system.
Sets up the Tkinter window, styles, and page navigation.
"""

import tkinter as tk
from tkinter import ttk
import database
from home import HomePage
from booking import BookingPage
from reservations import ReservationsPage
from edit_reservation import EditReservationPage

class App(tk.Tk):
    """
    Main application class.
    Handles navigation between pages.
    """

    def __init__(self):
        super().__init__()
        self.title("Flight Reservation System")
        self.geometry("850x600")
        self.resizable(False, False)

        # Global style configuration
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("TButton", font=("Arial", 11), padding=6)
        style.configure("TLabel", font=("Arial", 11))
        style.configure("Treeview.Heading", font=("Arial", 11, "bold"))

        # Container for all pages
        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)

        # Dictionary to hold all frames (pages)
        self.frames = {}
        for F in (HomePage, BookingPage, ReservationsPage, EditReservationPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the home page first
        self.show_frame("HomePage")

    def show_frame(self, page_name, **kwargs):
        """Raise the requested frame to the front and refresh if applicable."""
        frame = self.frames[page_name]
        frame.tkraise()
        if hasattr(frame, "refresh"):
            frame.refresh(**kwargs)

if __name__ == "__main__":
    # Initialize database and run the app
    database.init_db()
    app = App()
    app.mainloop()
