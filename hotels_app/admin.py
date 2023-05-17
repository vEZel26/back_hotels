from django.contrib import admin
from hotels_app.models import NumberReserved


class NumberReservedAdmin(admin.ModelAdmin):
    list_display = ["id", "type", "date_start_reserved", "date_end_reserved", "email_reserved", 'phone_reserved']

admin.site.register(NumberReserved, NumberReservedAdmin)

