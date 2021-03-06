from app import serializers, models

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth.models import User
from app import models
from app import serializers


class GetFaultsByReporter(generics.ListAPIView):
    serializer_class = serializers.FaultsSerializer

    def get_queryset(self):
        reporter = self.kwargs['reporter']
        user = User.objects.get(username=reporter)
        citi = models.Citizen.objects.get(user_id=user.id)
        return models.Fault.objects.filter(reporters=citi.id)


class GetAllFaults(generics.ListCreateAPIView):
    queryset = models.Fault.objects.all()
    serializer_class = serializers.FaultSerializer


class RegisterCitizen(generics.ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class ListCreateCitizen(generics.ListCreateAPIView):
    queryset = models.Citizen.objects.all()
    serializer_class = serializers.CitizenSerializer


class GetCaseManager(generics.ListAPIView):
    serializer_class = serializers.CaseManagerSerializer

    def get_queryset(self):
        user = models.User.objects.get(username=self.request.user)
        emp = models.Employee.objects.get(user_id=user.id)
        return models.CaseManager.objects.filter(responder_id=emp.id)


class GetAllCases(generics.ListAPIView):
    queryset = models.CaseManager.objects.all()
    serializer_class = serializers.CaseManagerSerializer


class GetEmployees(generics.ListAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer


class GetUser(generics.ListAPIView):
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        return User.objects.filter(username=username)
    

class GetCitizen(generics.ListAPIView):
    serializer_class = serializers.CitizenSerializer

    def get_queryset(self):
        citizen_id = int(self.kwargs['citizen_id'])
        return models.Citizen.objects.filter(pk=citizen_id)


class GetEmployee(generics.ListAPIView):
    serializer_class = serializers.EmployeeSerializer

    def get_queryset(self):
        emp_id = self.kwargs['emp_id']
        return models.Employee.objects.filter(pk=int(emp_id))


class GetClientAddress(generics.ListCreateAPIView):
    serializer_class = serializers.AddressSerializer

    def get_queryset(self):
        return models.Address.objects.all()


class GetVacancies(generics.ListAPIView):
    queryset = models.Vacancy.objects.all().order_by('posting_date')
    serializer_class = serializers.VacancySerializer
