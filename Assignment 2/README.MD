# Home Food and Chore Management System  

**Assignment 2 Note: select here to skip to [python API](#API-in-Python-using-FastAPI) and [ERD](#Entity-Relationship-Diagram)** 


**Student:** Kristen Brunngraber

**Class:**  2025SP SOFTWARE ARCH. (CIDM-6330-70)

**Date:**  28 February 2025

------------------------------------------------------------------------------------------------


## Introduction 

##### A problem for which a designed software system could assist in improving or solving
As people are getting more used to companies tracking *(and using)* the meta data that is constantly being tracked in virtually every interaction we have, from any purchase with a debit or credit card to the streaming services and social media apps we use, it would be nice to see some additional benefits other than targeted ads. 
Additionally, with increasing use of smart technology I can see the application of new technologies that track items that enter your home and ones that help track consumption. A smart trashcan that can scan barcodes on boxes or image recognition to identify used items and subtract it off the current household inventory list. It would be an integrated software system to assist a persons non-virtual life. Easy tracking, searching, and accessing an array of household information. The specs and standards for all my appliances, a digital accounting of all the books, games, furniture *(including dimensions)*, stock of the items in your fridge, integration with your streaming services to track what you have watched, maintenance and replacement schedules, and the ability to integrate your smart assistant (Echo, Nest, Siri) to allow for voice communication, archive, and access for information. 
For very wealthy people, you could preauthorize purchases for items when it knows you are getting low. Or even have your home be [adaptive and reactive](https://news.mit.edu/2018/AI-identifies-people-indoor-smart-homes-1017#:~:text=When%20Betsy%20returns%20to%20the,monitoring%20and%20responsive%20smart%20homes.) to you. 

##### The domain of practice or interest in which this problem is situated
This would fit within the technology industry and computer science domain and could be utilized in people homes to make their lives easier, like a simpler version of [Jarvis](https://en.wikipedia.org/wiki/J.A.R.V.I.S.) , as an AI assistant that could help relieve the burden of running your home. 

#####  Your personal/professional interest in this problem domain
Personal interest would be to reduce mental burden of keeping up with daily life and responsibilities. It would allow me far more free time outside of work, where I don’t feel I need to get a hundred things done at every moment of my life. If integrated with your fridge or grocery purchases it could also help reduce food waste and excess in the house. 
I don’t need total efficiency in my life, but it would *(to reference the assignment description)* maximize the benefit of all my smart systems and devices in the house. 

#####  What sort of system you want to prototype that would allow you to better understand the problem, problem domain, or design considerations thereon.

__To scope this down for this class, I am focusing on the software architecture of a home task and maintenance management system.__

<mark> This prototype would be a basic home management system to send prescheduled and suggested tasks and inventory reminders to the user to check off as complete or schedule for later. Task and maintenance will be limited in this initial design to food and cleaning type household responsibilities. Eating and cleaning are two of the most basic functions in the household, and this projects protype will start here.</mark>


------------------------------------------------------------------------------------------------


## Contents

1. [Requirements statements](#Requirements-Statements)
    1. [User Stories] 
    2. [Use Cases] 
    3. [Features] 
    4. [Gherkin Validation] 

2. [Specifications](#Specifications)
    1. [Concept] 
    2. [UX Notes] 
    3. [Interfaces (Controls)] 
    4. [Behaviors] 
        1. Feature/Package A (appropriate UML diagrams)
        2. Feature/Package N (appropriate UML diagrams)
3. [Entity Relationship Diagram](#Entity-Relationship-Diagram)
4. [API in Python using FastAPI](#API-in-Python-using-FastAPI)

------------------------------------------------------------------------------------------------


##  Requirements Statements


### 1a. User Stories

**As a user of the basic home management system I would like to have reminders for when food is expiring**

Confirmations/Acceptance Criteria: 
- [ ] Items with a best buy date will have the date stored as the expiration date
- [ ] Food locations are defined as either Pantry, Refrigerator, or Freezer
- [ ] A reminder will be sent one week before expiration for items in the Pantry or Freezer
- [ ] A reminder will be sent two days before for items in the refrigerator
- [ ] All foods will have a designated expiration date

**As a user of the basic home management system I would like to view all current food items stored in the system**

Confirmations/Acceptance Criteria: 
- [ ] Food item names will be between three and 50 characters 
- [ ] Food items can be viewed categorized by location
- [ ] Food items can be viewed in alphabetical order
- [ ] Food items can be viewed in order of expiration date; sorted by both nearest and farthest expiration in relation to the current date 
- [ ] Expiration date is defined by Day, Month, Year

**As a user of the basic home management system I would like to designate food items as consumed, disposed of, or in current inventory**

Confirmations/Acceptance Criteria: 
- [ ] Food items will have a designated status
- [ ] Food item statuses include consumed, disposed of, or in current inventory

**As a user of the basic home management system I would like to have reminders for daily, monthly, and quarterly cleaning chores**

Confirmations/Acceptance Criteria: 
- [ ] Cleaning chores should have a task due date
- [ ] Cleaning chores can be set as stand alone events or repeat tasks
- [ ] Cleaning chores have a location assigned to include bathroom, living room, kitchen, bedroom, garage, garden, etc. 
- [ ] Repeat cleaning chores can be set as daily, weekly, monthly, or quarterly tasks
- [ ] Repeat cleaning chores should have one or more selected day(s) of the week to be repeated

**As a user of the basic home management system I would like to set a new reminder after being given a reminder for daily, monthly, and quarterly cleaning chores**

Confirmations/Acceptance Criteria: 
- [ ] When a user gets a reminder, they are prompted with a choice to reschedule
- [ ] When a user is choosing to reschedule user can also edit frequency 

**As a user of the basic home management system I would like to mark chore tasks as complete**

Confirmations/Acceptance Criteria: 
- [ ] Cleaning chores will have a designated status
- [ ] Cleaning chores statuses include scheduled, late, or completed



### 1b.Use Cases

**Name: Enter new Food Item**

**Identifier: UC-1**

**Base Course of Action**
- User selects system function (example selects a button) for entering in a new food item to track
- System presents user with mandatory blank entry fields for Item Name (Free text), Item location (dropdown), Expiration date (Date field)
- User enters in the Item name
- System verifies the item name field is not blank
- System saves the item name
- User selects the Item location
- System verifies the item location field is not blank
- System saves the item location
- User enters/selects the item expiration date
- System verifies the item expiration date field is not blank
- System verifies the item expiration date is not before todays date
- System saves the expiration date
- System presents user with optional blank entry fields for Notes
- System saves notes field if not empty
- System sets item status to in current inventory
- System provides verification item has been saved to inventory

**Name: Update Food Item**

**Identifier: UC-2**

**Base Course of Action**
- User selects Food item to update from list of items in inventory
- System displays food item details: Item name, Item location, Expiration date, Notes
- User selects field to edit
- System increases edit area for user to detail changes and displays an save or discard changes function to user
- User edits field and selects save or discard
- System saves updated information if save is selected, or discards changes if discard is selected
- System provides verification item has been updated or changes have been discarded
- System displays list of items

**Name:  Enter Cleaning Chore** 
**Identifier: UC-3** 
**Base Course of Action**  
- User selects system function (example selects a button) for entering in a new cleaning chore
- System presents user with mandatory blank entry fields for Chore Name (Free text), Chore location (dropdown), Chore date (Date field)
- User enters in the cleaning chore name
- System verifies the cleaning chore name field is not blank
- System saves the cleaning chore name
- User selects the cleaning chore location
- System verifies the cleaning chore location field is not blank
- System saves the cleaning chore location
- User enters/selects the cleaning chore date
- System verifies the cleaning chore  date field is not blank
- System verifies the cleaning chore date is not before todays date
- System saves the cleaning chore date
- System presents user with optional blank entry fields for Notes
- System saves notes field if not empty
- System provides verification cleaning chore has been saved to management system

**Name: Update Cleaning Chore** 
**Identifier: UC-4** 
**Base Course of Action**  
- User selects cleaning chore to update from list of items in schedule
- System displays food item details: Item name, Item location, Expiration date, Notes
- User selects field to edit
- System increases edit area for user to detail changes and displays an save or discard changes function to user
- User edits field and selects save or discard
- System saves updated information if save is selected, or discards changes if discard is selected
- System provides verification item has been updated or changes have been discarded
- System displays list of items

**Name: View Food Inventory List** 
**Identifier: UC-5** 
**Base Course of Action**  
TBD - placeholder, need to determine in better detail what it means to sort and group Items by date, location, alphabetically etc. 

**Name: View Cleaning Chores** 
**Identifier: UC-6** 
**Base Course of Action**  
TBD - placeholder, need to determine in better detail what it means to sort and group tasks by date, location, alphabetically etc. and determine if I want to add in a priority function

### 1c. Features

**Food Inventory Database (FID)**
- Store new food items in data structure/database
- Select a food item to modify
- Store updated information for food items
- Verify user inputs for new and updated food items
- Set rules for food expiration reminders
- Calculate reminder schedule based off item expiration date and rules for reminders
- Send user reminder for food expirations
- Set and update item status

**Cleaning chores/tasks Database (CD)**
- Store new Cleaning chore/task in data structure/database
- Select a Cleaning chore/task to modify
- Store updated information for Cleaning chores/tasks
- Verify user inputs for new and updated Cleaning chore/task
- Calculate recurring reminders for cleaning chores/tasks
- Send user reminder for cleaning chores/tasks
- Set and update chore/task status


### 1d. Gherkin Validation (Example Test Scenarios)

#### Feature: Store new food items in data structure/database

##### Scenario 1: Valid food item name non-duplicate entry

Given: The user has selected to enter in a food item name 

And the name does not already appear in the inventory

When: User enters a item name with character length is greater than 3 

And character length is less than 50

Then:  Food item name check against inventory list passes

And Food item name is saved into inventory as a new record 

And User is given a visual confirmation that the item is saved

##### Scenario 2:  Valid food item name duplicate entry - initial submission

Given: The user has selected to enter in a food item name

And the name already appear in the active inventory (Non archived/consumed)

When:  User enters a item name with character length is greater than 3 

And character length is less than 50

Then:  Food item name check against inventory list fails

And User is given a choice to add new duplicate item or cancel adding a duplicate food item


##### Scenario 2a: Valid food item name duplicate entry - user decides to cancel new food item

Given: User is trying to add a duplicate food item 

And the user has been prompted with the choice to add new duplicate item or cancel adding a duplicate food item

When: User selects canceling adding the new item

Then: User is given a visual confirmation that adding the food item has been cancelled


##### Scenario 2b: Valid food item name duplicate entry - user decides to add duplicate new food item

Given: User is trying to add a duplicate food item 

And the user has been prompted with the choice to add new duplicate item or cancel adding a duplicate food item

When: User selects to duplicate the food item

Then: Food item name is saved into inventory as a new record 

And User is given a visual confirmation that the item is saved


##### Scenario 3: Invalid food item name - too few characters

Given: The user has selected to enter in a food item name 

And the name does not already appear in the inventory

When: User enters a item name with character length is less than 3 

Then: User is given a visual invalid Food Name warning 


##### Scenario 4: Invalid food item name - too many characters

Given: The user has selected to enter in a food item name 

And the name does not already appear in the inventory

When: User enters a item name with character length is greater than 50

Then: User is given a visual invalid Food Name warning 


------------------------------------------------------------------------------------------------


## Specifications

### 2a. Concept

#### Purpose
Home Food and Chore Management System will provide a basic management system with an easy to use interface 

#### Goal
Release working management system with basic features and build additional features to track and manage additional household duties. Ensure the application usage does not create unreasonable additional work for the user. 

#### Target Users
Adults whom do not have enough money to pay for an assistant to help manage their daily lives. Users whom want to simplify their task tracking 


### 2b. UX Notes

#### System Shall
- Pass user acceptance testing
- Utilize industry standard for readability
    - font size
    - font style
    - text and background contrast
    - text alignment
    - line height
    - consistent letter spacing
- Provide user with a continuous navigation experience 
- Both web and mobile applications keep to same theme and similar navigation 

#### System May
- Provide text to voice
- Allow user to change color scheme to "dark mode"
- Allow user to increase font size

### 2c. Interfaces (Controls)

#### Interfaces

| Interface | Description |
| ----------- | ----------- |
| External Interface to User | Interface will prompt and accept input from user |
| Interface Between Application and System Hosted on | Interface requirements include data input, data output, data storage, date information, CPU, etc. |



### 2d. Behaviors


#### Feature: Store new food items in data structure/database


##### Use Case Diagram

![This is a Use Case Diagram](/Assignment%201/UseCaseDiagramFoodItems.PNG "This is a Use Case Diagram")



##### Activity Diagram


![This is a Activity Diagram](/Assignment%201/ActivityDiagramFoodItems.PNG "This is a Activity Diagram")


------------------------------------------------------------------------------------------------


## Entity Relationship Diagram

![This is a ERD](/Assignment%202/EntityRelationshipDiagram.PNG "This is a ERD")
 

------------------------------------------------------------------------------------------------


## API in Python using FastAPI 
Pydantic models that mirror ERD and initial set of CRUD transactions for User Entity 

```{python}
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
	

# 5.6 additional CRUD operations for the other entities food items, chore items, schedules to be created later




if __name__ == "__main__": # !! This needs to come after all the api def statements
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


```
