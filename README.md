# Bangazon Orientation API

An open API for Bangazon, a fictitious company of Nashville Software School, built with the Django REST framework. The initial version is for internal consumption only, and will not require permissions to access, or manipulate, any resources. 

### This API will expose these resources:
1. Customer
    - First Name
    - Last Name
    - Date Created
1. Order
    - Payment Type
    - Order Date
    - Customer ID
1. Product
    - Price
    - Title
    - Description
    - Product Type ID
    - Customer ID
1. Department
    - Budget
    - Name
1. Computer
    - Title
    - Purchase Date
    - Decommission Date
1. Training Program
    - Name
    - Start Date
    - End Date
    - Max Enrollment
1. Product Type
    - Label
1. Payment Type
    - Account Number
    - Account Label
    - Account Type
    - Customer ID
1. Employee
    - First Name
    - Last Name
    - Is Supervisor(True/False)
    - Department ID


## Requirements/Dependencies
### Install Python Python
[Python 3.6.0](https://wiki.python.org/moin/BeginnersGuide/Download) (click for instructions for installing)

### Install Django and Django REST framework
```
pip install django
pip install djangorestframework
```

## Setup Project
1. Clone the repository
    ```
    git clone https://github.com/solanum-tuberosums/bangazonOrientationAPI.git
    ```
1. Set up Data Base
    ```
    cd bangazon
    python manage.py makemigrations
    python manage.py migrate
    python manage.py loaddata customerdata.json
    python manage.py loaddata employeedata.json
    python manage.py runserver
    ```
1. View in your borwser by going to [localhost:8000](http://localhost:8000/)

