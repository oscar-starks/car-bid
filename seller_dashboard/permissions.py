from rest_framework import permissions

class IsInstructor(permissions.IsAuthenticated):
    message = "this user is not an approved seller"

    def has_permission(self, request, view):
        is_authenticated = request.user.is_authenticated and request.user.approved_seller
        return bool(is_authenticated)
