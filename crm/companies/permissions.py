from rest_framework import permissions


class AdminPermission(permissions.BasePermission):
    """
    Разрешение для администратора
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_role == 'admin'
