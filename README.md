# Shopzee - Grocery Store Application
CRUD Application built as a part of the course - Modern Application Development: 2

Web-Framework: Flask
Front End: VueJS and VueBootstrap
Back End: SQLite

# Accessing the Application
## Setting up Back End
### Step 1
Navigate to `backend` folder
Install all dependencies by performing 
```pip install -r requirements.txt```

### Step 2
Initiate Redis Server using the command 
```sudo service redis-server start```

### Step 3
Run celery beat and celery worker using the command 
```celery -A app:celery_app beat -l info```
```celery -A app:celery_app worker -l info```

### Step 4
Run the `app.py`

## Setting up the Front End
### Step 1
Navigate to `frontend` folder
Install all dependencies by performing 
```npm install```

### Step 2
Initiate VueJS server and run frontend using the command 
```npm run serve```

### Step 3
Click on the link given to access the application.
