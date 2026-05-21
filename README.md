#  Website Monitor

##  Description
A Django-based web application that automatically monitors websites for changes. Users can register, add websites, and check for content changes with one click.

##  Features
-  User registration and authentication
-  Add websites to monitor
-  Check websites for changes
-  View change count for each website
-  Delete websites from monitoring list
-  User data isolation (each user sees only their own websites)
-  CSRF protection and password hashing

##  Technologies Used
| Technology | Purpose |
|------------|---------|
| Python 3.14 | Backend programming |
| Django 6.0 | Web framework |
| SQLite | Database |
| Requests | HTTP requests for web scraping |
| BeautifulSoup | HTML parsing |
| HTML/CSS | Frontend interface |

##  Project Structure
my_project/
├── manage.py
├── my_project/
│ ├── settings.py
│ └── urls.py
└── monitor/
├── models.py # Database models
├── views.py # Business logic
├── urls.py # URL routing
├── admin.py # Admin panel registration
└── templates/
└── monitor/
├── home.html
├── register.html
├── login.html
└── dashboard.html

##  Installation

### Prerequisites
- Python 3.14 or higher

### Steps
```bash

# 1. Install dependencies
pip install -r requirements.txt

# 2. Run migrations
cd my_project
python manage.py makemigrations
python manage.py migrate

# 3. Run the application
python manage.py runserver
```

 How to Use

*Register - Create a new account

*Login - Enter your credentials

*Add Website - Enter name and URL (e.g., Google, https://google.com)

*Check - Click "Check" to see if the website changed

*Delete - Remove websites you no longer monitor

 by: Arsyk100
