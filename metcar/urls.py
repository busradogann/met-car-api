from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from main.views import CarList

urlpatterns = [
	path('', CarList.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('admin/', admin.site.urls),
]
