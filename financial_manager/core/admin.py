from django.contrib import admin
from .models import Transaction, Project,CustomUser
# Register your models here.

admin.site.register(Transaction)
admin.site.register(Project)
admin.site.register(CustomUser)