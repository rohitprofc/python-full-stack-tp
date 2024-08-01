# Django Notes Application

A simple notes application built with Django. This project allows users to create, view, edit, and delete notes. It uses Bootstrap for responsive design and includes functionality for displaying notes in a list group.

## Features

- Create, view, edit, and delete notes
- Display notes in a responsive Bootstrap grid
- Use of Bootstrap modals for confirmation dialogs
- Localized time display

## Prerequisites

- Python 3.12 or later
- Django 5.x
- Bootstrap 5.x

## Setup and Installation

1. **Clone the Repository**

   Clone the repository to your local machine:

   ```bash
   https://github.com/rohitprofc/python-full-stack-tp.git
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd python-full-stack-tp
   ```

3. **Create and Activate a Virtual Environment**

   Create a virtual environment:

   ```bash
   virtualenv venv
   ```

   Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**

   Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

5. **Naviagte to Django Project**

   ```bash
   cd Day\ 26/ myproject
   ```

6. **Apply Migrations**

   Run the Django migrations to set up the database:

   ```bash
   python manage.py migrate
   ```

7. **Run the Development Server**

   Start the Django development server:

   ```bash
   python manage.py runserver
   ```

   The application will be available at `http://127.0.0.1:8000/`.

## Usage

- **Access the Notes List:** Navigate to `http://127.0.0.1:8000/` to view the list of notes.
- **Create a New Note:** Click on the "Create New Note" button to add a new note.
- **View Details:** Click on a note title to view its details.
- **Edit a Note:** On the note detail page, click the "Edit" button to modify the note.
- **Delete a Note:** Use the delete button on the note detail page to remove the note, which will trigger a confirmation modal.
