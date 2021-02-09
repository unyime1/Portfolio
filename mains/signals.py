from django.template.loader import render_to_string
from django.db.models.signals import post_save
from django.core import mail
from .models import *

def development_email(sender, instance, created, **kwargs):
    """send mail when someone requests a product"""
    if created:
        full_name = instance.full_name
        phone_number = instance.phone_number
        email = instance.email
        project_title = instance.project_title
        budget = instance.budget
        currency = instance.currency
        project_description = instance.project_description

        dev_message = render_to_string('mains/dev_message.html', {
            'full_name':full_name,
            'phone_number':phone_number,
            'email':email,
            'project_title':project_title,
            'budget':budget,
            'currency':currency,
            'project_description':project_description

        })

        connection = mail.get_connection()

        # Manually open the connection
        connection.open()

        # Construct an email message that uses the connection
        email1 = mail.EmailMessage(
            'Project Request', #title
            dev_message, #message
            'lordunyime@gmail.com', #from
            ['contact@unyimeetim.com'], #to
            connection=connection,
        )
        

        # Send the two emails in a single call -
        connection.send_messages([email1])
        # The connection was already open so send_messages() doesn't close it.
        # We need to manually close the connection.
        connection.close()

post_save.connect(development_email, sender=ProductDevelopment) 