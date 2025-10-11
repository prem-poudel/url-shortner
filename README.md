# URL Shortener

A simple Django-based URL shortener application.

## Demo Link
[Live Demo](https://short-link.prempoudel.com.np/)

## Features

- **Shorten long URLs:** Instantly generate short links for any long URL.
- **Redirection:** Automatically redirect users from short links to the original URLs. 
- **QR Code Generation:** Create QR codes for each short URL.
- **User Authentication:** Register and log in to manage your own links.
- **User-friendly Web Interface:** Clean and intuitive UI for easy navigation.
- **Docker Support:** Easily deploy the application using Docker.


## Setup

### Environment Setup

1. Copy the example environment file:
    - On **Linux/macOS**:
      ```bash
      cp .env.example .env
      ```
    - On **Windows** (Command Prompt):
      ```cmd
      copy .env.example .env
      ```
2. Update the `.env` file with your configuration (e.g., secret keys, database settings).


### Using Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Using Docker

```bash
docker compose up --build -d
```

## Usage

- If running with a virtual environment, visit `http://localhost:8000` in your browser.
- If running with Docker, visit `http://localhost:8020`.
- Use the web interface or API to shorten URLs.
