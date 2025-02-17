# Event Planner

A web-based Event Planner app that allows users to browse, comment, share, buy tickets, and post events. Users can save their favorite events and, in the future, filter them by categories.

## Features

### Not Logged-in Users:
- Browse through events
- Comment on events
- Share events with friends
- Buy tickets for events

### Logged-in Users:
- Browse, comment, and buy tickets
- Post and share your own events
- Save your favorite events for easy access

## Table of Contents
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Setting Up with venv (Virtual Environment)](#2-setting-up-with-venv-virtual-environment)
  - [3. Setting Up with Docker (Optional)](#3-setting-up-with-docker-optional)
  - [4. Acquiring and Adding Secrets](#4-acquiring-and-adding-secrets)
  - [5. Run the Application](#5-run-the-application)
  - [6. Static and Media Files](#6-static-and-media-files)
  - [7. Testing](#7-testing)
  - [8. Troubleshooting](#8-troubleshooting)
- [Contribution](#contribution)
- [License](#license)

## Requirements

- Python 3.8+
- Docker 
- Docker Compose 

## Setup Instructions

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
gh repo clone siboniseni/event_planner
cd /event_planner
```

### 2. Setting Up with venv (Virtual Environment)

#### Create a Virtual Environment

Create a virtual environment in the project directory:

```bash
python -m venv venv
```

#### Activate the Virtual Environment

For **Windows**:

```bash
venv\Scripts\activate
```

For **macOS/Linux**:

```bash
source venv/bin/activate
```

#### Install Dependencies

Once the virtual environment is activated, install the necessary dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Setting Up with Docker (Optional)

#### Build the Docker Image

Build the Docker image. Ensure you have Docker installed.

```bash
docker build -t event_planner .
```

#### Run the Docker Container

Run the container:

```bash
docker run -d -p 8000:8000 event_planner
```

### 4. Acquiring and Adding Secrets

**Important:** Do not commit secrets such as passwords or API tokens to public repositories. You can add these secrets by creating a `.env` file in the root directory of your project. The `.env` file should include sensitive values like the Django `SECRET_KEY`, API tokens, etc.

Make sure to add `.env` to your `.gitignore` file to avoid accidentally committing sensitive information.

### 5. Run the Application

#### Applying Migrations

Before running the server, apply the database migrations:

```bash
python manage.py migrate
```

#### Running the Development Server

To start the Django development server:

```bash
python manage.py runserver
```

Visit the application at `http://127.0.0.1:8000/` to view and manage events.

### 6. Static and Media Files

#### Static Files

For production, collect static files using the following command:

```bash
python manage.py collectstatic
```

This will gather all static files into a single location (`STATIC_ROOT`).

#### Media Files

Make sure to configure the `MEDIA_URL` and `MEDIA_ROOT` for handling user-uploaded media files. For local development, the media files will be stored in the `media` directory.

### 7. Testing

To run the tests for the application, use the following command:

```bash
python manage.py test
```

### 8. Troubleshooting

- **Docker Errors:** Ensure Docker is running on your machine and the ports are not already in use.
- **Virtual Environment Issues:** Make sure the correct Python version is installed and the virtual environment is activated before running commands.

## Contribution

Feel free to fork the repository and submit pull requests. Please ensure that you write tests for new features or bug fixes.

## License

This project is licensed under the MIT License.



**Live Demo:**
   ```bash
   https://event-planner-2025-7b214c2805eb.herokuapp.com/
   ```

