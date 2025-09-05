Task Manager - Backend 

This is the backend API for the Task Manager app, built with Django and Django REST Framework.

#Setup Instructions

# 1. Clone the repository
git clone https://github.com/your_username/task-manager-backend.git
cd task-manager-backend/backend

# 2. Create and activate virtual environment
python -m venv .venv
# On Windows:
.venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Start the server
python manage.py runserver

Backend will run at:  
http://127.0.0.1:8000

# API Endpoints

Method | Endpoint          | Description                  

GET    | /tasks/           | List all tasks               
POST   | /tasks/           | Create a new task            
PATCH  | /tasks/{id}/      | Update a task (toggle, edit) 
DELETE | /tasks/{id}/      | Delete a task                


# Notes
- Database: SQLite (default, inside `/backend/db.sqlite3`)
- CORS is configured for frontend running on `http://localhost:5173`
