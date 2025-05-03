# Home Food and Chore Management System  

**Student:** Kristen Brunngraber

**Class:**  2025SP SOFTWARE ARCH. (CIDM-6330-70)

**Date:**  11 May 2025

------------------------------------------------------------------------------------------------

## Contents

1. [Introduction / Evolution 0: Domain Specification and UML Modeling](#Introduction)  
	1. [Requirements statements](#Requirements-Statements)
		* [User Stories](#User-Stories)
		* [Use Cases](#Use-Cases)
		* [Features](#Features)
		* [Gherkin Validation](#Gherkin-Validation)

	2. [Specifications](#Specifications)
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

	1. [Entity Relationship Diagram](#Entity-Relationship-Diagram) 
	2. [Additional Use Case Diagrams](#Service-Level-Use-Case-Sequence-Diagrams)
 
4. [Evolution 2: An updated API](#Updated-API)

	1. You may use the Django REST Framwork or Django Ninja

	2. [Updated ERD](#Updated-ERD) 

	3. [Update CRUD Transactions](#Update-CRUD-Transactions)

5. [Evolution 3: Skipping](#Evolution-3)

6. [Evolution 4: Migrate to Django](#Migrate-to-Django)

Ensure the proper models, views, and urls are in place
Migrate from FastAPI to Django Rest Framework (DRF) or Django Ninja

7. [Evolution 5: Full Django + Tests](#Full-Django-and-Tests)

For DDD create a ubiquitous language glossary: https://thedomaindrivendesign.io/developing-the-ubiquitous-language/)
For BDD create A Gherkin Notation expression for each test: https://cucumber.io/docs/gherkin/)
For TDD create tests that correspond with your Gherkin Statements.
With these you will create Django unittests that demonstrates three Use Cases of your system.  



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

**Name: View Food Inventory List** 
**Identifier: UC-5** 
**Base Course of Action**  
TBD - placeholder, need to determine in better detail what it means to sort and group Items by date, location, alphabetically etc. 

**Name: View Cleaning Chores** 
**Identifier: UC-6** 
**Base Course of Action**  
TBD - placeholder, need to determine in better detail what it means to sort and group tasks by date, location, alphabetically etc. and determine if I want to add in a priority function

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

![This is a Class Diagram]

##### Component Diagram

![This is a Component Diagram]

##### State Machine Diagram

![This is a State Machine Diagram]

------------------------------------------------------------------------------------------------

## Requirements Specification

### Entity Relationship Diagram

![This is a ERD](/Assignment%202/EntityRelationshipDiagram.PNG "This is a ERD")
 
### Service Level Use Case Sequence Diagrams

#### Feature: Food Inventory Database (FID)

![This is a Sequence Diagram](/Final%20Project/Diagrams/Food_Items_ServiceLevelSequenceDiagrams.PNG "This is a Sequence Diagram")

#### Feature: Cleaning chores/tasks Database (CD)

![This is a Sequence Diagram](/Final%20Project/Diagrams/Chores_ServiceLevelSequenceDiagrams.PNG "This is a Sequence Diagram")

------------------------------------------------------------------------------------------------

## Updated API

### API in Python using Django REST Framwork or Django Ninja
 

```{python}



```

### Updated ERD


### Update CRUD Transactions


------------------------------------------------------------------------------------------------

## Evolution 3 

Note: This Evolution became irrelevant once we went to a monolith like Djanog with its O/RM - all repository variations are dropped as the O/RM works differently

------------------------------------------------------------------------------------------------

## Migrate to Django







------------------------------------------------------------------------------------------------

## Full Django and Tests






