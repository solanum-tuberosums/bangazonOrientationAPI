# Bangazon Orientation API

An open API for Bangazon, a fictitious company of Nashville Software School, built with the Django REST framework. The initial version is for internal consumption only, and will not require permissions to access, or manipulate, any resources. 

### This API will expose these resources: 

Fields written in **bold** font are reserved for super users.

1. Customer
    - First Name
    - Last Name
    - **Date Created**
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
    - Serial Number
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
#### Install Python
[Python 3.6.0](https://wiki.python.org/moin/BeginnersGuide/Download) (click for instructions for installing)

#### Install Django and Django REST framework
```
pip install django
pip install djangorestframework
```

## Setup Project
1. Clone the repository
    ```
    git clone https://github.com/solanum-tuberosums/bangazonOrientationAPI.git
    ```
1. Set up Database
    ```
    cd bangazonOrientationAPI/bangazon/
    python manage.py builddb
    python manage.py createsuperuser
    python manage.py runserver
    ```
1. View in your browser by going to [localhost:8000](http://localhost:8000/)

