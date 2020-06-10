from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Problem, Order, Part, PartStage, Car


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'required': True, 'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class CarDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['name']


class PartListSerializer(serializers.ModelSerializer):
    car = CarDetailSerializer(many=True)

    class Meta:
        model = Part
        fields = ['car', 'name', 'number']


class PartStageListSerializer(serializers.ModelSerializer):
    part = PartListSerializer(many=False)

    class Meta:
        model = PartStage
        fields = ['part', 'stage']


class OrderListSerializer(serializers.ModelSerializer):
    part = PartStageListSerializer(many=True)

    class Meta:
        model = Order
        fields = ['number', 'date_time_delivery', 'part']


class ProblemDetailSerializer(serializers.ModelSerializer):
    order = OrderListSerializer(many=True)

    class Meta:
        model = Problem
        fields = '__all__'


class ProblemListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Problem
        fields = ['number', 'description']


class OrderDetailSerializer(serializers.ModelSerializer):
    part = PartStageListSerializer(many=True)
    problem = ProblemListSerializer(many=False)

    class Meta:
        model = Order
        fields = '__all__'


class PartStageDetailSerializer(serializers.ModelSerializer):
    part = PartListSerializer(many=False)
    order = OrderListSerializer(many=True)

    class Meta:
        model = PartStage
        fields = '__all__'


class PartStageShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = PartStage
        fields = ['stage']


class PartDetailSerializer(serializers.ModelSerializer):
    car = CarDetailSerializer(many=True)
    part_stage = PartStageShortSerializer(many=True)

    class Meta:
        model = Part
        fields = '__all__'
