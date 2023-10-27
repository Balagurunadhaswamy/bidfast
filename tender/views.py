from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Employee, TenderDetails
from django.contrib.auth.models import User
from datetime import datetime
# Create your views here.

def main(request):
	# import pdb; pdb.set_trace()
	if request.user.is_authenticated == True:
		user_id = request.user.id
		obj = Employee.objects.filter(id=user_id)
		# import pdb; pdb.set_trace()
		context = {'data':obj}
		return render(request, "tender.html", context)
	else:
		return HttpResponse("User not authenticated! Go back and kindly Login!")
	
def save(request):
	date = request.POST['date']
	company = request.POST['company']
	ph = request.POST['ph']
	ps = request.POST['ps']
	pp = request.POST['pp']
	fs = request.POST['fd']
	# import pdb; pdb.set_trace()
	if date == '':
		return HttpResponse("Please add the date")
	user = Employee.objects.get(phone_number = ph)
	store_date = datetime.strptime(date, '%Y-%m-%d').date()
	res = TenderDetails.objects.create(date=store_date, sender=user, prop_summary=ps, proj_planning=pp, financing_details=fs, company_name=company)
	return HttpResponse("The data has been saved in the Tender Details Model successfully!")