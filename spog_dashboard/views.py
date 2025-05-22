# from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader

# def spog_dashboard(request):
#     template = loader.get_template('spog_company_dashboard.html')
#     return HttpResponse(template.render())


# from django.shortcuts import render

# # from django.template import loader

# from django.template import loader
# from django.http import HttpResponse

# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required



# @login_required
# def admin_dashboard(request):
#     if not request.user.is_staff:
#         return redirect('user_dashboard')
#     return render(request, 'admin_dashboard.html')

# @login_required
# def user_dashboard(request):
#     return render(request, 'user_dashboard.html')



# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
# from django.template import loader

# # Remove the old spog_dashboard view and replace with these:
# def spog_dashboard(request):
#   template = loader.get_template('spog_company_dashboard.html')
#   return HttpResponse(template.render())

# @login_required
# def admin_dashboard(request):
#     if not request.user.is_superuser:  # Check if user is admin/superuser
#         return redirect('user_dashboard')  # Redirect non-admins to user dashboard
#     return render(request, 'admin_dashboard.html')

# @login_required
# def user_dashboard(request):
#     return render(request, 'user_dashboard.html')
# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.template import loader
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import redirect

# # Delete this old view
# def spog_dashboard(request):
#     template = loader.get_template('spog_company_dashboard.html')
#     return HttpResponse(template.render())

# # Add these new views
# @login_required
# def admin_dashboard(request):
#     if not request.user.is_superuser:
#         return redirect('user_dashboard')
#     return render(request, 'admin_dashboard.html')

# @login_required
# def user_dashboard(request):
#     return render(request, 'user_dashboard.html')
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

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