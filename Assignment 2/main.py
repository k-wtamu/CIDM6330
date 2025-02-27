from fastapi import FastAPI # 1: import
from pydantic import BaseModel
import datetime

# note tuples cant be changed easily, use lists for things likely to change
# note 2, not nesisary to define everything by class name inside the class


app = FastAPI() # 2: make app


@app.get("/") # 3: path operation the decorator indicating path and type of operatation
#	async def root():
#    return {"message": "Hello World"}


# Create pydantic models for Entities

class Users(BaseModel):
    	userID: str
	username: str
    	useryearborn: date.year					# may want to just use DOB if this doesnt work and use datetime.date
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
	fooditemexpirationreminder:  list[int | str]		# or maybe its a List[str,int] or  Union[str, int]. https://stackoverflow.com/questions/72111467/why-cant-i-specify-multiple-types-in-a-list-in-pydantic 
	fooditemdaysuntilexpiration: int
	fooditemexpirationdate: datetime.date 				# not sure if pydantic can use datetime.date. need attributes; year, month, and day.
	fooditemnotes: str
	fooditemstoragelocation: str

class ChoreItem(BaseModel):
	choreitemUID: str
	choreitemname: str
	choreitemduration: # needs number and interval
	choreitempriority: # ???
	choreitemlocation: # str ?? needs household and room 
	chireitemnotes:	str

class ChoreSchedule(BaseModel):
	scheduleUID:str
	duedate: datetime.date 
	actualcompletiondate: datetime.date
	notification: int, interval, hour of date
	choreitemstatus: str
	recurrence:3 pieces broken down further
	assignment: str


# create example data

users = {
"1": Users( UserID=123456,  fooditemstatus=  ...),
"2": Users( .....
}

fooditem = {
"1": FoodItem( fooditemUID= 1111,  = ...),
"2": FoodItem( .....
}

