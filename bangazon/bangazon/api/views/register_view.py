from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from bangazon.api.views.login_user_view import login_user

def register_user(request):
    '''Handles the creation of a new user for authentication
    Method arguments:
      request -- The full HTTP request object
    '''

    # Load the JSON string of the request body into a dict
    req_body = json.loads(request.body.decode())

    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    new_user = User.objects.create_user(
                    username=req_body['username'],
                    password=req_body['password'],
                    email=req_body['email'],
                    first_name=req_body['first_name'],
                    last_name=req_body['last_name'],
                    )

    # Commit the user to the database by saving it
    new_user.save()

    return login_user(request)


# def register(request):
    """
    Handles the creation of a new user for authentication
    ---Arguments---
    None
    ---GET---
    Renders register.html
        ---Context---
        'user_form': the form from user_form.py
    ---POST---
    runs the login_user function
    Author: Steve Browlee
    """

    # A boolean value for telling the template 
    # whether the registration was successful.
    # Set to False initially. Code changes value to True when registration 
    # succeeds.
    # registered = False

    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    # if request.method == 'POST':
    #     user_form = UserForm(data=request.POST)

    #     if user_form.is_valid():
    #         # Save the user's form data to the database.
    #         user = user_form.save()

    #         # Now we hash the password with the set_password method.
    #         # Once hashed, we can update the user object.
    #         user.set_password(user.password)
    #         user.save()

    #         # Update our variable to tell the template 
    #         # registration was successful.
    #         registered = True

    #     return login_user(request)

    # elif request.method == 'GET':
    #     user_form = UserForm()
    #     template_name = 'register.html'
    #     return render(request, template_name, {'user_form': user_form})

