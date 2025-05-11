from datetime import datetime, date
from ninja import Router, Field, Schema, FilterSchema
# from prophet.serialize import model_to_json, model_from_json
from django.core.cache import cache
# import pandas as pd
# import requests
#NEW#
from pydantic import BaseModel, ConfigDict
from job.models import User, FoodItem, ChoreItem, ChoreSchedule



router = Router()


# Tests

@router.get("/hello")
def hello(request):
    return {"message": "Hello, World!"}

@router.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}


"""
# START for Users
"""

# This is an input schema for the Users Table
class UsersIn(Schema):
	username: str
	birthdate: date						
	usericon: str 						
	useremail: str	
#	userphonenumber: int = None	

	
# this is to delete/replace
class UsersOut(Schema):
	userID: int # unique to out, generated
	username: str
	birthdate: date						
	usericon: str 						
	useremail: str	
#	userphonenumber: int = None	


@router.post("/user")
def create_user(request, user: UsersIn):
    newuser_info = user.dict()
    newuser = user(newuser_info)
    user = user.objects.create(newuser)    

    return user

@router.get("/user/{userID}", response=UsersOut)
def get_user(request, userID: int):
    user = get_object_or_404(User, id=userID)
    return user

@router.get("/user", response=list[UsersOut])
def list_user(request):
    user = User.objects.all()
    return user

@router.put("/user/{userID}")
def update_user(request, userID: int, payload: UsersIn):
    user = get_object_or_404(User, id=userID)
    user.usericon = user.usericon
    user.username = user.username
    user.userphonenumber = user.userphonenumber
    user.birthdate = user.birthdate
    user.useremail = user.useremail
    user.userID = user.userID

    for attr, value in payload.dict().items():
        setattr(user, attr, value)
    user.save()
    return {"success": True, "user": user}

@router.delete("/user/{userID}")
def delete_user(request, userID: int):
    user = get_object_or_404(User, id=userID)
    user.delete()
    return {"success": True, "user": user}
	


"""
# START for FoodItem
"""

# This is an input schema for the FoodItem Table
class FoodItemIn(Schema):
	fooditemstatus: str
	fooditemquantity: int
	fooditemname: str
	fooditemfavorite: bool#= None
	fooditemspecialtystore: str#= None
	fooditemshoppinglist: str#= None 
	fooditemexpirationreminder: str# = None
	fooditemexpirationdate: date 
	fooditemnotes: str #= None
	fooditemstoragelocation: str #= None

# this is to delete/replace
class FoodItemOut(Schema):
	fooditemUID: int  # unique to out, generated
	fooditemstatus: str  
	fooditemquantity: int 
	fooditemname: str
	fooditemfavorite: bool = None
	fooditemspecialtystore: str = None
	fooditemshoppinglist: str = None 			 
	fooditemexpirationreminder:  str = None
	fooditemdaysuntilexpiration: int # unique to out, calculated
	fooditemexpirationdate: date 		 
	fooditemnotes: str = None
	fooditemstoragelocation: str = None


@router.post("/fooditem")
def create_fooditem(request, fooditem: FoodItemIn):
    fooditem_info = fooditem.dict()
    fooditem = FoodItem(**fooditem_info)
    fooditem = FoodItem.objects.create(fooditem)    

    return fooditem

@router.get("/fooditem/{fooditemUID}", response=FoodItemOut)
def get_fooditem(request, fooditemUID: int):
    fooditem = get_object_or_404(FoodItem, id=fooditemUID)
    return fooditem

@router.get("/fooditem", response=list[FoodItemOut])
def list_fooditem(request):
    fooditem = FoodItem.objects.all()
    return fooditem

@router.put("/fooditem/{fooditemUID}")
def update_fooditem(request, fooditemUID: int, payload: FoodItemIn):
    fooditem = get_object_or_404(FoodItem, id=fooditemUID)
#    fooditem.fooditemstatus = fooditem.fooditemstatus
#    fooditem.fooditemquantity = fooditem.fooditemquantity
#    fooditem.fooditemname = fooditem.fooditemname
#    fooditem.fooditemfavorite = fooditem.fooditemfavorite
#    fooditem.fooditemspecialtystore = fooditem.fooditemspecialtystore
#    fooditem.fooditemsUID = fooditem.fooditemsUID
#    fooditem.fooditemshoppinglist = fooditem.fooditemshoppinglist
#    fooditem.fooditemexpirationreminder = fooditem.fooditemexpirationreminder
#    fooditem.fooditemdaysuntilexpiration = fooditem.fooditemdaysuntilexpiration
#    fooditem.fooditemexpirationdate = fooditem.fooditemexpirationdate
#    fooditem.fooditemnotes = fooditem.fooditemnotes
#    fooditem.fooditemstoragelocation = fooditem.fooditemstoragelocation

    for attr, value in payload.dict().items():
        setattr(fooditem, attr, value)
    fooditem.save()
    return {"success": True, "fooditem": fooditem}

@router.delete("/fooditem/{fooditemUID}")
def delete_fooditem(request, fooditemUID: int):
    fooditem = get_object_or_404(FoodItem, id=fooditemUID)
    fooditem.delete()
    return {"success": True, "fooditem": fooditem}
	

"""
# START for ChoreItem 
"""

# This is an input schema for the ChoreItem Table
class ChoreItemIn(Schema):
	choreitemname: str
	choreitemduration: str
	choreitempriority: int = None
	choreitemlocation: str = None
	choreitemnotes:	str	= None

# this is to delete/replace
class ChoreItemOut(Schema):
	choreitemUID: int  # unique to out, generated
	choreitemname: str
	choreitemduration: str
	choreitempriority: int = None
	choreitemlocation: str = None
	choreitemnotes:	str	= None


@router.post("/choreitem")
def create_choreitem(request, choreitem: ChoreItemIn):
    choreitem_info = choreitem.dict()
    choreitem = ChoreItem(**choreitem_info)
    choreitem = ChoreItem.objects.create(choreitem)    

    return choreitem

@router.get("/choreitem/{choreitemUID}", response=ChoreItemOut)
def get_choreitem(request, choreitemUID: int):
    choreitem = get_object_or_404(ChoreItem, id=choreitemUID)
    return choreitem

@router.get("/choreitem", response=list[ChoreItemOut])
def list_choreitem(request):
    choreitem = ChoreItem.objects.all()
    return choreitem

@router.put("/choreitem/{choreitemUID}")
def update_choreitem(request, choreitemUID: int, payload: ChoreItemIn):
    choreitem = get_object_or_404(ChoreItem, id=choreitemUID)
#    choreitem.choreitemsUID = choreitem.choreitemsUID
#    choreitem.choreitemname = choreitem.choreitemname
#    choreitem.choreitemduration = choreitem.choreitemduration
#    choreitem.choreitempriority = choreitem.choreitempriority
#    choreitem.choreitemlocation = choreitem.choreitemlocation
#    choreitem.choreitemnotes = choreitem.choreitemnotes

    for attr, value in payload.dict().items():
        setattr(choreitem, attr, value)
    choreitem.save()
    return {"success": True, "choreitem": choreitem}

@router.delete("/choreitem/{choreitemUID}")
def delete_choreitem(request, choreitemUID: int):
    choreitem = get_object_or_404(ChoreItem, id=choreitemUID)
    choreitem.delete()
    return {"success": True, "choreitem": choreitem}
	


"""
# START for ChoreSchedule
"""

# This is an input schema for the ChoreSchedule Table
class ChoreScheduleIn(Schema):
	choretocomplete: int # !!FK for the chore you are scheduling!!
	duedate: date 
	actualcompletiondate: date
	notification:  str
	choreitemstatus: str
	repeateevery:  str
	repeaton: str 								 
	endon:  date = None						
	endafer: int = None								
	assignment:  str	

# this is to delete/replace
class ChoreScheduleOut(Schema):
	chorescheduleUID: int   # unique to out, generated
	choretocomplete: int # !!FK for the chore you are scheduling!!
	duedate: date 
	actualcompletiondate: date
	notification:  str
	choreitemstatus: str
	repeateevery:  str
	repeaton: str 								 
	endon: date = None						
	endafer: int = None								
	assignment:  str	
	

@router.post("/choreschedule")
def create_choreschedule(request, choreschedule: ChoreScheduleIn):
    choreschedule_info = choreschedule.dict()
    choreschedule = ChoreSchedule(**choreschedule_info)
    choreschedule = ChoreSchedule.objects.create(choreschedule)    

    return choreschedule

@router.get("/choreschedule/{chorescheduleUID}", response=ChoreScheduleOut)
def get_choreschedule(request, chorescheduleUID: int):
    choreschedule = get_object_or_404(ChoreSchedule, id=chorescheduleUID)
    return choreschedule

@router.get("/choreschedule", response=list[ChoreScheduleOut])
def list_choreschedule(request):
    choreschedule = ChoreSchedule.objects.all()
    return choreschedule

@router.put("/choreschedule/{chorescheduleUID}")
def update_choreschedule(request, chorescheduleUID: int, payload: ChoreScheduleIn):
    choreschedule = get_object_or_404(ChoreSchedule, id=chorescheduleUID)
#    choreschedule.choreschedulesUID = choreschedule.choreschedulesUID
#    choreschedule.choreschedulename = choreschedule.choreschedulename
#    choreschedule.chorescheduleduration = choreschedule.chorescheduleduration
#    choreschedule.choreschedulepriority = choreschedule.choreschedulepriority
#    choreschedule.choreschedulelocation = choreschedule.choreschedulelocation
#    choreschedule.choreschedulenotes = choreschedule.choreschedulenotes

    for attr, value in payload.dict().items():
        setattr(choreschedule, attr, value)
    choreschedule.save()
    return {"success": True, "choreschedule": choreschedule}

@router.delete("/choreschedule/{chorescheduleUID}")
def delete_choreschedule(request, chorescheduleUID: int):
    choreschedule = get_object_or_404(ChoreSchedule, id=chorescheduleUID)
    choreschedule.delete()
    return {"success": True, "choreschedule": choreschedule}



# Beyond basic CRUD Statments - data aggregation/reporting 

# Return number of food items that are favorited

@router.get("/numfavoritefooditem/", response=FoodItemOut)
def get_num_fav_fooditem(request):
	allfooditem = FoodItem.objects.all()
	numfavfooditem = sum(1 for item in allfooditem if FoodItem.fooditemfavorite == True)
	return {"count": numfavfooditem}

# Return a list of all items that are favorited

@router.get("/listfavoritefooditem", response=list[FoodItemOut])
def list_fav_fooditem(request):# filters:FoodItem Query(fooditemfavorite == True) ):
	listfavfooditem = FoodItem.objects.filter(FoodItem.fooditemfavorite == True)
	#	allfooditem = FoodItem.objects.all()
	#	allfooditem if FoodItem.fooditemfavorite == True
	return listfavfooditem
