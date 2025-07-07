# spog_dashboard/models.py
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('superadmin', 'Super Admin'),
        ('admin', 'Admin'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} ({self.role})"


class Client(models.Model):
    client_id = models.BigIntegerField(primary_key=True)
    client_name = models.TextField()
    client_type = models.TextField(blank=True, null=True)
    parent_company_name = models.TextField(blank=True, null=True)
    territory = models.TextField(blank=True, null=True)
    address_1 = models.TextField(blank=True, null=True)
    address_2 = models.TextField(blank=True, null=True)
    country_name = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    postal_zip = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    company_number = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'spog_dashboard_clients'  # Important to match your table



class AutotaskTicket(models.Model):
    id = models.BigIntegerField(primary_key=True)
    ticket_number = models.CharField(max_length=255)
    title = models.TextField()
    description = models.TextField()
    status = models.CharField(max_length=50)
    priority = models.IntegerField()
    company_id = models.BigIntegerField()
    contact_id = models.BigIntegerField()
    assigned_resource_id = models.BigIntegerField()
    create_date = models.DateTimeField()
    last_activity_date = models.DateTimeField()
    resolved_date = models.DateTimeField(null=True)
    due_date = models.DateTimeField(null=True)
    resolution = models.TextField(null=True)

    class Meta:
        managed = False
        db_table = 'autotask_tickets'

# models.py
class AutotaskTicketStatus(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.TextField()
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=100)
    create_date = models.DateTimeField()
    ticketNumber = models.CharField(max_length=20, blank=True, null=True)




# models.py

class Position(models.Model):
    id = models.BigIntegerField(primary_key=True)  # Changed here
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=50)

class Schedule(models.Model):
    id = models.BigIntegerField(primary_key=True)  # Changed here
    name = models.CharField(max_length=255)

class Employee(models.Model):
    id = models.BigIntegerField(primary_key=True)  # Changed here
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=100, default='Unknown')
    employee = models.CharField(max_length=255, default='Unknown')
    work_email = models.EmailField()
    mobile_dialing_code = models.CharField(max_length=10, null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    mobile_country_code = models.CharField(max_length=10, null=True, blank=True)
    zuid = models.CharField(max_length=50, null=True, blank=True)
    invite_status = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    photo_url = models.URLField(null=True, blank=True)
    access_level_id = models.CharField(max_length=50)

    positions = models.ManyToManyField(Position, related_name='employees')
    schedules = models.ManyToManyField(Schedule, related_name='employees')


class EmployeeShift(models.Model):
    id = models.CharField(primary_key=True, max_length=50)  # Zoho shift ID as primary key
    employee_id = models.CharField(max_length=50, null=True, blank=True)  # Store employee ID as string or ForeignKey if you have Employee model
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    schedule = models.CharField(max_length=100, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    color = models.CharField(max_length=30, null=True, blank=True)
    is_published = models.BooleanField(default=False)
    is_confirmed = models.BooleanField(default=False)
    break_duration = models.CharField(max_length=20, null=True, blank=True)
    duration = models.CharField(max_length=20, null=True, blank=True)
    pay = models.CharField(max_length=20, null=True, blank=True)
    rate = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"Shift {self.id} for Employee {self.employee_id}"

