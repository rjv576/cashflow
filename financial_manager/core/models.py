from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_default = models.BooleanField(default=False) # Indica si es predefinida
    
    def __str__(self):
        return self.name

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('INCOME', 'Ingreso'),
        ('EXPENSE', 'Gasto'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.transaction_type}: {self.category} - {self.amount}"
    
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total_income = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    
    def get_profit(self):
        return self.total_income - self.total_cost
    
    def __str__(self):
        return self.name
    
