from fastapi import FastAPI # 1: import
from pydantic import BaseModel
import datetime

# note tuples cant be changed easily, use lists for things likely to change
# note 2, not necessary to define everything by class name inside the class


app = FastAPI() # 2: make app


@app.get("/") # 3: path operation the decorator indicating path and type of operation
	async def root():
    return {"message": "Hello World"}


# Create pydantic models for Entities

class Users(BaseModel):
    	userID: str
	username: str
    	useryearborn: date.year					# may want to just use DOB if this doesnt work and use datetime. date
    	usericon: str 						# may want to update to another way to store image/icon data
	useremail: List[str]
	userphonenumber: List[str]

class FoodItem(BaseModel):
	fooditemUID: str
	fooditemstatus: str  
	fooditemquantity: str 
 	fooditemname: str
	fooditemfavorite: bool
	fooditemspecialtystore: List[str]
	fooditemshoppinglist: List[str] 			# allows for multiple shopping list "tags"
	fooditemexpirationreminder:  List[int | str]		# or maybe its a List[str,int] or  Union[str, int]. https://stackoverflow.com/questions/72111467/why-cant-i-specify-multiple-types-in-a-list-in-pydantic 
	fooditemdaysuntilexpiration: int
	fooditemexpirationdate: datetime.date 			# not sure if pydantic can use datetime.date. need attributes; year, month, and day.
	fooditemnotes: str
	fooditemstoragelocation: str

class ChoreItem(BaseModel):
	choreitemUID: str
	choreitemname: str
	choreitemduration: List[int | str] # needs number and interval
	choreitempriority: int
	choreitemlocation: List[str] # needs household and room 
	choreitemnotes:	str

class ChoreSchedule(BaseModel):
	scheduleUID: str
	duedate: datetime.date 
	actualcompletiondate: datetime.date
	notification:  List[int | str]
	choreitemstatus: str
	repeateevery: List[int | str]				# combines to get the recurrence / frequency schedule 
	repeaton: str 						# combines to get the recurrence / frequency schedule 
	enddetails: List[int | str]				# combines to get the recurrence / frequency schedule 
	assignment: str


# create example data

users = {
"1": Users(UserID=123456, username="Hal" ,  useryearborn=2001, usericon="red circle", useremail="discovery1@gmail.com", userphonenumber="281-111-1111"),
"2": Users(UserID=1234567, username="DRain" ,  useryearborn=1968, usericon="square", useremail="discovery2@gmail.com", userphonenumber="281-222-2222"),
"3": Users(UserID=12345678, username="Joshua" ,  useryearborn=1983, usericon="star", useremail="falken@gmail.com", userphonenumber="281-333-3333"),
"4": Users(UserID=12345678, username="David" ,  useryearborn=1983, usericon="star", useremail="worp@gmail.com", userphonenumber="281-333-3333")
}

fooditems = {
"1": FoodItem(fooditemUID=1111,  fooditemstatus="available", fooditemquantity=7, fooditemname:"banana", fooditemfavorite=TRUE, fooditemspecialtystore=[], fooditemshoppinglist=[], fooditemexpirationdate="12/6/2024",fooditemexpirationreminder=[5,"days",0900] , fooditemdaysuntilexpiration=6, fooditemnotes="", fooditemstoragelocation="counter"),
"2": FoodItem(fooditemUID=1112,  fooditemstatus="available", fooditemquantity=1, fooditemname:"apple pie", fooditemfavorite=FALSE, fooditemspecialtystore=[], fooditemshoppinglist=[], fooditemexpirationdate="12/15/2024", fooditemexpirationreminder=[2,"days",0900] , fooditemdaysuntilexpiration=15, fooditemnotes="", fooditemstoragelocation="refridgerator"),
"3": FoodItem(fooditemUID=1112,  fooditemstatus="available", fooditemquantity=1, fooditemname:"ice cream", fooditemfavorite=TRUE, fooditemspecialtystore=[], fooditemshoppinglist=[], fooditemexpirationdate="01/30/2025", fooditemexpirationreminder=[1,"week",0900] , fooditemdaysuntilexpiration=60, fooditemnotes="", fooditemstoragelocation="freezer")
"4": FoodItem(fooditemUID=1112,  fooditemstatus="spolied", fooditemquantity=1, fooditemname:"potatoes", fooditemfavorite=FALSE, fooditemspecialtystore=[], fooditemshoppinglist=[], fooditemexpirationdate="12/01/2026", fooditemexpirationreminder=3,"day",0900] , fooditemdaysuntilexpiration=1, fooditemnotes="", fooditemstoragelocation="counter")
}

choreitems ={
"1": ChoreItem(choreitemUID=111, choreitemname="sweeping", choreitemduration=[15,"min"], choreitempriority=2, choreitemlocation= ["livingroom","bedroom 2", "hallway"], choreitemnotes=""),
"2": ChoreItem(choreitemUID=222, choreitemname="dishes", choreitemduration=[25,"min"], choreitempriority=1, choreitemlocation= ["kitchen"], choreitemnotes=""),
"3": ChoreItem(choreitemUID=333, choreitemname="laundry", choreitemduration=[2,"hour"], choreitempriority=2, choreitemlocation= ["laundry"], choreitemnotes=""),
"4": ChoreItem(choreitemUID=444, choreitemname="trash", choreitemduration=[30,"min"], choreitempriority=1, choreitemlocation= ["kitchen","bedroom 1", "garage"], choreitemnotes=""),
}

schedules = {
"1": ChoreSchedules(scheduleUID=1 , duedate=12/12/2024 , actualcompletiondate=12/11/2024 , notification="" , choreitemstatus="complete" , repeateevery=[2,"weeks"], repeaton="Thursday" , enddetails="Never" ), 
"2": ChoreSchedules(scheduleUID=2 , duedate=12/15/2024 , actualcompletiondate=12/15/2024 , notification="" , choreitemstatus="complete" , repeateevery=[2,"weeks]" , repeaton="Thursday" , enddetails="5" ), 
"3": ChoreSchedules(scheduleUID=3 , duedate=12/16/2024 , actualcompletiondate=12/17/2024 , notification="" , choreitemstatus="complete" , repeateevery=[1, "month"] , repeaton="Monday", enddetails="01/02/2031" ), 
"4": ChoreSchedules(scheduleUID=4 , duedate=12/18/2024 , actualcompletiondate=12/18/2024 , notification="" , choreitemstatus="complete" , repeateevery=[3, "days"] , repeaton="Monday" , enddetails= "05/05/2031"), 
}



@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/users/{userID}")
def read_item(userID: int): # read user id
    return {"userID": userID, "user": users[str(userID)]}

@app.put("/users/{userID}")
def update_item(userID: int, user: Users):
    user[str(userID)] = user  # update the pet in the dictionary
    # however, without a persistence strategy, this will be lost when the server restarts
    return {"userID": userID, "item": Users[str(userID)]}
