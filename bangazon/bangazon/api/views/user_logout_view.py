from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse


# Use the login_required() decorator to ensure only 
# those logged in can access the view.
@login_required
def user_logout(request):
    """
    This method is invoked to logout the user and redirect them to the index

     ---Arguments---
    None

    Author: Beve Strownlee & Blaise Roberts
    """

    # Since we know the user is logged in, we can now just log them out.
    logout(request)