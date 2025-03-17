# Personal Task Manager API and Web Application

## Overview

This project is a Personal Task Manager, built using Flask and Flask-RESTful, designed to demonstrate the development and integration of a RESTful API with a user-friendly web interface. It showcases the ability to create, retrieve, update, and delete tasks, with a focus on API design and functionality.

The application allows users to:

* Add tasks with titles, descriptions, deadlines, and assignment types.
* View a list of all tasks.
* Delete selected tasks.

This project highlights skills in API development, web application creation, and simple user interface design

## Features

* **RESTful API:** Implements a RESTful API using Flask-RESTful to manage tasks.
* **Web Interface:** Provides a simple web interface for users to interact with the task manager.
* **Task Management:** Allows users to add, view, and delete tasks.
* **Detailed Task Information:** Supports task titles, descriptions, deadlines (date and time), and assignment types.
* **User-Friendly Interface:** Uses HTML and CSS to create an intuitive user experience.
* **Delete Multiple Tasks:** Allows the user to select and delete multiple tasks at once.

## Technologies Used

* **Python:** Programming language.
* **Flask:** Web framework.
* **Flask-RESTful:** Library for building RESTful APIs.
* **requests:** Library for making HTTP requests.
* **HTML/CSS:** For the web interface.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone [repository URL]
    cd TaskManager
    ```
2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install Flask Flask-RESTful requests
    ```
4.  **Run the application:**
    ```bash
    python main.py
    ```
5.  **Open your browser:**
    * Navigate to `http://127.0.0.1:5000/`.

## API Endpoints

* **`GET /api/task`**: Retrieves all tasks.
* **`GET /api/task/<task_id>`**: Retrieves a specific task by ID.
* **`POST /api/task`**: Creates a new task.
* **`DELETE /api/task/<task_id>`**: Deletes a task by ID.

## Web Pages

* **Home Page (`/`)**: Displays "Add Task" and "Show Task List" buttons.
* **Add Task Page (`/add_task`)**: Allows users to add new tasks.
* **Show Task List Page (`/show_tasks`)**: Displays a list of tasks with checkboxes for deletion.
* **Delete Tasks (`/delete_tasks`)**: handles the deletion of tasks.


## Future Enhancements

* **Database Integration:** Use a database to persist tasks.
* **User Authentication:** Add user authentication for secure task management.
* **Improved UI/UX:** Enhance the user interface with more advanced styling and features.
* **API Documentation:** Add API documentation using Swagger or OpenAPI.
