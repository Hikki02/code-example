from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    ...


# @admin.register(UserPermission)
# class UserPermissionAdmin(admin.ModelAdmin):
#     ...
#
#
# @admin.register(UserRole)
# class UserRoleAdmin(admin.ModelAdmin):
#     ...
