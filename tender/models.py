from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
import datetime
from django.core.exceptions import ValidationError
# Create your models here.


class Employee(models.Model):

	'''
	Model to extend the django base user class without changing the origianl in-built model, 
	Will store basic user details.

	I have regex validattor to validate the phone numbers.
	'''

	phone_regex = RegexValidator(regex=r'^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$', message="Phone number must be entered in the format: '+919999999999'. Up to 15 digits allowed.")

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	# phone = models.PositiveBigIntegerField()
	phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
	address = models.TextField()

	def __str__(self):
		return f"{self.user.username}"


class TenderDetails(models.Model):

	'''
	This model stores the Tender details once it is created for later use.
	I do not know a lot about tender proposals form, I have created a very basic info
	form. Please ignore the format of the proposal!
	'''

	date = models.DateField(default=datetime.date.today)
	company_name = models.CharField(max_length=50)
	title = models.CharField(max_length=20)
	sender = models.ForeignKey(Employee, on_delete=models.CASCADE)
	prop_summary = models.TextField()
	proj_planning = models.TextField()
	financing_details = models.TextField(default="To be filled")

	def save(self, *args, **kwargs):
		if self.date < datetime.date.today():
			raise ValidationError("The date cannot be in the past!")
		super(TenderDetails, self).save(*args, **kwargs)