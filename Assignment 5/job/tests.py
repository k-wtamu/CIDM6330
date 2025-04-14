

# Create your tests here in this file below the tests


from django.test import TestCase
from django.urls import reverse_lazy
from ninja.testing import TestClient
from django.test import Client

from .api import router as list_router

# built-in Django Test Client
class ViewTest(TestCase):
    def setUp(self):
        # This method is called before each test
        # arrange
        self.client = Client()

    def test_index(self):
        # act
        path = reverse_lazy("job:index")
        response = self.client.get(path)
        # assert
        assert response.status_code == 200, "API is not reachable"
        assert response.json() == {
            "message": "Welcome to the Integrated Smart Home API"
        }, "Unexpected response message"

    def test_xyz(self):
        # act
        response = self.client.get("/api/cities/v1/")
        # assert
        assert response.status_code == 200, "API is not reachable"
        assert response.json() == {
            "message": "Welcome to the Integrated Smart Home API"
        }, "Unexpected response message"

    def test_hello(self):
        # act
        response = self.client.get("/api/v1/hello/")
        # assert
        assert response.status_code == 200, "API is not reachable"
        assert response.json() == {
            "message": "Hello, World!"
        }, "Unexpected response message"

# Test Cases
# built-in DjangoNinja Test Client
class BasicTest(TestCase):

    def setUp(self):
        # This method is called before each test
        # arrange
        self.client = TestClient(list_router)

    def test_basic(self):

        # act
        path = reverse_lazy("api-1.0.0:welcome")
        print(f"{path} - WELCOME")
        self.client.get("/api/")
        response = self.client.get(path)
        # assert
        assert response.status_code == 200, "API is not reachable"
        assert response.json() == {
            "message": "Welcome to the Integrated Smart Home API"
        }, "Unexpected response message"

    def test_hello(self):
        # act
        path = reverse_lazy("api-1.0.0:hello")
        response = self.client.get(path)
        # assert
        assert response.status_code == 200, "API is not reachable"
        assert response.json() == {
            "message": "Hello, World!"
        }, "Unexpected response message"

# Create your tests here.

# Name: Enter new Food Item 
# Identifier: UC-1
class UseCase1(TestCase):
	def 


# Name: Update Food Item
# Identifier: UC-2
class UseCase2(TestCase):
	def 


# Name: Enter Cleaning Chore 
# Identifier: UC-3 Base Course of Action

class UseCase3(TestCase):
	def 
	

# Name: Update Cleaning Chore 
# Identifier: UC-4 Base Course of Action

class UseCase4(TestCase):
	def 


# Name: View Food Inventory List 
# Identifier: UC-5  

class UseCase5(TestCase):
	def 

# Name: View Cleaning Chores 
# Identifier: UC-6 Base Course of Action

class UseCase6(TestCase):
	def 
