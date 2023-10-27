from django.contrib import admin
from .models import TenderDetails, Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
	list_display = ['user', 'phone_number']
admin.site.register(Employee, EmployeeAdmin)

class TenderDetailsAdmin(admin.ModelAdmin):
	list_display = ['company_name', 'title', 'sender', 'date']
admin.site.register(TenderDetails, TenderDetailsAdmin)