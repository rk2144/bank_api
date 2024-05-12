
Django Bank Details API
This Django project provides an API for managing bank details including banks, branches, and accounts.

Features
API Endpoints: CRUD operations for banks, branches, and accounts.
Browsable API: Easily interact with the API through Django Rest Framework's browsable interface.
Clean Code: Follows best practices for Django development.
Test Coverage: Includes comprehensive test cases for views and API endpoints.
Deployment: Instructions for deploying the project to Heroku.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your_username/django-bank-details-api.git
Install dependencies:

bash
Copy code
cd django-bank-details-api
pip install -r requirements.txt
Run migrations:

bash
Copy code
python manage.py migrate
Start the development server:

bash
Copy code
python manage.py runserver
Access the API at http://127.0.0.1:8000/api/.

Testing
Run the test suite:

bash
Copy code
python manage.py test bank_details
Deployment
This project can be deployed to Heroku:

Create a new Heroku app:

bash
Copy code
heroku create your-app-name
Deploy the code to Heroku:

bash
Copy code
git push heroku main
Run migrations on Heroku:

bash
Copy code
heroku run python manage.py migrate
Open your app:

bash
Copy code
heroku open
