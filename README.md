🎟️ Lottery Management System – Python Tkinter

This project is a Lottery Management System built using Python and Tkinter, designed for managing a home loan lottery process.

The application allows administrators to:

Manage participants

Manage loans with defined periods and amounts

Run a fair and fully random lottery

Display ordered results showing which participant receives the loan each month

The project is implemented using a three-layer architecture and includes a database for data persistence.

⭐ Features
👥 Participant Management

Add new participants

💰 Loan Management

Register loans with:

Start date and end date

Loan amount

Edit and delete loans

Full CRUD operations

🎲 Lottery System

Select a specific loan

Run a fully random lottery

Automatically order participants from first to last

Display monthly loan assignment, for example:

Month 1 → Ahmad

Month 2 → Sara

Month 3 → Reza

ℹ️ About Section

Information about the application and its purpose

🧱 Architecture

The project follows a three-layer architecture:

Presentation Layer (GUI) – Tkinter

Business Logic Layer

Data Access Layer (Database)

This structure improves code organization, maintainability, and scalability.

🛠 Technologies Used

Python 3

Tkinter (GUI)

SQLite (Database)

Random module

▶ How It Works

Participants are registered and managed in the system.

Loans are created with defined time periods and amounts.

A loan is selected for the lottery.

The system randomly orders participants.

Each participant is assigned a loan month based on the lottery result.

Results are displayed in an ordered list from first to last.

🚀 How to Run
python main.py

✔ Real-world project for loan and lottery management
✔ Can be extended with user authentication and reporting features
