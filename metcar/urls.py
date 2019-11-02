from django.contrib import admin
from django.urls import path

from main.views import CarList

urlpatterns = [
	path('', CarList.as_view()),
    path('admin/', admin.site.urls),
]
