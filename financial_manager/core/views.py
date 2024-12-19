from rest_framework import viewsets
from .models import Transaction, Project
from .serializers import ProjectSerializer, TransactionSerializer
# Create your views here.

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
