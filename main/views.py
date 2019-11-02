from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView


class CarList(APIView):
	def get(self, request, format=None):
		 return Response({"qwe": 123})