import json
import boto3
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta
from django.db.models import Count
from .models import AutotaskTicket, Employee, Position, Schedule  # Make sure these are correct
from .models import EmployeeShift  # Your actual model for shifts
from .models import AutotaskTicketStatus  # Adjust the import path as needed
from django.utils.dateparse import parse_datetime
import logging
from django.contrib.auth.views import LoginView
from .models import Client


logger = logging.getLogger(__name__)

from django.contrib.auth.decorators import login_required
from .decorators import role_required

@login_required
@role_required(allowed_roles=['superadmin'])
def superadmin_dashboard(request):
    return render(request, 'registration/superadmin_dashboard.html')

@login_required
@role_required(allowed_roles=['admin', 'superadmin'])
def admin_dashboard(request):
    return render(request, 'registration/admin_dashboard.html')


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def form_valid(self, form):
        # Check Remember Me
        remember_me = self.request.POST.get('remember_me')

        # Log the user in
        response = super().form_valid(form)

        if remember_me:
            # Session expiry for 30 days
            self.request.session.set_expiry(60 * 60 * 24 * 30)  # 30 days
        else:
            # Session expires on browser close
            self.request.session.set_expiry(0)

        return response
    
# @login_required
# def client_dashboard(request):
#     clients = Client.objects.all().order_by('client_name')
#     client_id = request.GET.get('client_id')
#     selected_client = None
#     if client_id:
#         selected_client = Client.objects.filter(client_id=client_id).first()
#     return render(request, 'registration/client_view.html', {
#         'clients': clients,
#         'selected_client': selected_client
#     })

def client_login(request):
    return render(request, 'registration/client_login.html')
@login_required
def client_dashboard(request):
    clients = Client.objects.all()
    client_id = request.GET.get('client_id')
    selected_client = None
    if client_id:
        selected_client = Client.objects.filter(client_id=client_id).first()
    return render(request, 'registration/client_view.html', {
        'clients': clients,
        'selected_client': selected_client
    })


