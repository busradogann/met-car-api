from django.shortcuts import render
from django.utils.module_loading import import_string

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from provider.models import Provider
from provider.serializers import CarListSerializer
import collections

class CarList(APIView):
	#permission_classes = (IsAuthenticated,)

	def get(self, *args, **kwargs):
		providers = Provider.objects.filter(status="active").all()
		response_data = []
		for provider in providers:
			adapter = provider.get_adapter
			result = adapter.search()
			response_data.extend(result)
		serializer = CarListSerializer(response_data, many=True)

		#en dusuk fiyatli aractan en yuksek fiyatli araca dogru siralama
		sorted_data = sorted(serializer.data, key = lambda i: i['total_amount'])
		
		#en dusuk fiyatli ayni model araci bulma
		sorted_list = []
		for sort in sorted_data:
			pass
		for sor in sorted_data:
			if sort['vehicle_name'] == sor['vehicle_name']:
				sorted_list.append(sor)            
		return Response(sorted_list)