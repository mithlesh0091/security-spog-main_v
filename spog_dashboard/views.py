from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import AutotaskTicket
from django.db.models import Count
from django.utils import timezone

# Delete this old view
# def spog_dashboard(request):
#     template = loader.get_template('spog_company_dashboard.html')
#     return HttpResponse(template.render())

# Add these new views
# @login_required
# def admin_dashboard(request):
#     if not request.user.is_superuser:
#         return redirect('user_dashboard')
#     return render(request, 'admin_dashboard.html')

# @login_required
# def user_dashboard(request):
#     return render(request, 'user_dashboard.html')
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        return redirect('user_dashboard')
    return render(request, 'registration/admin_dashboard.html')

@login_required
def user_dashboard(request):
    return render(request, 'registration/user_dashboard.html', {
        'user': request.user
    })

# def security_dashboard(request):
#     return render(request, 'registration/security_dashboard.html')



# def security_dashboard(request):
#     tickets = AutotaskTicket.objects.all()
#     status_counts = tickets.values('status').annotate(count=Count('status'))
    
#     # Convert to format needed for chart
#     labels = [item['status'] for item in status_counts]
#     values = [item['count'] for item in status_counts]
    
#     color_palette = [
#         "#b91d47", "#00aba9", "#2b5797", "#e8c3b9",
#         "#1e7145", "#00aba9", "#e8c3b9", "#b91d47", "#2b5797"
#     ]
    
#     return render(request, 'registration/security_dashboard.html', {
#         'status_data': {
#             'labels': labels,
#             'values': values,
#             'colors': color_palette[:len(labels)],
#             'total': tickets.count()
#         }
#     })

# def security_dashboard(request):
#     # Get start of today in UTC
#     today_start = timezone.now().replace(
#         hour=0, minute=0, second=0, microsecond=0
#     )
    
#     # Filter tickets created today
#     today_tickets = AutotaskTicket.objects.filter(
#         create_date__gte=today_start
#     )
    
#     # Get status counts for today's tickets
#     status_counts = today_tickets.values('status').annotate(
#         count=Count('status')
#     )
    
#     # Prepare chart data
#     labels = [item['status'] for item in status_counts]
#     values = [item['count'] for item in status_counts]
    
#     color_palette = [
#         "#b91d47", "#00aba9", "#2b5797", "#e8c3b9",
#         "#1e7145", "#00aba9", "#e8c3b9", "#b91d47", "#2b5797"
#     ]
    
#     return render(request, 'registration/security_dashboard.html', {
#         'status_data': {
#             'labels': labels,
#             'values': values,
#             'colors': color_palette[:len(labels)],
#             'total': today_tickets.count(),
#             'date_filter': "Today's"
#         }
#     })
#1630 spaces, 16th floor, max tower sector 16 b nodia.
def security_dashboard(request):
    today_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
    today_tickets = AutotaskTicket.objects.filter(create_date__gte=today_start)
    
    status_counts = today_tickets.values('status').annotate(count=Count('status'))

    
    # Calculate new tickets count
    new_count = today_tickets.filter(status="New").count()
    print()
    
    color_palette = [
        "#b91d47", "#00aba9", "#2b5797", "#e8c3b9",
        "#1e7145", "#00aba9", "#e8c3b9", "#b91d47", "#2b5797"
    ]
    
    return render(request, 'registration/security_dashboard.html', {
        'status_data': {
            'labels': [item['status'] for item in status_counts],
            'values': [item['count'] for item in status_counts],
            'colors': color_palette[:len(status_counts)],
            'total': today_tickets.count(),
            'date_filter': "Today's",
            'new_count': new_count  # Add new count to context
        }
    })

def zoho_dashboard(request):
    return render(request, 'registration/zoho_dashboard.html')