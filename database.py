"""
database.py
------------
Handles SQLite database connection and CRUD operations for the flight reservation system.
"""

import sqlite3

def init_db():
    """Initialize the database and create the reservations table if it does not exist."""
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            flight_number TEXT NOT NULL,
            departure TEXT NOT NULL,
            destination TEXT NOT NULL,
            date TEXT NOT NULL,
            seat_number TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_reservation(name, flight_number, departure, destination, date, seat_number):
    """Insert a new reservation record into the database."""
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, flight_number, departure, destination, date, seat_number))
    conn.commit()
    conn.close()

def get_reservations():
    """Retrieve all reservations from the database."""
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservations")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_reservation(res_id, name, flight_number, departure, destination, date, seat_number):
    """Update an existing reservation by ID."""
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE reservations
        SET name=?, flight_number=?, departure=?, destination=?, date=?, seat_number=?
        WHERE id=?
    ''', (name, flight_number, departure, destination, date, seat_number, res_id))
    conn.commit()
    conn.close()

def delete_reservation(res_id):
    """Delete a reservation by ID."""
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM reservations WHERE id=?", (res_id,))
    conn.commit()
    conn.close()
