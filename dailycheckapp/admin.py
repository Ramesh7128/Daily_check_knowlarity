from django.contrib import admin
from dailycheckapp.models import Employee,Messages

# Register your models here.
class MessagesAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Username',               {'fields': ['employee']}),
        ('Messages', {'fields': ['messages']}),
    ]
    # fields = ['user', 'messages', 'data']

admin.site.register(Employee)
admin.site.register(Messages, MessagesAdmin)