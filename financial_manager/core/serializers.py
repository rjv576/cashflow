from rest_framework import serializers
from .models import Transaction, Project, Category

class TransactionSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField() 
    class Meta:
        model = Transaction
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'