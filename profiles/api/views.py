from rest_framework import viewsets
from .serializers import CustomerSerializer
from profiles.models import Customer
#from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class CustomerModelViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
#    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]