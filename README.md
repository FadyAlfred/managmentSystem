# Management System

### Installation:
##### System Dependencies:

1. Install git:  
`sudo apt-get install -y git`
2. Clone or download this repo.
3. Install pip and vitualenv:  
`sudo apt-get install -y virtualenv`  
`sudo apt-get install -y python3-pip`
4. Create a virtual environment:  
`virtualenv -p python3 ~/.virtualenvs/managementEnv`
5. Activate the virtual environment:  
`source ~/.virtualenvs/managementEnv/bin/activate`
6. Install requirements in the virtualenv:  
`pip3 install -r requirements.txt`

##### Relational database dependencies (PostgreSQL):
1. Install components for Ubuntu:  
`sudo apt-get update`  
`sudo apt-get install python-dev libpq-dev postgresql postgresql-contrib`
2. Switch to **postgres** (PostgreSQL administrative user):  
`sudo su postgres`
3. Log into a Postgres session:  
`psql`
4. Create database with name **blockwork**:
`CREATE DATABASE blockwork;`
5. Create a database user which we will use to connect to the database:  
`CREATE USER blockwork_user WITH PASSWORD 'blockwork_pass';`
6. Modify a few of the connection parameters for the user we just created:  
`ALTER ROLE blockwork_user SET client_encoding TO 'utf8';`      
`ALTER ROLE blockwork_user SET default_transaction_isolation TO 'read committed';`      
`ALTER ROLE blockwork_user SET timezone TO 'UTC';`      
`ALTER USER blockwork_user CREATEDB;`
7. Give our database user access rights to the database we created:  
`GRANT ALL PRIVILEGES ON DATABASE blobwork TO blobwork_user;`
8. Exit the SQL prompt and the postgres user's shell session:  
`\q` then `exit`
9. Activate the virtual environment:  
`source ~/.virtualenvs/managementEnv/bin/activate`
10. Make Django database migrations:
`python manage.py makemigrations`  
then: `python manage.py migrate`

##### Use admin interface:
1. Create an admin user:  
`python manage.py createsuperuser`
2. Run the project locally:  
`python manage.py runserver`
3. Navigate to: `http://localhost:8000/admin/`

### API Endpoints
##### Product
Method: `GET`       
Endpoint: `/product/`   
Description: `List all products from the database`

Method: `POST`      
Endpoint: `/product/`       
Payload:
`{
    "title": "product name",
    "product_code": "product code",
    "price": product price,
    "quantity": product quantity,
    "categories": [
        1,2
        ]
}`      
Description: `Create new product in the database`

Method: `GET`       
Endpoint: `/product/<product ID>/`      
Description: `Get product in detail from the database`

Method: `PUT`       
Endpoint: `/product/<product ID>/`      
Payload:
`{
    "title": "new product name",
    "product_code": "new product code",
    "price": new product price,
    "quantity": new product quantity,
    "categories": [
        1,2,3,4
        ]
}`      
Description: `Update existing product in the database`

Method: `DELETE`        
Endpoint: `/product/<product ID>/`      
Description: `Delete product from the database`

##### Category
Method: `GET`       
Endpoint: `/category/`      
Description: `List all categories from the database`

Method: `POST`      
Endpoint: `/category/`      
Payload:
`{
    "name": "category name",
    "parent": 1 or can be null
}`      
Description: `Create new category in the database`

Method: `GET`       
Endpoint: `/category/<category ID>/`        
Description: `Get category in detail from the database`

Method: `PUT`       
Endpoint: `/category/<category ID>/`        
Payload:
`{
    "name": "new category name",
    "parent": new parent ID or can be null
}`      
Description: `Update existing category in the database`

Method: `DELETE`        
Endpoint: `/category/<category ID>/`        
Description: `Delete category from the database`

Method: `GET`       
Endpoint: `/category/<category ID>/children/`       
Description: `Get specific category children from the database`
