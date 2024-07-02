# SEA Technical Challenge - Backend
Welcome to the repository. This project is a task for the COMPFEST SEA Academy. 

## Highlights
- Hosted the database on supabase
- All endpoints are prefixed with "api/v1/"

## Getting Started
Before running you'd need to add a .env file in root of the project. The content is as follows :
```
DATABASE_PASSWORD = KktW8z0eoCSUXxFR
```  

For the first time, simply do the steps below to install the required dependencies :
```bash
python -m venv env
pip install -r requirements.txt

# If you're on macOS or linux
source env/bin/activate 

# If you're on windows
env\Scripts\activate
```
After that you'd only need to run 
```bash
python manage.py runserver
```
