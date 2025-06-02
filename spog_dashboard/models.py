# spog_dashboard/models.py
from django.db import models

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