from django.contrib import admin
from .models import AjoGroup,AjoMembers,AjoGenerator

admin.site.register(AjoGroup)
admin.site.register(AjoMembers)
admin.site.register(AjoGenerator)