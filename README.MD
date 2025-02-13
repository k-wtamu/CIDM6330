# Home Food and Chore Manangement System ~Integrated Smart Home, More than Just Security and Fancy Gadgets~
**Assignment 1 Note:** For this week, I striked through changes from last week and <mark>highlighted new details</mark> to descope the projected from an entire home system to just focusing on one aspect of a household to make this a little more achiveable this semester, at the next submission I will just remove them.

**Student:** Kristen Brunngraber

**Class:**  2025SP SOFTWARE ARCH. (CIDM-6330-70)

**Date:**  12 Febuary 2025

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
~~This prototype would essentially be a very large Systems of Systems Integration effort with APIs and a database that a user can interact easily with. 
If this was not a school project I would need to compare specifications and connection between currently available smart home devices and understand the legal feasibility of collecting and utilizing the needed data from the smart devices. Because my knowledge of current smart home devices is limited, I would need a lot of research into the currently and upcoming smart home appliances/systems. I would also need more about how inventory tracking systems store data, and research ones that are already available. Some [initial research](https://www.nerdwallet.com/article/insurance/home-inventory-app-template) looks like there are home inventory systems that utilize barcode scanning and [additional *“research”*](https://www.reddit.com/r/selfhosted/comments/sm2hih/home_inventory_management_system_ideas/) shows there are “web-based self-hosted groceries & household management solution for your home” through ERP solutions such as [Grocy.](https://grocy.info/) I would also look for tools that utilize images and sensors to identify products like Amazons [“Just Walk Out technology”](https://www.aboutamazon.com/news/retail/amazon-just-walk-out-rfid-technology). I’m pretty sure at the airport recently, there was a small convenience store you placed your items on a large table scanner and scale that determined what item you were trying to buy. As this technology gets cheaper and more reasonable to have in your home there is even more potential.~~


__*To scope this down for this class, I am focusing on the software architecture of a home task and maintenance management system.*__

<mark> This prototype would be a basic home management system to send prescheduled and suggested tasks and inventory reminders to the user to check off as complete or schedule for later. Task and maintenance will be limited in this initial design to food and cleaning type household responsibilities. Eating and cleaning are two of the most basic functions in the household, and this projects protype will start here.</mark>


------------------------------------------------------------------------------------------------


## Contents

1. [Requirements statements](#Requirements-statements)
    1. [User Stories](#User-Stories)
    2. [Use Cases](#Use-Cases)
    3. [Features](#Features)
    4. [Gherkin Validation](#Gherkin-Validation)

2. Specifications
    1. [Concept](#Concept)
    2. [UX Notes](#UX-Notes)
    3. [Interfaces (Controls)](#Interfaces-(Controls))
    4. [Behaviors](#Behaviors)
        1. Feature/Package A (appropriate UML diagrams)
        2. Feature/Package N (appropriate UML diagrams)


------------------------------------------------------------------------------------------------


##  1. Requirements statements


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
- [ ] Food item names will be between three and 50 charecters 
- [ ] Food items can be viewed categorized by location
- [ ] Food items can be viewed in alphebetical order
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
- [ ] Cleaning chores have a location assigned to include bathroom, living room, kitchen, bedroom, gargage, garden, etc. 
- [ ] Repeate cleaning chores can be set as daily, weekly, monthly, or quarterly tasks
- [ ] Repeate cleaning chores should have one or more selected day(s) of the week to be repeated

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
- System pesents user with mandatory blank entry fields for Item Name (Free text), Item location (dropdown), Expiration date (Date field)
- User enters in the Item name
- System verifies the item name field is not blank
- System saves the item name
- User selects the Item location
- System verifies the item location field is not blank
- System saves the item location
- User enters/selects the item expiration date
- System verifies the item exirpation date field is not blank
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
- System displays food item details: Item name, Item location, Epiration date, Notes
- User selects field to edit
- System increases edit area for user to detail changes and displays an save or discard changes function to user
- User edits field and selects save or discard
- System saves updated infromation if save is selected, or discards changes if discard is selected
- System provides verification item has been updated or changes have been discarded
- System displays list of items

**Name:  Enter Cleaning Chore** 
**Identifier: UC-3** 
**Base Course of Action**  
- User selects system function (example selects a button) for entering in a new cleaning chore
- System pesents user with mandatory blank entry fields for Chore Name (Free text), Chore location (dropdown), Chore date (Date field)
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
- System displays food item details: Item name, Item location, Epiration date, Notes
- User selects field to edit
- System increases edit area for user to detail changes and displays an save or discard changes function to user
- User edits field and selects save or discard
- System saves updated infromation if save is selected, or discards changes if discard is selected
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
- Calculate reminder schedule based off item expeiration date and rules for reminders
- Send user reminder for food expirations
- Set and update item status

**Cleaning chores/tasks Database (CD)**
- Store new Cleaning chore/task in data structure/database
- Select a Cleaning chore/task to modify
- Store updated information for Cleaning chores/tasks
- Verify user inputs for new and updated Cleaning chore/task
- Calculate recurring reminders for cleaning chores/tasks
- Send user reminder for cleaning chores/tasks
- Set and upate chore/task status


### 1d. Gherkin Validation (Example Test Scenarios)

**Feature: Store new food items in data structure/database**

Scenario 1:  Valid food item name non-duplicate entry 
Given: The user has selected to enter in a food item name and the name does not already appear in the inventory
When:  User enters a item name with charecter length between 3 and 50
Then:  Food item name is checked against inventoty list && Food item name is saved into inventory as a new record && User is given a visual confirmation that the item is saved

Scenario 1:  Valid food item name duplicate entry 
Given: The user has selected to enter in a food item name
When:  User enters a item name with charecter length between 3 and 50
Then:  Food item name is saved into inventory as a new record, 

Scenario 3: Invalid food item name 
Given: 
When: less than 3 or greater than 50
Then: 




------------------------------------------------------------------------------------------------


##  2. Specifications


### 2a. Concept


### 2b. UX Notes


### 2c. Interfaces (Controls)


### 2d. Behaviors


#### Feature/Package A (appropriate UML diagrams)


#### Feature/Package N (appropriate UML diagrams)

 Diagrams should be rendered as images that appear within the README document.

