Django Car Dealership Management System

A web-based car dealership management system built with Python and Django. The application is designed to help dealerships manage vehicle inventory, customers, and sales through a centralized dashboard.

Features

- Vehicle Management: Add, view, update and manage vehicle inventory.
- Customer Management: Register and manage customer information.
- Sales Management: Record sales and manage sales information and statuses.
- Dashboard: View dealership information from a centralized dashboard.
- Authentication: User registration and login functionality.
- Vehicle Images: Support for vehicle image uploads.
- CRUD Operations: Create, read, update and delete records.

Technologies Used

- Python
- Django
- HTML5
- CSS3
- JavaScript
- SQLite

Project Structure

DealshipDjango/
│
├── cars/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
│
├── dealership/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── .gitignore
└── README.md

Installation and Setup

1. Clone the repository

git clone https://github.com/Karabo04/django-car-dealership.git

2. Navigate into the project

cd django-car-dealership

3. Create a virtual environment

python -m venv env

Activate it on Linux:

source env/bin/activate

4. Install dependencies

pip install Django python-dotenv

Install any additional dependencies required by the project.

5. Configure environment variables

Create a ".env" file in the project root and add your own Django secret key:

django_secret_key=your-own-secret-key

Important: Never upload your ".env" file or expose your secret key publicly.

6. Apply database migrations

python manage.py migrate

7. Create an administrator account

python manage.py createsuperuser

8. Start the development server

python manage.py runserver

Open your browser and visit:

http://127.0.0.1:8000/

Purpose

This project was developed to demonstrate practical skills in Django web development, database management, application architecture, authentication, form handling and CRUD operations.

Author

Karabo Nqambi

GitHub: "@karabo04" (https://github.com/Karabo04)