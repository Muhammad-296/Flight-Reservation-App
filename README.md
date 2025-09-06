# Flight Reservation App 

A simple desktop-based flight reservation system built with **Python**, **Tkinter**, and **SQLite**.  
This project demonstrates how to integrate a GUI with a relational database to perform **CRUD operations** (Create, Read, Update, Delete).

---

## 🎯 Project Objectives
- Provide a user-friendly interface for booking and managing flight reservations.
- Showcase CRUD operations using SQLite.
- Demonstrate multi-page navigation with Tkinter.
- Serve as a learning project for Python GUI + Database integration.

---

## ✈ Features
1. **Home Page**
   - Central navigation hub.
   - Buttons to book a new flight or view existing reservations.

2. **Flight Booking Page**
   - Input fields for:
     - Passenger Name  
     - Flight Number  
     - Departure  
     - Destination  
     - Date  
     - Seat Number  
   - Save button to insert the reservation into the database.

3. **Reservation List Page**
   - Displays all reservations in a table-like format.
   - Each record has options to **Edit** or **Delete**.

4. **Edit Reservation Page**
   - Pre-fills the selected reservation’s details.
   - Allows updating information and saving back to the database.

5. **Database**
   - Powered by SQLite (`flights.db`).
   - Automatically created on first run.
   - Table schema:
     ```sql
     CREATE TABLE reservations (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT NOT NULL,
         flight_number TEXT NOT NULL,
         departure TEXT NOT NULL,
         destination TEXT NOT NULL,
         date TEXT NOT NULL,
         seat_number TEXT NOT NULL
     );
     ```

---

## 🛠️ Technologies Used
- **Python 3.x**
- **Tkinter** (GUI library, built into Python)
- **SQLite** (lightweight relational database)
- **tkcalendar** (optional, for a date picker widget)

---
