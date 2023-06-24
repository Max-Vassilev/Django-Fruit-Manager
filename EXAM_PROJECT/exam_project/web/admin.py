from django.contrib import admin
from exam_project.web.models import Profile, Fruit


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Fruit)
class FruitAdmin(admin.ModelAdmin):
    pass
