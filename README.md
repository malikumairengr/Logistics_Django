# Logistics Django App

This is a minimal logistics management application built with Django and Django REST Framework.

Quick start

1. Create a virtual environment and install requirements:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run migrations and start server:

```bash
python manage.py migrate
python manage.py runserver
```

API endpoints will be available under `/api/` (e.g. `/api/shipments/`).
