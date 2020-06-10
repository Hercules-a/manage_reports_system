from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Problem, Order, PartStage, Part, Car
from .serializers import UserSerializer, ProblemDetailSerializer, OrderDetailSerializer, PartStageDetailSerializer
from .serializers import PartDetailSerializer, CarDetailSerializer, OrderListSerializer, ProblemListSerializer
from .serializers import PartStageListSerializer, PartListSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class ProblemViewSet(viewsets.ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemDetailSerializer

    def list(self, request, *args, **kwargs):
        self.serializer_class = ProblemListSerializer
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(self.queryset, many=True)

        return Response(serializer.data)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer

    def list(self, request, *args, **kwargs):
        self.serializer_class = OrderListSerializer
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(self.queryset, many=True)

        return Response(serializer.data)


class PartStageViewSet(viewsets.ModelViewSet):
    queryset = PartStage.objects.all()
    serializer_class = PartStageDetailSerializer

    def list(self, request, *args, **kwargs):
        self.serializer_class = PartStageListSerializer
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(self.queryset, many=True)

        return Response(serializer.data)


class PartViewSet(viewsets.ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartDetailSerializer

    def list(self, request, *args, **kwargs):
        self.serializer_class = PartListSerializer
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(self.queryset, many=True)

        return Response(serializer.data)


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarDetailSerializer
