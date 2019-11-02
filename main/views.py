from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class CarList(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request, format=None):
		content = {"qwe": 12345}
		return Response(content) 