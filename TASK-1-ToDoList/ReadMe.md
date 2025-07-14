# Task 1 - To-Do List Application (Tkinter GUI)

This project is a secure, user-based To-Do List application developed using Python and Tkinter as part of the CodSoft Internship (July 2025 Batch).

It supports individual user accounts with login and registration, password hashing using bcrypt, and persistent task storage using JSON files.

## Features

- User Registration with auto-generated User ID
- Secure login with hashed passwords
- Add, view, update, and delete tasks
- Store tasks with status (e.g., "Incomplete", "Done", etc.)
- Data persistence using `listusers.json`
- Clean and simple GUI using Tkinter

## How to Run

1. Make sure you have Python installed (version 3.x)

##Technologies Used

Python
Tkinter (for GUI)
bcrypt (for password security)
JSON (for saving user accounts and tasks)

##Notes
Passwords must be 8+ characters with at least one special character.
Make sure to remember your User ID after registration. It's required for login.
Each user's tasks are saved and reloaded automatically.

##Example
Register → Name: Arjun, Password: pass@1234
App gives you: User ID: 107
On next run, you can login using ID 107 and your password
