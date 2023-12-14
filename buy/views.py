from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
def pay(viewsets.ModelViewSet):
    
    serializer_class = UserSerializer
    queryset = User.objects.all()
