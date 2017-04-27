"""
bangazon factory to create sample data to seed a database using Faker in lieu of using 
fixtures
"""

import factory
from bangazon.api.models import *


class DepartmentFactory(factory.django.DjangoModelFactory):
    """
    This class creates data for the department table in the API's database.

    ----Fields----
    name('company'): fake name of a department
    budget('random_int', min = 1, max = 100): fake budget number

    Author: Jeremy Bakker
    """

    class Meta:
        model = Department
    name = factory.Faker('company')
    budget = factory.Faker('random_int', min=1, max=100)

class CustomerFactory(factory.django.DjangoModelFactory):
    """
    This class creates data for the customer table in the API's database.

    ----Fields----
    first_name('first_name'): fake first name of a customer
    last_name('last_name'): fake last name of a customer
    date('date'): fake account-creation date

    Author: Jeremy Bakker
    """
    
    class Meta:
        model = Customer
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    date_created = factory.Faker('date')

class ComputerFactory(factory.django.DjangoModelFactory):
    """
    This class creates data for the computer table in the API's database.

    ----Fields----
    serial_number('ean13'): fake serial number
    date_purchase('date'): fake purchase date
    date_decommissioned('date'): fake decommission date

    Author: Jeremy Bakker
    """
    
    class Meta:
        model = Computer
    serial_number = factory.Faker('ean13')
    date_purchased = factory.Faker('date')
    date_decommissioned = None

class ProductTypeFactory(factory.django.DjangoModelFactory):
    """
    This class creates data for the product type table in the API's database.

    ----Fields----
    label('word'): fake product type

    Author: Blaise Roberts
    """
    
    class Meta:
        model = ProductType
    label = factory.Faker('word')

class TrainingProgramFactory(factory.django.DjangoModelFactory):
    """
    This class creates data for the training program table in the API's database.

    ----Fields----
    name('bs'): fake training program name
    start_date('date'): fake start date for a training program

    Author: Blaise Roberts
    """
    
    class Meta:
        model = TrainingProgram
    name = factory.Faker('bs')
    start_date = factory.Faker('date')
    end_date = factory.Faker('date')
    max_enrollment = factory.Faker('random_int', min=10, max=100)

class EmployeeFactory(factory.django.DjangoModelFactory):
    """
    This class creates data for the employee table in the API's database.

    ----Fields----
    first_name('first_name'): fake first name of an employee
    last_name('last_name'): fake last name of an employee
    is_supervisor: '0' hard coded as default False
    is_customer_support_specialist: '0' hard coded as default False
    department_id(Iterator[Department]): fake foreign key linked to the department table

    Author: Blaise Roberts
    """
    
    class Meta:
        model = Employee
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_supervisor = 0
    is_customer_support_specialist = 0
    department_id = factory.Iterator(Department.objects.all())

class SupervisorFactory(EmployeeFactory):
    """
    This class inherits from EmployeeFactory and creates data for a supervisor employee in 
    the API's database.

    ----Fields----
    is_supervisor: '1' hard coded to register True 

    Author: Blaise Roberts
    """
    
    is_supervisor = 1

class CustomerSupportSpecialistFactory(EmployeeFactory):
    """
    This class inherits from EmployeeFactory and creates data for a customer-support employee 
    in the API's database.

    ----Fields----
    is_customer_support_specialist: '1' hard coded to register True 

    Author: Jeremy Bakker
    """
    
    is_customer_support_specialist = 1

class ProductFactory(factory.django.DjangoModelFactory):
    """
    This class creates data for the product table in the API's database.

    ----Fields----
    price('random_int'): fake price for a product
    title('word'): fake title of a product
    description('text'): fake description of a product
    product_type(Iterator[ProductType]): fake foreign key linked to the product type table
    customer(Iterator[Customer]): fake foreign key linked to the customer table
    
    Author: Blaise Roberts
    """
    
    class Meta:
        model = Product
    price = factory.Faker('random_int')
    title = factory.Faker('word')
    description = factory.Faker('text')
    product_type = factory.Iterator(ProductType.objects.all())
    customer = factory.Iterator(Customer.objects.all())

class PaymentTypeFactory(factory.django.DjangoModelFactory):
    """
    This class creates data for the payment type table in the API's database.

    ----Fields----
    account_label('word'): fake payment type
    account_type('credit_card_provider'): fake credit card type
    account_number(credit_card_number): fake credit card number
    customer_id(Iterator[Customer]): fake foreign key linked to the customer table
    
    Author: Blaise Roberts
    """
    
    class Meta:
        model = PaymentType
    account_label = factory.Faker('word')
    account_type = factory.Faker('credit_card_provider')
    account_number = factory.Faker('credit_card_number')
    customer_id = factory.Iterator(Customer.objects.all())

class OrderFactory(factory.django.DjangoModelFactory):
    """
    This class creates data for the order table in the API's database.

    ----Fields----
    payment_type_id: Null field hard coded
    order_date('date'): fake date for an order
    customer_id(Iterator[Customer]): fake foreign key linked to the customer table
    
    Author: Blaise Roberts
    """
    
    class Meta:
        model = Order
    payment_type_id = None
    order_date = factory.Faker('date')
    customer_id = factory.Iterator(Customer.objects.all())

class OrderProductFactory(factory.django.DjangoModelFactory):
    """
    This class creates data for the order-product table in the API's database.

    ----Fields----
    product_id(Iterator[Product]): fake foreign key linked to the product table 
    order_id(Iterator[Order]): fake foreign key linked to the order table
    
    Author: Blaise Roberts
    """
    
    class Meta:
        model = OrderProduct
    product_id = factory.Iterator(Product.objects.all())
    order_id = factory.Iterator(Order.objects.all())

class EmployeeComputerFactory(factory.django.DjangoModelFactory):
    """
    This class creates data for the employee-computer table in the API's database.

    ----Fields----
    date_assigned('date'): fake date indicating the date a computer was assigned to an employee
    employee_id(Iterator[Employee]): fake foreign key linked to the employee table 
    computer_id(Iterator[Computer]): fake foreign key linked to the computer table
    
    Author: Blaise Roberts
    """
   
    class Meta:
        model = EmployeeComputer
    date_assigned = factory.Faker('date')
    employee_id = factory.Iterator(Employee.objects.all())
    computer_id = factory.Iterator(Computer.objects.all())

class EmployeeTrainingFactory(factory.django.DjangoModelFactory):
    """
    This class creates data for the employee-training table in the API's database.

    ----Fields----
    training_id(Iterator[TrainingProgram]): fake foreign key linked to the training program table 
    employee_id(Iterator[Employee]): fake foreign key linked to the employee table

    Author: Blaise Roberts
    """

    class Meta:
        model = EmployeeTraining
    training_id = factory.Iterator(TrainingProgram.objects.all())
    employee_id = factory.Iterator(Employee.objects.all())

class CustomerSupportTicketFactory(factory.django.DjangoModelFactory):
    """
    This class creates data for the customer support ticket table in the API's database.

    ----Fields----
    customer_id(Iterator[Customer]): fake foreign key linked to the customer table
    ticket_description('paragraphs'): fake description of a support ticket
    order_id(Iterator[Order]): fake foreign key linked to the order table
    date_created('date'): fake date of a support ticket
    resolution_description('paragraphs'): fake description of a ticket resolution
    date_resolved('date'): fake date of a ticket resolution

    Author: Jeremy Bakker
    """

    class Meta:
        model = CustomerSupportTicket
    customer_id = factory.Iterator(Customer.objects.all())
    ticket_description = factory.Faker('paragraphs', nb=1)
    order_id = factory.Iterator(Order.objects.all())
    date_created = factory.Faker('date')
    resolution_description = factory.Faker('paragraphs', nb=1)
    date_resolved = factory.Faker('date')

class EmployeeTicketFactory(factory.django.DjangoModelFactory):
    """
    This class creates data for the employee-ticket table in the API's database.

    ----Fields----
    date_assigned('date'): fake date indicating the date a computer was assigned to an employee
    employee_id(Iterator[Employee]): fake foreign key linked to the employee table 
    customer_support_ticket_id(Iterator[CustomerSupportTicket]): fake foreign key linked to 
        the customer support ticket table
    
    Author: Jeremy Bakker
    """

    class Meta:
        model = EmployeeTicket
    employee_id = factory.Iterator(Employee.objects.all())
    customer_support_ticket_id = factory.Iterator(CustomerSupportTicket.objects.all())