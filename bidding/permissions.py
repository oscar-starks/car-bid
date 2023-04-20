from rest_framework import permissions

class IsDealer(permissions.IsAuthenticated):
    message = "this user is not an approved dealer"

    def has_permission(self, request, view):
        is_authenticated = request.user.is_authenticated and request.user.dealer
        return bool(is_authenticated)
