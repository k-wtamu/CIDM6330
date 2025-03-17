#1 Create empty file User.csv
# Reference AI Overview:  "abstract repository for multiple entities python with fastapi": https://www.google.com/search?sca_esv=fe77601a3581b981&sxsrf=AHTn8zr6rlzrniM3FYxe74_abOv8R9eiew:1742163411425&q=abstract+repository+for+multiple+entities+python+with+fastapi&spell=1&sa=X&ved=2ahUKEwiohZ260I-MAxUeElkFHd7ZCdQQBSgAegQIGBAB&biw=982&bih=1599&dpr=1.1 
# Insure you have a virtual environment (python -m venv .venv) and, if you do, activate it:
# Windows with Git-Bash: . ./.venv/Scripts/activate

# python -m venv .venv
# pip install sqlmodel

# 2: imports
from abc import ABC, abstractmethod
from sqlmodel import SQLModel, create_engine, Session, Field, select
from dataclasses import dataclass, asdict, field, InitVar
from fastapi import FastAPI, HTTPException 
from typing import Optional
import datetime
import csv

# 3 Define the model (starting w/ only User table)

@dataclass
class Users(SQLModel, table=True):
	userID: int = Field(default=None, primary_key=True)
	username: str
	useryearborn: int					# Todo: will need to later limit the years between XXXX & YYYY too complicated if we just want year datetime.date.year				
	usericon: str 						# Note: may want to update to another way to store image/icon data
	useremail: str	# !!! Need to look into how you can use lists here.... for now using str instead of list[str] 
	userphonenumber: str	# !!! Need to look into how you can use lists here.... for now using str instead of list[str] 

"""	Will try to add in later. need to also make csv/sql/memory and fast API edits with these too if impelmenting for wole project
class FoodItem(SQLModel, table=True):
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

class ChoreItem(SQLModel, table=True):
	choreitemUID: int
	choreitemname: str
	choreitemduration: list[int | str] # Note: needs number and interval
	choreitempriority: int
	choreitemlocation: list[str]			 # Review: needs ability to store household and room if needed, so maybe seaperate these
	choreitemnotes:	str

class ChoreSchedule(SQLModel, table=True):
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
	
"""	
	
		
# 3 Repository Interface

class ManagementSystemRepository(ABC):
    @abstractmethod

# Create
    @abstractmethod
    def do_create(self, user: Users):
        pass
# Read
    @abstractmethod
    def read_all(self):
        pass
# Read
    @abstractmethod
    def do_read(self, userID):
        pass
# Update
    @abstractmethod
    def do_update(self, userID: int, field: str, value):
        pass
# Delete
    @abstractmethod
    def do_delete(self, userID):
        pass


# 5 CSV implementation

class ManagementSystemRepositoryCSVRepo(ManagementSystemRepository):

    def __init__(self, filename: str, id_field: int, fieldnames: list):

        self.repo = list[Users] # this is a typehint for a list of Users Table objects
        self.filename = filename
        self.fieldnames = fieldnames

        with open(filename, mode="r", newline="") as file:
            csv_reader = csv.DictReader(file)
            self.repo = [Users(**row) for row in csv_reader]

    def do_create(self, user: Users):
        self.repo.append(user)
        self.do_save_file()

    def read_all(self):
        return self.repo

    def do_read(self, userID):
        for user in self.repo:
            if int(user.userID) == int(userID):
                return user

    def do_update(self, userID: int, field: str, value):
        if field == "username":
            for index, user in enumerate(self.repo):
                if int(user.userID) == int(userID):
                    self.repo[index].username = value
                    self.do_save_file()
                    return self.repo[index]
 
        if field == "useryearborn":
            for index, user in enumerate(self.repo):
                if int(user.userID) == int(userID):
                    self.repo[index].useryearborn = value
                    self.do_save_file()
                    return self.repo[index]

        if field == "usericon":
            for index, user in enumerate(self.repo):
                if int(user.userID) == int(userID):
                    self.repo[index].usericon = value
                    self.do_save_file()
                    return self.repo[index]

        if field == "useremail":
            for index, user in enumerate(self.repo):
                if int(user.userID) == int(userID):
                    self.repo[index].useremail = value
                    self.do_save_file()
                    return self.repo[index]
            
        if field == "userphonenumber":
            for index, user in enumerate(self.repo):
                if int(user.userID) == int(userID):
                    self.repo[index].userphonenumber = value
                    self.do_save_file()
                    return self.repo[index]
			

    def do_delete(self, userID):
        for user in self.repo:
            if int(user.userID) == int(userID):
                self.repo.remove(user)
                break

        self.do_save_file()

    def do_save_file(self):
        with open(self.filename, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            for user in self.repo:
                writer.writerow(asdict(user))

"""

# 6 SQLModel implementation

class SQLModelRepository(ManagementSystemRepository):
    def __init__(self, db_string="sqlite:///todo.db"):
        self.engine = create_engine(db_string)
        SQLModel.metadata.create_all(self.engine)
        self.session = Session(self.engine)
# Create
    def do_create(self, item: Users):
        self.session.add(item)
        self.session.commit()		
# Read
    def get(self, name: str) -> Users | None:
        statement = select(Users).where(Users.name == name)
        return self.session.exec(statement).first()		
# Update

# Delete

# 7 Memory implementation

class ManagementSystemRepositoryMemoryRepo(ManagementSystemRepository):

    def __init__(self, id_field: str):

        self.repo = list[Users]

    def do_create(self, user: Users):
        self.repo.append(user)

    def read_all(self):
        return self.repo

    def do_read(self, userID):
        return self.repo[userID]

    def do_update(self, userID, user: Users):
        self.repo[userID] = user

    def do_delete(self, userID):
        for user in self.repo:
            if int(user.userID) == int(userID):
                self.repo.remove(user)
                break
        
"""

# 8 Initalize with dummy data
def do_csv():
    print("Loading Inital Data Set for CSV")
    # CSV Dummy Data
    global user_repo 
    user_repo = ManagementSystemRepositoryCSVRepo("User.csv", "id", ["userID", "username", "useryearborn", "usericon", "useremail",  "userphonenumber"]) # create one for each Class (Data table)
    user_repo.do_create(Users(userID=123456, username="Hal" ,  useryearborn=2001, usericon="red circle", useremail="discovery1@gmail.com", userphonenumber="281-111-1111"))	# ["discovery1@gmail.com"],["281-111-1111"] change back if I find out how to use a list
    user_repo.do_create(Users(userID=1234567, username="DRain" ,  useryearborn=1968, usericon="square", useremail="discovery2@gmail.com", userphonenumber="281-222-2222"))
    user_repo.do_create(Users(userID=12345678, username="Joshua" ,  useryearborn=1983, usericon="star", useremail="falken@gmail.com", userphonenumber="281-333-3333"))
    print(user_repo.read_all())

def do_sql():
    print("Loading Inital Data Set for SQL")

def do_memory():
    print("Loading Inital Data Set for Memory")


# 9  FAST API  create path operation(s) the decorator indicating path and type of operation for each crud 

app = FastAPI() # make app
# Note web only uses get, use the fastapi http://127.0.0.1:8000/docs

# Routes for Users
	# Create
@app.post("/api/createnewuser/{userID}")
def new_user(userID: int, newuser: Users):
	user_repo.do_create(newuser)
	return user_repo.do_create(newuser.userID)
	# Read
@app.get("/api/getuser/{userID}")
def read_user(userID: int):
    return {"userID": userID, "user": user_repo.do_read(userID)}
	# Update
@app.put("/api/updateuser/{userID}")
def update_user(userID: int, field: str, value):
    user_repo.do_update(userID, field, value)
    return user_repo.do_update(userID, field, value)
	# Delete

@app.delete("/api/deleteuser/{userID}")
def delete_user(userID: int): 
		user_repo.do_delete(userID)


# Testing 
""" Create
Test Request Body
{
  "userID": 9999,
  "username": "Turtle",
  "useryearborn": 2025,
  "usericon": "heart",
  "useremail": "Turtle@gmail.com",
  "userphonenumber": ""
}
"""
	
""" Read
Test 1: get request with userID from test request above 
http://127.0.0.1:8000/api/getuser/9999
Test 2:	test ID 1234567
http://127.0.0.1:8000/api/getuser/1234567
"""

""" Update
Test Request Body into updateuser

	"userID" = 9999,
	field = "username"
	Value =  "Chicken"


check again, and see if its updated
http://127.0.0.1:8000/api/getuser/9999

"""

if __name__ == "__main__":
    do_csv() # comment out when testing other types
#	do_sql() # comment out when testing other types
#	do_memory() # comment out when testing other types
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
	
