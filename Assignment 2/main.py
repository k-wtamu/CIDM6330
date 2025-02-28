from fastapi import FastAPI # 1: imports
from pydantic import BaseModel
from typing import Optional
import datetime


# note tuples cant be changed easily, use lists for things likely to change
# note 2, not necessary to define everything by class name inside the class


app = FastAPI() # 2: make app


# 3: Create pydantic models for Entities

class Users(BaseModel):
	userID: int
	username: str
	useryearborn: int					# Todo: will need to later limit the years between XXXX & YYYY too complicated if we just want year datetime.date.year				
	usericon: str 						# Note: may want to update to another way to store image/icon data
	useremail: list[str]
	userphonenumber: list[str]

class FoodItem(BaseModel):
	fooditemUID: int
	fooditemstatus: str  
	fooditemquantity: int 
	fooditemname: str
	fooditemfavorite: bool
	fooditemspecialtystore: list[str]
	fooditemshoppinglist: list[str] 			# Note: allows for multiple shopping list "tags"
	fooditemexpirationreminder:  list[int | str]		# Note: or maybe its a List[str,int] or  Union[str, int]. https://stackoverflow.com/questions/72111467/why-cant-i-specify-multiple-types-in-a-list-in-pydantic 
	fooditemdaysuntilexpiration: int
	fooditemexpirationdate: datetime.date 			#Note: using datetime.date because need attributes; year, month, and day.
	fooditemnotes: str
	fooditemstoragelocation: str

class ChoreItem(BaseModel):
	choreitemUID: int
	choreitemname: str
	choreitemduration: list[int | str] # Note: needs number and interval
	choreitempriority: int
	choreitemlocation: list[str]			 # Review: needs ability to store household and room if needed, so maybe seaperate these
	choreitemnotes:	str

class ChoreSchedule(BaseModel):
	scheduleUID: int
	choretocomplete: int # !!FK for the chore you are scheduling!!
	duedate: datetime.date 
	actualcompletiondate: datetime.date
	notification:  list[int | str]
	choreitemstatus: str
	repeateevery: list[int | str]				# Note: combines to get the recurrence / frequency schedule 
	repeaton: str 								# Note:combines to get the recurrence / frequency schedule 
	endon: Optional[datetime.date] = None						# Note:combines to get the "Ends" part of the recurrence schedule
	endafer: Optional[int] = None								# Todo: both of these are defaulted to = None so by defalult the Never attribute = True. when cretaing the code if endon = None &if endafter = None then set Never = True 
	assignment: list[int] # !!FK for the chore you are assigning to people!!


# 4: create example data

userdata = {
	"1": Users(userID=123456, username="Hal" ,  useryearborn=2001, usericon="red circle", useremail=["discovery1@gmail.com"], userphonenumber=["281-111-1111"]),
	"2": Users(userID=1234567, username="DRain" ,  useryearborn=1968, usericon="square", useremail=["discovery2@gmail.com"], userphonenumber=["281-222-2222"]),
	"3": Users(userID=12345678, username="Joshua" ,  useryearborn=1983, usericon="star", useremail=["falken@gmail.com"], userphonenumber=["281-333-3333"]),
	"4": Users(userID=12345679, username="David" ,  useryearborn=1983, usericon="star", useremail=["worp@gmail.com"], userphonenumber=["281-333-3333"]),
}

fooditems = {
	"1": FoodItem(fooditemUID=1111,  fooditemstatus="available", fooditemquantity=7, fooditemname="banana", fooditemfavorite=True, fooditemspecialtystore=[], fooditemshoppinglist=[], fooditemexpirationdate= datetime.date(2024,12,6),fooditemexpirationreminder=[5,"days",900] , fooditemdaysuntilexpiration=6, fooditemnotes="", fooditemstoragelocation="counter"),
	"2": FoodItem(fooditemUID=1112,  fooditemstatus="available", fooditemquantity=1, fooditemname="apple pie", fooditemfavorite=False, fooditemspecialtystore=[], fooditemshoppinglist=[], fooditemexpirationdate=datetime.date(2024,12,15), fooditemexpirationreminder=[2,"days",900] , fooditemdaysuntilexpiration=15, fooditemnotes="", fooditemstoragelocation="refridgerator"),
	"3": FoodItem(fooditemUID=1112,  fooditemstatus="available", fooditemquantity=1, fooditemname="ice cream", fooditemfavorite=True, fooditemspecialtystore=[], fooditemshoppinglist=[], fooditemexpirationdate=datetime.date(2025,1,30), fooditemexpirationreminder=[1,"week",900] , fooditemdaysuntilexpiration=60, fooditemnotes="", fooditemstoragelocation="freezer"),
	"4": FoodItem(fooditemUID=1112,  fooditemstatus="spolied", fooditemquantity=1, fooditemname="potatoes", fooditemfavorite=False, fooditemspecialtystore=[], fooditemshoppinglist=[], fooditemexpirationdate=datetime.date(2026,12,1), fooditemexpirationreminder=[3,"day",900] , fooditemdaysuntilexpiration=1, fooditemnotes="", fooditemstoragelocation="counter"),
}

choreitems = {
	"1": ChoreItem(choreitemUID=111, choreitemname="sweeping", choreitemduration=[15,"min"], choreitempriority=2, choreitemlocation= ["livingroom","bedroom 2", "hallway"], choreitemnotes=""),
	"2": ChoreItem(choreitemUID=222, choreitemname="dishes", choreitemduration=[25,"min"], choreitempriority=1, choreitemlocation= ["kitchen"], choreitemnotes=""),
	"3": ChoreItem(choreitemUID=333, choreitemname="laundry", choreitemduration=[2,"hour"], choreitempriority=2, choreitemlocation= ["laundry"], choreitemnotes=""),
	"4": ChoreItem(choreitemUID=444, choreitemname="trash", choreitemduration=[30,"min"], choreitempriority=1, choreitemlocation= ["kitchen","bedroom 1", "garage"], choreitemnotes=""),
	"5": ChoreItem(choreitemUID=555, choreitemname="get roof inspected", choreitemduration=[5,"hour"], choreitempriority=3, choreitemlocation= ["roof"], choreitemnotes="Need to schedule time to do research and find a good roofing company to do an inspection"), #!! test for an unscheduled chore !!
}

schedules = {
	"1": ChoreSchedule(scheduleUID=1 , choretocomplete=111,  duedate=datetime.date(2024,12,12), actualcompletiondate=datetime.date(2024,12,11), notification=[""] , choreitemstatus="complete" , repeateevery=[2,"weeks"], repeaton="Thursday", endon=None, endafter=None, assignment=[123456,1234567,12345678,12345679]  ), # Note: this should default to Never end 
	"2": ChoreSchedule(scheduleUID=2 , choretocomplete=222, duedate=datetime.date(2024,3,15), actualcompletiondate=datetime.date(2024,12,15), notification=[""] , choreitemstatus="complete" , repeateevery=[2,"weeks"], repeaton="Thursday" , endon=None, endafter=5, assignment=[12345678]), 
	"3": ChoreSchedule(scheduleUID=3 ,choretocomplete=333, duedate=datetime.date(2024,3,16), actualcompletiondate=datetime.date(2024,12,17), notification=[""] , choreitemstatus="complete" , repeateevery=[1, "month"], repeaton="Monday", endon=datetime.date(2031,1,2),endafter=None, assignment=[123456,12345679]), 
	"4": ChoreSchedule(scheduleUID=4 ,choretocomplete=444, duedate=datetime.date(2024,3,18), actualcompletiondate=datetime.date(2024,12,18), notification=[""] , choreitemstatus="complete" , repeateevery=[3, "days"], repeaton="Monday" , endon=datetime.date(2031,5,5),endafter=None, assignment=[12345679]), 
}


# 5: create path operation(s) the decorator indicating path and type of operation for each crud 

# Test 
@app.get("/api/greet")

def greet():
    return {"message": "Hello from FastAPI"}
	
@app.get("/api/test") # test to be sure I understand what the example is doing 
def test_root():
    return {"Hello": "World"}
# end test



# 5.1: "C" create: create a new user & add to existing dictionary of test data

@app.post("/api/createuser/{userID}")
async def create_new_user( : Users)

	return 
	




# 5.2: "R" read: read user information based on a specific user id

#@app.get("/users/{userID}")
#def read_item(userID: int): 
 #   return {"userID": userID, "user": users[str(userID)]}



# 5.3: "U" update:  udpdate a users email list to add a secondary email




# 5.4: "D" Delete: delete user account from dictionary 



#@app.put("/users/{userID}")
#def update_item(userID: int, user: Users):
#    user[str(userID)] = user  # update the pet in the dictionary
    # however, without a persistence strategy, this will be lost when the server restarts
#    return {"userID": userID, "item": Users[str(userID)]}


if __name__ == "__main__": # !! This needs to come after all the api def statements
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

"""
Build CRUD statements from decorators available:
@app.get()
@app.post()
@app.put()
@app.delete()
@app.options()
@app.head()
@app.patch()
@app.trace()
"""
