from django.core.cache import cache
from prophet.serialize import model_to_json, model_from_json
from celery import shared_task
import requests
import datetime


from django.contrib.auth import get_user_model
from django.core.mail import send_mail
"""
Celery tasks to implement business rules
"""


@shared_task
def test_task_initalSignup(userID):
        # Sends a welcome email to a newly registered user.
        User = get_user_model()
        try:
            user = User.objects.get(pk=userID)
            send_mail(
                'Welcome to Our Site!',
                f'Hi {user.username}, welcome to our website!',
                'noreply@example.com',
                [user.email],
                fail_silently=False,
            )
            return f"Welcome email sent to user {user.username}"
        except User.DoesNotExist:
             return f"User with id {userID} not found."
    except requests.exceptions.RequestException as e:
        # Handle API request exceptions
        print(f"Error - Handle API request exceptions: {e}")
    except Exception as e:
        # Handle other exceptions
        print(f"Error - other exceptions: {e}")
		

# #1 As a user of the basic home management system I would like to have reminders for when food is expiring
"""
 A reminder will be sent one week before expiration for items in the Pantry or Freezer
 A reminder will be sent two days before for items in the refrigerator
"""

# #2 As a user of the basic home management system I would like to view all current food items stored in the system

"""
 Food items can be viewed categorized by location
 Food items can be viewed in alphabetical order
 Food items can be viewed in order of expiration date; sorted by both nearest and farthest expiration in relation to the current date
 Expiration date is defined by Day, Month, Year
 """ 
 
 
 
 # #3  As a user of the basic home management system I would like to designate food items as consumed, disposed of, or in current inventory
 """
 Food items will have a designated status
 Food item statuses include consumed, disposed of, or in current inventory
 """
 
# #4  As a user of the basic home management system I would like to have reminders for daily, monthly, and quarterly cleaning chores
"""
 Cleaning chores can be set as stand alone events or repeat tasks
 """
 
 
 # #5 As a user of the basic home management system I would like to set a new reminder after being given a reminder for daily, monthly, and quarterly cleaning chores

""" 
 When a user gets a reminder, they are prompted with a choice to reschedule
 When a user is choosing to reschedule user can also edit frequency

"""

# #6  As a user of the basic home management system I would like to mark chore tasks as complete
"""
 Cleaning chores will have a designated status
 Cleaning chores statuses include scheduled, late, or completed
"""
