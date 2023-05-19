from django.contrib import admin
from hotels_app.models import NumberReserved, WorkingPosition, UserReserved, Number


class NumberReservedAdmin(admin.ModelAdmin):
    list_display = ["id", "type", "date_start_reserved", "date_end_reserved", "email_reserved", 'phone_reserved']

class WorkingPositionAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]

class UserReservedAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "phone"]

class NumberAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "type", "rooms"]


admin.site.register(NumberReserved, NumberReservedAdmin)
admin.site.register(WorkingPosition, WorkingPositionAdmin)
admin.site.register(UserReserved, UserReservedAdmin)
admin.site.register(Number, NumberAdmin)

