# Flask Routing | Flask Dynamic Content Project

## Overview

This project demonstrates a Flask web application with dynamic content loading using JavaScript. The application features multiple routes and allows for seamless navigation between different pages without reloading the entire page.

## Project Structure

The project consists of the following files:

- `app.py`: Main Flask application file.
- `demo.py`: A separate Flask app for demonstration purposes.
- `templates/index.html`: The HTML template that includes JavaScript for dynamic content loading.

## File Descriptions

### `app.py`

This is the main Flask application file. It defines several routes that return either HTML or JSON responses based on the type of request:

- `/`: Returns the home page or JSON content for AJAX requests.
- `/about`: Returns the about page or JSON content for AJAX requests.
- `/contact`: Returns the contact page or JSON content for AJAX requests.
- `/user/<username>`: Returns a user profile page with a dynamic username or JSON content for AJAX requests.
- `/portfolio`, `/portfolio/about`, `/portfolio/education`, `/portfolio/personal`, `/portfolio/skills`, `/portfolio/achievements`: Various portfolio-related pages with JSON content for AJAX requests.

### `demo.py`

A separate, simpler Flask application for demonstration purposes. It includes basic routes for testing:

- `/`: Returns a welcome message.
- `/about`: Returns an about page message.

### `templates/index.html`

The HTML template used by the `app.py` application. It includes:

- JavaScript to handle dynamic content loading using the Fetch API.
- Buttons for navigating to different routes and updating the page content without reloading.
- A content area where dynamic content is displayed based on the route.

## How to Run the Project

1. **Install Flask**: Make sure you have Flask installed. You can install it using pip:

    ```bash
    pip install Flask
    ```

2. **Run the Main Application**: Start the Flask application by running `app.py`:

    ```bash
    python app.py
    ```

    Open your browser and go to `http://localhost:5000` to see the main application.

3. **Run the Demo Application**: For demonstration purposes, you can also run `demo.py`:

    ```bash
    python demo.py
    ```

    Open your browser and go to `http://localhost:5000` to see the demo application.

## Usage

- Use the buttons on the home page to navigate to different sections. The content area will update dynamically without a full page reload.
- Use the browser's back and forward buttons to navigate through the history of dynamically loaded content.
