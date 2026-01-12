# Django ToDo App ✅

A clean and user-based To-Do application built with **Django** and **Bootstrap**.

## 🚀 Features
- User Authentication (Signup / Login / Logout)
- Create tasks
- Edit task title
- Delete tasks (with confirmation)
- Mark task as Done / Undone
- Separate Pending & Completed sections
- Clear all completed tasks
- Responsive Bootstrap UI

## 🛠 Tech Stack
- Django
- SQLite (local)
- Bootstrap 5
- WhiteNoise (static files)
- Gunicorn (production server)

## 📸 Screenshots
_Add screenshots here_

## ⚙️ Setup (Local)
```bash
git clone <your-repo-link>
cd ToDo
python -m venv env

# Windows
env\Scripts\activate

# Mac/Linux
source env/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
