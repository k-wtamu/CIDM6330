from django.db import models

# Create your models here.

class User(models.Model):
	userID = models.AutoField
	username = models.CharField(max_length=100)
	birthdate = models.DateField(null=True, blank=True)
	usericon = models.CharField(max_length=100)
	useremail = models.CharField(max_length=100)
#	userphonenumber = models.IntegerField


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
	