from django.contrib import admin
from .models import About, SocialLink
# Register your models here.

class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):          #it is a builtin function that checks if an object can be added or not , means it restrict the addition of multiple objects
        count = About.objects.all().count()
        if count == 0:
            return True
        return False
    

admin.site.register(About, AboutAdmin)

admin.site.register(SocialLink)