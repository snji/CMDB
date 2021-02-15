from django.contrib import admin
from .models import Server,users
# Register your models here.
class server_admin(admin.ModelAdmin):
    list_display = ['IP','server_type','create_by']
    list_filter = ['server_type','create_by']
    search_fields = ['IP']


class user_admin(admin.ModelAdmin):
    list_display =['username','password','server']
admin.site.register(Server,server_admin)
admin.site.register(users,user_admin)