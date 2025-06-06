from django.contrib import admin
from django.urls import path, include

# urls do app central e um include para ver as outras urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('to_do_list.urls')),
]
