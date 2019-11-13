from django.shortcuts import render
from django.utils.module_loading import import_string

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from provider.models import Provider


class CarList(APIView):
	#permission_classes = (IsAuthenticated,)

	def get(self, *args, **kwargs):
		providers = Provider.objects.filter(status="active").all()
		print(providers)
		response_data = []
		for provider in providers:
			adapter = provider.get_adapter
			result = adapter.search()
			response_data.append(result['results'])

			if response_data:
				return Response(response_data, status=status.HTTP_200_OK)
		return Response(response_data)