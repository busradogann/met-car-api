from rest_framework import serializers


class CarListSerializer(serializers.Serializer):
	vehicle_name = serializers.CharField(max_length=40)
	is_available = serializers.BooleanField()
	total_amount = serializers.IntegerField()
	currency =  serializers.CharField(max_length=20)