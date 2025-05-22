from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

# urlpatterns = [
#     path('spog_dashboard/', views.spog_dashboard, name='spog_dashboard'),
# ]

urlpatterns = [
    path('user-dashboard/', views.user_dashboard, name='user_dashboard'),
      #path('spog_dashboard/', views.spog_dashboard, name='spog_dashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
]