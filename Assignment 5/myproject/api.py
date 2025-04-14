import datetime
from datetime import date

from django.shortcuts import get_object_or_404

from ninja import NinjaAPI, Router, Schema, Field # ###
from ninja import UploadedFile, File

from job.api import router as list_router # ###

from job.models import User
from job.models import FoodItem
from job.models import ChoreItem
from job.models import ChoreSchedule

api = NinjaAPI()
default_router = Router() # ###



class HelloResponseSchema(Schema):
    message: str = Field(..., description="Hello message")
    def hello(request):
        return {"message": "Hello, World!"}
    
@default_router.get("hello/", response=HelloResponseSchema, url_name="hello")
def hello(request):
    return {"message": "Hello, World!"}

api.add_router("/hello", list_router)
api.add_router("/add", list_router)
api.add_router("/user",list_router)
api.add_router("/user/{userID}", list_router)
api.add_router("/fooditem", list_router)
api.add_router("/fooditem/{fooditemUID}", list_router)
api.add_router("/choreitem", list_router)
api.add_router("/choreschedule", list_router)
api.add_router("/choreschedule/{chorescheduleUID}", list_router)