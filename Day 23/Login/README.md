# Flask Login

This is a simple Flask web application that includes a basic login system, a homepage, and a user dashboard. It demonstrates how to set up user authentication with Flask, handle sessions, and use Flask-WTF for form handling.

## Prerequisites

- Python 3.x
- Flask
- Flask-WTF
- Werkzeug

## Application Structure

- `app.py`: The main Flask application file.
- `templates/`:
  - `index.html`: Homepage template.
  - `login.html`: Login page template.
  - `dashboard.html`: Dashboard page template.

## Running the Application

To start the Flask development server, run:

```bash
python app.py
```

Open a web browser and navigate to `http://127.0.0.1:5000/` to access the application.

## Features

1. **Homepage** (`/`):
   - Displays a welcome message and a button to navigate to the login page.

2. **Login Page** (`/login`):
   - Users can enter their username and password to log in.
   - Displays an error message if login credentials are invalid.

3. **Dashboard** (`/dashboard`):
   - Accessible only to logged-in users.
   - Displays a personalized message and a logout button.

4. **Logout** (`/logout`):
   - Logs the user out and redirects to the homepage.

## Security

- Passwords are hashed using Werkzeug's `generate_password_hash` and checked with `check_password_hash`.
- A secure random secret key is used for session management.

## Forms

- **LoginForm**:
  - `username`: A required field for the username.
  - `password`: A required field for the password.

## Customization

- **Adding Users**:
  Modify the `users` dictionary in `app.py` to add more users or change existing passwords.

- **Styling**:
  The application uses Bootstrap 5 for basic styling. You can customize the appearance by modifying the Bootstrap classes or adding custom CSS.
