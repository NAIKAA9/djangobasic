from django.contrib import admin
from django.urls import path, include

from studentDB import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('studentDB.urls')),
    path('profile/', views.user_profile, name='profile.html'),  # <-- comma added here
    path('accounts/', include('accounts.urls')),

]
