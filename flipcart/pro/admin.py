from django.contrib import admin
from pro.models import pro_table

# Register your models here.
class proAdmin(admin.ModelAdmin):
    list_display = ["id","name","price"]


admin.site.register(pro_table,proAdmin)
