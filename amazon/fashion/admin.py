from django.contrib import admin
from fashion.models import styles

# Register your models here.

class FashionAdmin(admin.ModelAdmin):
    list_display= ["id","fashion_name","delivery_date"]

admin.site.register(styles,FashionAdmin)

