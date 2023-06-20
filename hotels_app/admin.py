from django.contrib import admin
from hotels_app.models import NumberReserved, WorkingPosition, UserReserved, Number, User


class NumberReservedAdmin(admin.ModelAdmin):
    list_display = ["id", "type", "date_start_reserved", "date_end_reserved", "email_reserved", 'phone_reserved','name' ]

class WorkingPositionAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]

class UserReservedAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "phone"]

class NumberAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "type", "rooms"]

class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "first_name", 'last_name', 'email', 'get_positon']
    
    def get_positon(self, obj):
        if obj.working_position:
            return obj.working_position.title
        return ''
    get_positon.short_description = 'Должность'
    get_positon.admin_order_field = 'working_position__title'

admin.site.register(NumberReserved, NumberReservedAdmin)
admin.site.register(WorkingPosition, WorkingPositionAdmin)
admin.site.register(UserReserved, UserReservedAdmin)
admin.site.register(Number, NumberAdmin)
admin.site.register(User, UserAdmin)

