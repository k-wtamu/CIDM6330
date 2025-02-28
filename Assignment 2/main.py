from fastapi import FastAPI, HTTPException # 1: imports
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
	"123456": Users(userID=123456, username="Hal" ,  useryearborn=2001, usericon="red circle", useremail=["discovery1@gmail.com"], userphonenumber=["281-111-1111"]),
	"1234567": Users(userID=1234567, username="DRain" ,  useryearborn=1968, usericon="square", useremail=["discovery2@gmail.com"], userphonenumber=["281-222-2222"]),
	"12345678": Users(userID=12345678, username="Joshua" ,  useryearborn=1983, usericon="star", useremail=["falken@gmail.com"], userphonenumber=["281-333-3333"]),
	"12345679": Users(userID=12345679, username="David" ,  useryearborn=1983, usericon="star", useremail=["worp@gmail.com"], userphonenumber=["281-333-3333"]),
}

fooditems = {
	"1111": FoodItem(fooditemUID=1111,  fooditemstatus="available", fooditemquantity=7, fooditemname="banana", fooditemfavorite=True, fooditemspecialtystore=[], fooditemshoppinglist=[], fooditemexpirationdate= datetime.date(2024,12,6),fooditemexpirationreminder=[5,"days",900] , fooditemdaysuntilexpiration=6, fooditemnotes="", fooditemstoragelocation="counter"),
	"1112": FoodItem(fooditemUID=1112,  fooditemstatus="available", fooditemquantity=1, fooditemname="apple pie", fooditemfavorite=False, fooditemspecialtystore=[], fooditemshoppinglist=[], fooditemexpirationdate=datetime.date(2024,12,15), fooditemexpirationreminder=[2,"days",900] , fooditemdaysuntilexpiration=15, fooditemnotes="", fooditemstoragelocation="refridgerator"),
	"1113": FoodItem(fooditemUID=1113,  fooditemstatus="available", fooditemquantity=1, fooditemname="ice cream", fooditemfavorite=True, fooditemspecialtystore=[], fooditemshoppinglist=[], fooditemexpirationdate=datetime.date(2025,1,30), fooditemexpirationreminder=[1,"week",900] , fooditemdaysuntilexpiration=60, fooditemnotes="", fooditemstoragelocation="freezer"),
	"1114": FoodItem(fooditemUID=1114,  fooditemstatus="spolied", fooditemquantity=1, fooditemname="potatoes", fooditemfavorite=False, fooditemspecialtystore=[], fooditemshoppinglist=[], fooditemexpirationdate=datetime.date(2026,12,1), fooditemexpirationreminder=[3,"day",900] , fooditemdaysuntilexpiration=1, fooditemnotes="", fooditemstoragelocation="counter"),
}

choreitems = {
	"111": ChoreItem(choreitemUID=111, choreitemname="sweeping", choreitemduration=[15,"min"], choreitempriority=2, choreitemlocation= ["livingroom","bedroom 2", "hallway"], choreitemnotes=""),
	"222": ChoreItem(choreitemUID=222, choreitemname="dishes", choreitemduration=[25,"min"], choreitempriority=1, choreitemlocation= ["kitchen"], choreitemnotes=""),
	"333": ChoreItem(choreitemUID=333, choreitemname="laundry", choreitemduration=[2,"hour"], choreitempriority=2, choreitemlocation= ["laundry"], choreitemnotes=""),
	"444": ChoreItem(choreitemUID=444, choreitemname="trash", choreitemduration=[30,"min"], choreitempriority=1, choreitemlocation= ["kitchen","bedroom 1", "garage"], choreitemnotes=""),
	"555": ChoreItem(choreitemUID=555, choreitemname="get roof inspected", choreitemduration=[5,"hour"], choreitempriority=3, choreitemlocation= ["roof"], choreitemnotes="Need to schedule time to do research and find a good roofing company to do an inspection"), #!! test for an unscheduled chore !!
}

schedules = {
	"1": ChoreSchedule(scheduleUID=1 , choretocomplete=111,  duedate=datetime.date(2024,12,12), actualcompletiondate=datetime.date(2024,12,11), notification=[""] , choreitemstatus="todo" , repeateevery=[2,"weeks"], repeaton="Thursday", endon=None, endafter=None, assignment=[123456,1234567,12345678,12345679]  ), # Note: this should default to Never end 
	"2": ChoreSchedule(scheduleUID=2 , choretocomplete=222, duedate=datetime.date(2024,3,15), actualcompletiondate=datetime.date(2024,12,15), notification=[""] , choreitemstatus="todo" , repeateevery=[2,"weeks"], repeaton="Thursday" , endon=None, endafter=5, assignment=[12345678]), 
	"3": ChoreSchedule(scheduleUID=3 ,choretocomplete=333, duedate=datetime.date(2024,3,16), actualcompletiondate=datetime.date(2024,12,17), notification=[""] , choreitemstatus="complete" , repeateevery=[1, "month"], repeaton="Monday", endon=datetime.date(2031,1,2),endafter=None, assignment=[123456,12345679]), 
	"4": ChoreSchedule(scheduleUID=4 ,choretocomplete=444, duedate=datetime.date(2024,3,18), actualcompletiondate=datetime.date(2024,12,18), notification=[""] , choreitemstatus="complete" , repeateevery=[3, "days"], repeaton="Monday" , endon=datetime.date(2031,5,5),endafter=None, assignment=[12345679]), 
}


# Note web only uses get, use the fastapi http://127.0.0.1:8000/docs

# 5: create path operation(s) the decorator indicating path and type of operation for each crud 

# Test 
@app.get("/api/greet")

def greet():
    return {"message": "Hello from FastAPI"}
	
@app.get("/api/test/{favorite_fruit}") # test to be sure I understand what the example is doing 
def test_path(favorite_fruit: str):
    return {"message": f"{favorite_fruit} is the best fruit in the world!"}
# end test

# CRUD for Users Entity 

# 5.1: "C" create: create a new users & add to existing dictionary of test data &

@app.post("/api/createnewuser/{userID}")
def create_new_user(userID: int, newuser: Users): # define function that uses PK userID and sets newuser class Users to accept new inputs from API
	if str(userID) in userdata:
		raise HTTPException(status_code=404, detail="Item already exists")	
	else: 
		userdata[str(userID)] = newuser  # adding newuser to userdata dictionary 	
	return {"userID": userID,"item": userdata[str(userID)]}	
	
"""
Test Request Body
{
  "userID": 9999,
  "username": "Turtle",
  "useryearborn": 2025,
  "usericon": "heart",
  "useremail": ["Turtle@gmail.com"],
  "userphonenumber": [""]
}
"""

# 5.2: "R" read:  verify new user is in dictionary, by reading user details based on UserID

@app.get("/api/getuser/{userID}")
def getuser(userID: int): 
	if str(userID) not in userdata:
		raise HTTPException(status_code=404, detail="Item not found")	
	return {"userID": userID,"item": userdata[str(userID)]}
"""
Test 1: get request with userID from test request above 
http://127.0.0.1:8000/api/getuser/9999
Test 2:	test ID 1234567
http://127.0.0.1:8000/api/getuser/1234567
"""

# 5.3: "U" update:  udpdate a users email list to add a secondary email

@app.put("/api/createnewuser/{userID}")
def updateuser(userID: int, newuser: Users): # define function that uses PK userID and sets newuser class Users to accept update inputs from API
	if str(userID) not in userdata:
		raise HTTPException(status_code=404, detail="Item not found")
	else:
		userdata[str(userID)] = newuser  # update newuser data to userdata dictionary 	
	return {"userID": userID,"item": userdata[str(userID)]}


"""
Test Request Body into updateuser
{
  "userID": 9999,
  "username": "Chicken",
  "useryearborn": 2025,
  "usericon": "heart",
  "useremail": ["Turtle@gmail.com"],
  "userphonenumber": [""]
}

check again, and see if its updated
http://127.0.0.1:8000/api/getuser/9999

"""


# 5.4: "D" Delete: delete user account from dictionary 

@app.delete("/api/createnewuser/{userID}")
def deleteuser(userID: str):  
	if str(userID) not in userdata:
		raise HTTPException(status_code=404, detail="Item not found")
	else:
		del userdata[userID]
	return {"message": f"Item {userID} deleted"}

"""
step 1: open the deleteuser in FastAPI docs and select try it out
step 3: userID = 123456
step 4: select execute
	message should say, item has been deleted
step 5: select execute again
	message should say, item not found
step 6: open getuser and select try it out
step 7: userID = 123456
step 8: select execute
	should give you error as its already been deleted

"""
	

# 5.6 additional CRUD opperations for the other entities fooditems, choreitems, schedules to be created later




if __name__ == "__main__": # !! This needs to come after all the api def statements
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
