# Library Management System

A Django-based Library Management System that allows administrators to manage books and students to view them.

## Features

- Admin Authentication (Signup/Login)
- Book Management (CRUD operations)
- Student View for books
- MySQL Database Integration
- Responsive UI using Bootstrap 5

## Setup Instructions

1. Create and activate virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create MySQL Database:
```sql
CREATE DATABASE library_db;
```

4. Configure environment variables:
Create a `.env` file in the root directory with:
```
DEBUG=True
SECRET_KEY=your-secret-key
DB_NAME=library_db
DB_USER=your-mysql-username
DB_PASSWORD=your-mysql-password
DB_HOST=localhost
DB_PORT=3306
```

5. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

8. Access the application:
- Admin interface: http://127.0.0.1:8000/admin/
- Main application: http://127.0.0.1:8000/

## Project Structure

```
library/
├── library/          # Main project directory
├── books/           # Books app
├── accounts/        # User authentication app
├── templates/       # HTML templates
├── static/         # Static files (CSS, JS, images)
└── manage.py       # Django management script
``` 