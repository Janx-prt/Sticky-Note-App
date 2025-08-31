## Django Sticky Note Application

A simple sticky note web application built with **Django**. 
Users can create, edit, and delete sticky notes in an intuitive interface.  

---

## Features
- Add new sticky notes
- Edit existing notes
- Delete notes
- Responsive and user-friendly UI
- Persistent data storage via Django ORM

---

## Tech Stack
- **Backend**: Django 5.2.5
- **Database**: SQLite (default, configurable)
- **Frontend**: Django Templates (HTML, CSS)
- **Environment**: Developed in Visual Studio Code

---

## Project Structure
sticky_notes/
│
├── posts/ # Main app
│ ├── migrations/ # Database migrations
│ ├── templates/ # HTML templates
│ │ ├── base.html
│ │ └── posts/
│ │ ├── post_detail.html
│ │ ├── post_form.html
│ │ └── post_list.html
│ ├── static/ # Static files
│ │ ├── images/
│ │ └── styles.css
│ ├── views.py # Application logic
│ ├── models.py # Database models
│ ├── urls.py # App routes
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ └── tests.py
│
├── sticky_notes/ # Project settings
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ ├── asgi.py
│ └── init.py
│
├── manage.py
├── db.sqlite3
├── requirements.txt
└── README.md

---

## Installation & Setup

## Clone the repository
   bash
   git clone https://github.com/your-username/django-sticky-notes.git
   cd django-sticky-notes

---
## Set up Virtual Environment

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

---

## Install Dependancies 

pip install -r requirements.txt

---

## Run Migrations

python manage.py migrate

---

## Run Server 

python manage.py runserver
http://127.0.0.1:8000/

---

## Test ##

python manage.py test

---

## Creator

Janke Pretorius

