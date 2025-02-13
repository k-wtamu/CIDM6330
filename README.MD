# Home Food Manangement System ~Integrated Smart Home, More than Just Security and Fancy Gadgets~
** Assignment 1 Note:** For this week, I striked through changes from last week and <mark>highlighted new details</mark> to descope the projected from an entire home system to just focusing on one aspect of a household to make this a little more achiveable this semester, at the next submission I will just remove them.

**Student:** Kristen Brunngraber

**Class:**  2025SP SOFTWARE ARCH. (CIDM-6330-70)

Front Page !!!!!!!!!!!


------------------------------------------------------------------------------------------------


Introduction 

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


# Contents

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


###  1. Requirements statements


#### User Stories

1) As a user of the basic home management system I would like to have reminders for when food is expiring 
Confirmations/Acceptance Criteria: 
- [ ] Items with a best buy date will have the date stored as the expiration date
- [ ] Food locations are defined as either Pantry, Refrigerator, or Freezer
- [ ] A reminder will be sent one week before expiration for items in the Pantry or Freezer
- [ ] A reminder will be sent two days before for items in the refrigerator
- [ ] All foods will have a designated expiration date

2) As a user of the home food management system I would like to view all current food items stored in the system
Confirmations/Acceptance Criteria: 
- [ ] Food items can be viewed categorized by location
- [ ] Food items can be viewed in alphebetical order
- [ ] Food items can be viewed in order of expiration date; sorted by both nearest and farthest expiration in relation to the current date 
- [ ] Expiration date is defined by Day, Month, Year 


3) As a user of the basic home management system I would like to have reminders for daily, monthly, and quarterly cleaning chores 
Confirmations/Acceptance Criteria: 
- [ ] Cleaning chores can be categorized as daily, monthly, or quarterly tasks
- [ ] Cleaning chores should be 

4) As a user of the home food management system I would like to set a new reminder after being given a reminder for daily, monthly, and quarterly cleaning
Confirmations/Acceptance Criteria: 
- [ ]



#### Use Cases

1) Enter new Food Item
Name
Identifier:
Base Course of Action 
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
- System provides verification item has been saved to inventory

2) 
Name
Identifier:
Base Course of Action 

3) 
Name
Identifier:
Base Course of Action 



#### Features


#### Gherkin Validation


------------------------------------------------------------------------------------------------


###  2. Specifications


#### Concept


#### UX Notes


#### Interfaces (Controls)


#### Behaviors


##### Feature/Package A (appropriate UML diagrams)


##### Feature/Package N (appropriate UML diagrams)

 Diagrams should be rendered as images that appear within the README document.

