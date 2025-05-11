# Home Food and Chore Management System  

**Student:** Kristen Brunngraber

**Class:**  2025SP SOFTWARE ARCH. (CIDM-6330-70)

**Date:**  11 May 2025

------------------------------------------------------------------------------------------------

## Contents

1. [Introduction / Evolution 0: Domain Specification and UML Modeling](#Introduction)  
	* [Requirements statements](#Requirements-Statements)
		* [User Stories](#User-Stories)
		* [Use Cases](#Use-Cases)
		* [Features](#Features)
		* [Gherkin Validation](#Gherkin-Validation)

	* [Specifications](#Specifications)
		* [Concept](#Concept)  
		* [UX Notes](#UX-Notes)
		* [Interfaces](#Interfaces) 
		* [Behaviors / Design Diagrams](#Design-Diagrams)
			- [Use Case Diagram](#Use-Case-Diagram)
			- [Activity Diagram](#Activity-Diagram)
			- [Sequence Diagram](#System-Level-Sequence-Diagram)
			- [Class Diagram](#Class-Diagram)
			- [Component Diagram](#Component-Diagram)
			- [State Machine Diagram](#State-Machine-Diagram)

3. [Evolution 1: An updated Requirements Specification](#Requirements-Specification)
	*  [Entity Relationship Diagram](#Entity-Relationship-Diagram) 
	*  [Additional Use Case Diagrams](#Service-Level-Use-Case-Sequence-Diagrams)
	*  [Updated Class Diagram](#Updated-Class-Diagram)
 
4. [Evolution 2: An updated API](#Updated-API)
	*  [Django Ninja API](#Django-Ninja-API)
	*  [Updated ERD](#Updated-ERD) 
	*  [Update CRUD Transactions](#Update-CRUD-Transactions)

5. [Evolution 3: Skipping](#Evolution-3)

6. [Evolution 4: Migrate to Django](#Migrate-to-Django)
	*  [Django Data Models](#Data-Models)
	*  [Django Views](#Views) 
	*  [Django Urls](#URLs)
	*  [Django APIs](#APIs)
	*  [Django Schemas](#Schemas)
	*  [Django Beyond CRUD](#Beyond-CRUD-Attempt)

7. [Evolution 5: Full Django + Tests](#Full-Django-and-Tests)
	* [DDD Ubiquitous Language Glossary](#DDD-Ubiquitous-Language-Glossary)
	* [BDD Gherkin Notation Expressions](#BDD-Gherkin-Notation-Expressions)
	* [TDD Corresponding Tests](#TDD-Corresponding-Tests)

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


###  Requirements Statements


#### User Stories

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



#### Use Cases

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

#### Features

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


#### Gherkin Validation

(Example Test Scenarios)

##### Feature: Store new food items in data structure/database

###### Scenario 1: Valid food item name non-duplicate entry

Given: The user has selected to enter in a food item name 

And the name does not already appear in the inventory

When: User enters a item name with character length is greater than 3 

And character length is less than 50

Then:  Food item name check against inventory list passes

And Food item name is saved into inventory as a new record 

And User is given a visual confirmation that the item is saved

###### Scenario 2:  Valid food item name duplicate entry - initial submission

Given: The user has selected to enter in a food item name

And the name already appear in the active inventory (Non archived/consumed)

When:  User enters a item name with character length is greater than 3 

And character length is less than 50

Then:  Food item name check against inventory list fails

And User is given a choice to add new duplicate item or cancel adding a duplicate food item


###### Scenario 2a: Valid food item name duplicate entry - user decides to cancel new food item

Given: User is trying to add a duplicate food item 

And the user has been prompted with the choice to add new duplicate item or cancel adding a duplicate food item

When: User selects canceling adding the new item

Then: User is given a visual confirmation that adding the food item has been cancelled


######  Scenario 2b: Valid food item name duplicate entry - user decides to add duplicate new food item

Given: User is trying to add a duplicate food item 

And the user has been prompted with the choice to add new duplicate item or cancel adding a duplicate food item

When: User selects to duplicate the food item

Then: Food item name is saved into inventory as a new record 

And User is given a visual confirmation that the item is saved


######  Scenario 3: Invalid food item name - too few characters

Given: The user has selected to enter in a food item name 

And the name does not already appear in the inventory

When: User enters a item name with character length is less than 3 

Then: User is given a visual invalid Food Name warning 


######  Scenario 4: Invalid food item name - too many characters

Given: The user has selected to enter in a food item name 

And the name does not already appear in the inventory

When: User enters a item name with character length is greater than 50

Then: User is given a visual invalid Food Name warning 


------------------------------------------------------------------------------------------------


## Specifications

### Concept

#### Purpose
Home Food and Chore Management System will provide a basic management system with an easy to use interface.

#### Goal
Release working management system with basic features and build additional features to track and manage additional household duties. Ensure the application usage does not create unreasonable additional work for the user. 

#### Target Users
Adults whom do not have enough money to pay for an assistant to help manage their daily lives. Users whom want to simplify their task tracking. 


### UX Notes

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

### Interfaces (Controls)

#### Interfaces

| Interface | Description |
| ----------- | ----------- |
| External Interface to User | Interface will prompt and accept input from user |
| Interface Between Application and System Hosted on | Interface requirements include data input, data output, data storage, date information, CPU, etc. |


### Design Diagrams

#### Use Case Diagram

#####  Feature: Store new food items in data structure/database

![This is a Use Case Diagram](/Assignment%201/UseCaseDiagramFoodItems.PNG "This is a Use Case Diagram")

##### Activity Diagram

![This is a Activity Diagram](/Assignment%201/ActivityDiagramFoodItems.PNG "This is a Activity Diagram")

##### System Level Sequence Diagram

![This is a Sequence Diagram](/Final%20Project/Diagrams/SystemLevelSequenceDiagrams.PNG "This is a Sequence Diagram")

##### Class Diagram

![This is a Class Diagram](/Final%20Project/Diagrams/ClassDiagram.PNG "This is a Class Diagram")

##### Component Diagram

![This is a Component Diagram](/Final%20Project/Diagrams/ComponentDiagram.PNG "This is a Component Diagram")

##### State Machine Diagram

![This is a State Machine Diagram](/Final%20Project/Diagrams/StateMachineDiagram.PNG "This is a State Machine Diagram")

------------------------------------------------------------------------------------------------

## Requirements Specification

### Entity Relationship Diagram

![This is a ERD](/Assignment%202/EntityRelationshipDiagram.PNG "This is a ERD")
 
### Service Level Use Case Sequence Diagrams

#### Feature: Food Inventory Database (FID)

![This is a Sequence Diagram](/Final%20Project/Diagrams/Food_Items_ServiceLevelSequenceDiagrams.PNG "This is a Sequence Diagram")

#### Feature: Cleaning chores/tasks Database (CD)

![This is a Sequence Diagram](/Final%20Project/Diagrams/Chores_ServiceLevelSequenceDiagrams.PNG "This is a Sequence Diagram")

### Updated Class Diagram

![This is a Class Diagram](/Final%20Project/Diagrams/UpdatedClassDiagram.PNG "This is a Class Diagram")

------------------------------------------------------------------------------------------------

## Updated API

### Django Ninja API

See api.py in the my project folder for full code

```{python}

api = NinjaAPI()

# This is an input schema for the FoodItem Table

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


class FoodItemIn(Schema):
	fooditemstatus: str  
	fooditemquantity: int 
	fooditemname: str
	fooditemfavorite: bool = None
	fooditemspecialtystore: str = None
	fooditemshoppinglist: str = None 			 
	fooditemexpirationreminder:  str = None
	fooditemexpirationdate: datetime.date 		 
	fooditemnotes: str = None
	fooditemstoragelocation: str = None

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
	fooditemexpirationdate: datetime.date 		 
	fooditemnotes: str = None
	fooditemstoragelocation: str = None

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


# This is an input schema for the ChoreSchedule Table
class ChoreScheduleIn(Schema):
	choretocomplete: int # !!FK for the chore you are scheduling!!
	duedate: datetime.date 
	actualcompletiondate: datetime.date
	notification:  str
	choreitemstatus: str
	repeateevery:  str
	repeaton: str 								 
	endon: datetime.date = None						
	endafer: int = None								
	assignment:  str	

# this is to delete/replace
class ChoreScheduleOut(Schema):
	chorescheduleUID: int   # unique to out, generated
	choretocomplete: int # !!FK for the chore you are scheduling!!
	duedate: datetime.date 
	actualcompletiondate: datetime.date
	notification:  str
	choreitemstatus: str
	repeateevery:  str
	repeaton: str 								 
	endon: datetime.date = None						
	endafer: int = None								
	assignment:  str	

```

### Updated ERD

![This is a ERD](/Final%20Project/Diagrams/UpdatedERD.PNG "This is a ERD") 

### Update CRUD Transactions

See api.py in the my project folder for full code or Views section in Migrate to Django for full CRUD defitions in python

| Create | Read | Update | Delete |
| ----------- | ----------- | ----------- | ----------- |
| @api.post("/user") def create_user(request, user: UsersIn) | @api.get("/user/{userID}", response=UsersOut) def get_user(request, userID: int) | @api.put("/user/{userID}") def update_user(request, userID: int, payload: UsersIn) | @api.delete("/user/{userID}") def delete_user(request, userID: int) |
| @api.post("/fooditem") def create_fooditem(request, fooditem: FoodItemIn) | @api.get("/fooditem/{fooditemUID}", response=FoodItemOut) def get_fooditem(request, fooditemUID: int) | @api.put("/fooditem/{fooditemUID}") def update_fooditem(request, fooditemUID: int, payload: FoodItemIn) | @api.delete("/fooditem/{fooditemUID}") def delete_fooditem(request, fooditemUID: int) |
| @api.post("/choreitem") def create_choreitem(request, choreitem: ChoreItemIn)| @api.get("/choreitem/{choreitemUID}", response=ChoreItemOut) def get_choreitem(request, choreitemUID: int) | @api.put("/choreitem/{choreitemUID}") def update_choreitem(request, choreitemUID: int, payload: ChoreItemIn) | @api.delete("/choreitem/{choreitemUID}") def delete_choreitem(request, choreitemUID: int)|
| @api.post("/choreschedule") def create_choreschedule(request, choreschedule: ChoreScheduleIn) | @api.get("/choreschedule/{chorescheduleUID}", response=ChoreScheduleOut) def get_choreschedule(request, chorescheduleUID: int) | @api.put("/choreschedule/{chorescheduleUID}") def update_choreschedule(request, chorescheduleUID: int, payload: ChoreScheduleIn) | @api.delete("/choreschedule/{chorescheduleUID}") def delete_choreschedule(request, chorescheduleUID: int) |

------------------------------------------------------------------------------------------------

## Evolution 3 

Note: This Evolution became irrelevant once we went to a monolith like Djanog with its O/RM - all repository variations are dropped as the O/RM works differently

------------------------------------------------------------------------------------------------

## Migrate to Django

### Data Models

See Models.py

```{python}
from django.db import models

class User(models.Model):
	userID = models.AutoField
	username = models.CharField(max_length=100)
	birthdate = models.DateField(null=True, blank=True)
	usericon = models.CharField(max_length=100)
	useremail = models.CharField(max_length=100)
	userphonenumber = models.IntegerField

class FoodItem(models.Model):
	fooditemUID =  models.AutoField
	fooditemstatus = models.CharField(max_length=100)  
	fooditemquantity = models.IntegerField 
	fooditemname = models.CharField(max_length=100)
	fooditemfavorite = models.BooleanField(default=False)
	fooditemspecialtystore = models.CharField(max_length=100)
	fooditemshoppinglist = models.CharField(max_length=100) 			 
	fooditemexpirationreminder =  models.CharField(max_length=100)
	fooditemdaysuntilexpiration = models.IntegerField
	fooditemexpirationdate = models.DateField(null=True, blank=True)		 
	fooditemnotes = models.CharField(max_length=1000)
	fooditemstoragelocation = models.CharField(max_length=100)	
	
class ChoreItem(models.Model):
	choreitemUID = models.AutoField
	choreitemname = models.CharField(max_length=100)
	choreitemduration = models.CharField(max_length=100)
	choreitempriority = models.IntegerField 
	choreitemlocation = models.CharField(max_length=100)
	choreitemnotes = models.CharField(max_length=1000)
	
class ChoreSchedule(models.Model):
	chorescheduleUID = models.AutoField
	choretocomplete = models.ForeignKey(ChoreItem, on_delete=models.CASCADE)  #FK for the chore you are scheduling 
	duedate = models.DateField(null=True, blank=True)
	actualcompletiondate = models.DateField(null=True, blank=True)
	notification =  models.CharField(max_length=100)
	choreitemstatus = models.CharField(max_length=100)
	repeateevery =  models.CharField(max_length=100)
	repeaton = models.CharField(max_length=100)								 
	endon = models.DateField(null=True, blank=True)						
	endafer = models.IntegerField 							
	assignment =  models.CharField(max_length=100)

```

### Views 

See api.py in the my project folder for full code

```{python}
@api.post("/user")
def create_user(request, user: UsersIn):
    user_info = user.dict()
    user = User(**user_info)
    user = User.objects.create(user)    

    return user

@api.get("/user/{userID}", response=UsersOut)
def get_user(request, userID: int):
    user = get_object_or_404(User, id=userID)
    return user

@api.get("/user", response=list[UsersOut])
def list_user(request):
    user = User.objects.all()
    return user

@api.put("/user/{userID}")
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

@api.delete("/user/{userID}")
def delete_user(request, userID: int):
    user = get_object_or_404(User, id=userID)
    user.delete()
    return {"success": True, "user": user}

@api.post("/fooditem")
def create_fooditem(request, fooditem: FoodItemIn):
    fooditem_info = fooditem.dict()
    fooditem = FoodItem(**fooditem_info)
    fooditem = FoodItem.objects.create(fooditem)    
    return fooditem

@api.get("/fooditem/{fooditemUID}", response=FoodItemOut)
def get_fooditem(request, fooditemUID: int):
    fooditem = get_object_or_404(FoodItem, id=fooditemUID)
    return fooditem

@api.get("/fooditem", response=list[FoodItemOut])
def list_fooditem(request):
    fooditem = FoodItem.objects.all()
    return fooditem

@api.put("/fooditem/{fooditemUID}")
def update_fooditem(request, fooditemUID: int, payload: FoodItemIn):
    fooditem = get_object_or_404(FoodItem, id=fooditemUID)
    for attr, value in payload.dict().items():
        setattr(fooditem, attr, value)
    fooditem.save()
    return {"success": True, "fooditem": fooditem}
	
@api.delete("/fooditem/{fooditemUID}")
def delete_fooditem(request, fooditemUID: int):
    fooditem = get_object_or_404(FoodItem, id=fooditemUID)
    fooditem.delete()
    return {"success": True, "fooditem": fooditem}

@api.post("/choreitem")
def create_choreitem(request, choreitem: ChoreItemIn):
    choreitem_info = choreitem.dict()
    choreitem = ChoreItem(**choreitem_info)
    choreitem = ChoreItem.objects.create(choreitem)    

    return choreitem

@api.get("/choreitem/{choreitemUID}", response=ChoreItemOut)
def get_choreitem(request, choreitemUID: int):
    choreitem = get_object_or_404(ChoreItem, id=choreitemUID)
    return choreitem

@api.get("/choreitem", response=list[ChoreItemOut])
def list_choreitem(request):
    choreitem = ChoreItem.objects.all()
    return choreitem

@api.put("/choreitem/{choreitemUID}")
def update_choreitem(request, choreitemUID: int, payload: ChoreItemIn):
    choreitem = get_object_or_404(ChoreItem, id=choreitemUID)
    for attr, value in payload.dict().items():
        setattr(choreitem, attr, value)
    choreitem.save()
    return {"success": True, "choreitem": choreitem}

@api.delete("/choreitem/{choreitemUID}")
def delete_choreitem(request, choreitemUID: int):
    choreitem = get_object_or_404(ChoreItem, id=choreitemUID)
    choreitem.delete()
    return {"success": True, "choreitem": choreitem}

@api.post("/choreschedule")
def create_choreschedule(request, choreschedule: ChoreScheduleIn):
    choreschedule_info = choreschedule.dict()
    choreschedule = ChoreSchedule(**choreschedule_info)
    choreschedule = ChoreSchedule.objects.create(choreschedule)    
    return choreschedule

@api.get("/choreschedule/{chorescheduleUID}", response=ChoreScheduleOut)
def get_choreschedule(request, chorescheduleUID: int):
    choreschedule = get_object_or_404(ChoreSchedule, id=chorescheduleUID)
    return choreschedule

@api.get("/choreschedule", response=list[ChoreScheduleOut])
def list_choreschedule(request):
    choreschedule = ChoreSchedule.objects.all()
    return choreschedule

@api.put("/choreschedule/{chorescheduleUID}")
def update_choreschedule(request, chorescheduleUID: int, payload: ChoreScheduleIn):
    choreschedule = get_object_or_404(ChoreSchedule, id=chorescheduleUID)
    for attr, value in payload.dict().items():
        setattr(choreschedule, attr, value)
    choreschedule.save()
    return {"success": True, "choreschedule": choreschedule}

@api.delete("/choreschedule/{chorescheduleUID}")
def delete_choreschedule(request, chorescheduleUID: int):
    choreschedule = get_object_or_404(ChoreSchedule, id=chorescheduleUID)
    choreschedule.delete()
    return {"success": True, "choreschedule": choreschedule}

```

### URLs

*  /user
* /fooditem
* /fooditem/{fooditemUID}
* /choreitem
* /choreitem/{choreitemUID}
* /choreschedule
* /choreschedule/{chorescheduleUID}


### APIs

![This is a image of API Options](/Final%20Project/Diagrams/Assignment4_API.PNG "This is a image of API Options")

### Schemas

![This is a image of the Schemas](/Final%20Project/Diagrams/Assignment4_API_Schemas.PNG "This is a image of the Schemas")

### Beyond CRUD Attempt

![This is a image of the Beyond CRUD Attempt](/Final%20Project/Diagrams/beyondCRUD.PNG "This is a image of Beyond CRUD Attempt")

```
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
```

------------------------------------------------------------------------------------------------

## Full Django and Tests

### DDD Ubiquitous Language Glossary

| Term | Definition | Example |
| ----------- | ----------- | ----------- |
| Date   | The day of the month or year as specified by a number, organized by year, month, day.    |  2025, 5, 10.   |
| User | A person who uses the home and chore management application. | Kai, Amelia, Mia, Liam, Olivia, Rowan, Noah, James.  |
| Icon   |  A picture or symbol that appears on a screen and is used to represent a user account.  |  Star, Flower, Animal.   |
| Email   | An address at which a person can receive email messages.  |  name@domain.com  |
| Phone number   | A set of figures identifying the telephone of a particular subscriber, and used in making connections to that telephone.  |  10 integers (between 0 and 9).  |
| Status   |  Gives information about the food or chore item.  |  For food items: consumed, disposed of, or in stock. For chore items: scheduled, late, or completed.  |
| Location   |  A place within the house the food is stored or where the chore has to be completed.   | For food items: Refrigerator, Freezer, Pantry. For chore items: Master Bedroom, Kids Bedroom, Spare Bedroom, Living Room, Movie Room, Office, Kitchen, Garage, etc.  |
| Priority   | Ranking.   | Used for chore items for users to categorize by ranking which chores are most or least important.   |
| Item   |   Can be used to describe a food item or a chore item.   | For food items: banana, etc. or a For chore items: laundry, sweep, mop, vacuum, homework, dishes etc.  |
| Schedule   |  A table that tracks time, notification, and status details of chore items. Tracks planned (due) and actual completion dates.  |  Recurring: Daily, weekly, monthly, or quarterly tasks , or on a specific date.  |
| Favorite  |  Item regarded with special favor or preference.   | Bool field, a food item can be marked as a favorite if fooditemfavorite = True.   |
| Reminder  | Notification to user by email.   |   Reminder to wash the car by 2025, 5, 10. |
| Expiration date    |  The last date that a product, as food, should be used before it is considered spoiled or ineffective, usually specified on the label or package.   | Organized by year, month, day: 2025, 5, 10.   |
| Notes | Short descriptive or summarized details on a chore or food item.  |  For food items: Mafaldine Pasta - Long, flat ribbons with ruffled edges, perfect for holding sauce. Goes great with ground meat. or a For chore items:  eminder to vacuum stairs with special attachment. |
|   UID  |  Unique Identifier (UID) is a string, either numeric or alphanumeric, that uniquely identifies an entity within a system.   |  This is a AutoField within this system.  |
| Credentials  |  Information that identifies an account and keeps it secure.  |  Username or useremail are used as credentials, used to ensure the system knows whos information to search and display.  |

### BDD Gherkin Notation Expressions

####  As a user of the basic home management system I would like to recieve a welcome email

```
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
```

#### As a user of the basic home management system I would like at the begining of the month to get a list of all current food items stored in the system

```
@shared_task
def send_monthly_food_avail(FoodItem, userID, fooditemstatus == "In Stock"):
    print(f"Sending monthly list of available food items: {datetime.now()}")
# logic for filtering list
	availfoodlist = [item for item in FoodItem if eval(FoodItem.objects.filter(FoodItem.fooditemstatus == "In Stock"))]
# logic for email sending
        try:
            user = User.objects.get(pk=userID)
            send_mail(
                'Monthly list of available food items!',
                f'Hi {user.username}, here is your monthly list of available food items!',
                'noreply@example.com',
                [user.email],
                fail_silently=False, 
				availfoodlist,
            )
            return f"Monthly available food item list email sent to user {user.username}"
        except User.DoesNotExist:
             return f"User with id {userID} not found."
        except requests.exceptions.RequestException as e:
# logic for schedule			
app.conf.beat_schedule = {
    'send-monthly-reminder': {
        'task': 'send_monthly_reminder',
        'schedule': crontab(day_of_month='1'), # Runs on the 1st of every month
    },
}
```


### TDD Corresponding Tests




