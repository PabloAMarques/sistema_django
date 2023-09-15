from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('web_interface.urls')),  
    path('admin/', admin.site.urls),
    path('api/', include('web_interface.urls')),  
    path('accounts/', include('django.contrib.auth.urls')),

]
