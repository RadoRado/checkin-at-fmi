from django.contrib import admin

from models import Specialty, CustomUser, Book

#class UserAdmin(admin.ModelAdmin):
#    fields = ['first_name', 'last_name', 'card_key']
#    list_display = ['first_name', 'last_name']

class CustomUserAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'card_key', 'groups', 'specialty',
            'grade', 'username', 'email', 'valid']
    list_display = ['first_name', 'last_name', 'specialty', 'valid']
    

class SpecialtyAdmin(admin.ModelAdmin):
	fields = ['name']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Specialty, SpecialtyAdmin)
admin.site.register(Book)