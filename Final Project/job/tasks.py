from django.core.cache import cache
#from prophet.serialize import model_to_json, model_from_json
from celery import shared_task
import requests
import datetime
from datetime import date
from celery.schedules import crontab
from models import User, FoodItem, ChoreItem, ChoreSchedule
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from .models import User, FoodItem, ChoreItem, ChoreSchedule

"""
Celery tasks to implement business rules
"""

# #1 As a user of the basic home management system I would like to recieve a welcome email

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


# #2 As a user of the basic home management system I would like at the begining of the month to get a list of all current food items stored in the system

@shared_task
def send_monthly_food_avail(FoodItem, userID, fooditemstatus = "In Stock"):
    print(f"Sending monthly list of available food items: {datetime.now()}")
# logic for filtering list
    availfoodlist = [item for item in FoodItem if eval(FoodItem.objects.filter(FoodItem.fooditemstatus == "In Stock"))]
# email sending logic here
    try:
        user = User.objects.get(pk=userID)
        send_mail(
            'Monthly list of available food items!',
            f'Hi {user.username}, here is your monthly list of available food items! {availfoodlist}',
            'noreply@example.com',
            [user.email],
            fail_silently=False,
        )
        return f"Monthly available food item list email sent to user {user.username}"
    except User.DoesNotExist:
         return f"User with id {userID} not found."
    except requests.exceptions.RequestException as e:
    # Handle API request exceptions
     print(f"Error - Handle API request exceptions: {e}")
    except Exception as e:
    # Handle other exceptions
         print(f"Error - other exceptions: {e}")
# logic for schedule			
app.conf.beat_schedule = {
    'send-monthly-reminder': {
        'task': 'send_monthly_reminder',
        'schedule': crontab(day_of_month='1'), # Runs on the 1st of every month
    },
}
