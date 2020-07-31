from django.shortcuts import render, redirect

def admin_only(view_func):
    """this decorator ensures that a particular page is viewed by the admin only"""
    def wrapper_func(request, *args, **kwargs): 
        group = None #usergroup initialized to none
        if request.user.groups.exists():   #check to see if the user is included in any group
            group = request.user.groups.all()[0].name # if he is, pick the first one and store in the group variable

        if group == 'admin':
            return view_func(request, *args, **kwargs) #return requested view if user is admin

        else:
            return redirect('home') #else, redirect to userpage

    return wrapper_func 