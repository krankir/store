from django.contrib import admin

from products.admin import BasketAdmin
from users.models import User


@admin.register(User)
class UserModel(admin.ModelAdmin):
    list_display = ('username',)
    inlines = (BasketAdmin,)
