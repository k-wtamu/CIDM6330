from django.urls import reverse_lazy, reverse
from ninja.testing import TestClient
from django.test import Client, RequestFactory, TestCase
from rest_framework import status
from rest_framework.test import APIClient
import json
import time
from job.api import router as list_router
from job.models import User, FoodItem, ChoreItem, ChoreSchedule


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


# Basic Tess
'''
	userID = models.AutoField
	username = models.CharField(max_length=100)
	birthdate = models.DateField(null=True, blank=True)
	usericon = models.CharField(max_length=100)
	useremail = models.CharField(max_length=100)
	
        self.user = User.objects.create_user(
            userID= 1, username="Jane", birthdate= datetime.date(1999, 1, 1) , usericon = "Star", email="janedoe@gmail.com"
        )
        self.user2 = User.objects.create_user(
            userID= 2, username="Jhon", birthdate= datetime.date(1980, 2, 2), usericon = "Smile", email="jhondoe@gmail.com"
        )
'''


# Name: Test if Enter new Food Item was successful 
# Identifier: UC-1
class UseCase1(TestCase):
    def setUp(self):
        # Setup run before every test method.
        pass
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            userID= 1, username="Jane", birthdate= datetime.date(1999, 1, 1) , usericon = "Star", email="janedoe@gmail.com"
        )
        self.user2 = User.objects.create_user(
            userID= 2, username="Jhon", birthdate= datetime.date(1980, 2, 2), usericon = 2 , email="jhondoe@gmail.com"
        )

    def test_fooditem_that_will_pass(self):
        # Create an instance of a GET request.
        request = self.factory.get("/user")
        request.user = self.user
        self.assertEqual(response.status_code, 200)
        print("Method: food item was entered properly - pass")
        time.sleep(30)

    def test_fooditem_that_will_fail(self):
        request = self.factory.get("/user")
        request.user = self.user2
        self.assertNOTEqual(response.status_code, 200)
        print("Method: food item was NOT entered properly - fail")
        time.sleep(30) # wait so I can see the test output

 ###https://docs.djangoproject.com/en/5.1/topics/testing/advanced/  --> first example but not using views 
 ## https://mattsegal.dev/alternate-test-styles.html
 ## https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django/Testing
 ## https://channels.readthedocs.io/en/stable/topics/testing.html
 

# Advanced Tests for Beyond CRUD API and Gherkin Expressions 


# Name: Check get_num_fav_fooditem returns a int value
# Identifier: UC-2
class UseCase2(TestCase):
    def setUp(self):
        # Setup run before every test method.
        pass
        self.client = APIClient()
        self.url = reverse('http://127.0.0.1:8000/api/numfavoritefooditem/')  # numfavfooditem url
    def test_api_output_type(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, int) # Check if output is a int


# Name: Check list_fav_fooditem returns a list 
# Identifier: UC-3  

class UseCase3(TestCase):
    def setUp(self):
        # Setup run before every test method.
        pass
        self.client = APIClient()
        self.url = reverse('http://127.0.0.1:8000/api/listfavoritefooditem/')  # list_fav_fooditem url
    def test_api_output_type2(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list) # Check if output is a list



# Name: 
# Identifier: UC-4  

class UseCase4(TestCase):
    def setUp(self):
        # Setup run before every test method.
        pass
	

test_task_initalSignup
self.assertEqual(lion.speak(), 'Welcome email sent to user {user.username}')

# Name:  
# Identifier: UC-5  

class UseCase5(TestCase):
    def setUp(self):
        # Setup run before every test method.
        pass


# Name: View  
# Identifier: UC-6  

class UseCase6(TestCase):
    def setUp(self):
        # Setup run before every test method.
        pass


